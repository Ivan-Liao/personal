import pandas as pd
import requests
import io

def request_data():
    # requests US country data as df_us
    url = 'https://api.covidtracking.com/v1/us/daily.csv'
    s = requests.get(url).content
    cols_to_use = ['date', 'hospitalizedCurrently', 'deathIncrease', 'positiveIncrease']
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), usecols=cols_to_use)
    df_us = extract_data_covidtracking_us(df)

    # requests US states data as df_states
    url = 'https://api.covidtracking.com/v1/states/daily.csv'
    s = requests.get(url).content
    cols_to_use = ['date', 'state', 'hospitalizedCurrently', 'deathIncrease', 'positiveIncrease']
    df_states = pd.read_csv(io.StringIO(s.decode('utf-8')), usecols=cols_to_use)

    # requests Global data as df_global
    url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/worldwide-aggregate.csv'
    s = requests.get(url).content
    cols_to_use = ['Date', 'Confirmed', 'Deaths']
    df_global = pd.read_csv(io.StringIO(s.decode('utf-8')), usecols=cols_to_use)
    df_global = extract_data_covid19_global(df_global)

    return df_us, df_states, df_global

def extract_data_covidtracking_us(df):
    df.date = pd.to_datetime(df.date, format='%Y%m%d')

    # make moving average columns for hospitalizations, deaths, cases
    s1 = df.hospitalizedCurrently.rolling(window=7).mean().round()
    s1.name = 'hospitalizedCurrentlyMA'
    s2 = df.deathIncrease.rolling(window=7).mean().round()
    s2.name = 'deathIncreaseMA'
    s3 = df.positiveIncrease.rolling(window=7).mean().round()
    s3.name = 'positiveIncreaseMA'
    df = pd.concat([df, s1, s2, s3], axis=1)
    return df


def extract_data_covidtracking_states(df, state_input):
    # convert date column to datetime
    df.date = pd.to_datetime(df.date, format='%Y%m%d')

    # group states data by date because of multiple daily reports
    df = df[df['state'] == state_input]
    df = df.groupby(['date']).sum()
    df = df.reset_index('date')

    # make moving average columns for hospitalizations, deaths, cases
    s1 = df.hospitalizedCurrently.rolling(window=7).mean().round()
    s1.name = 'hospitalizedCurrentlyMA'
    s2 = df.deathIncrease.rolling(window=7).mean().round()
    s2.name = 'deathIncreaseMA'
    s3 = df.positiveIncrease.rolling(window=7).mean().round()
    s3.name = 'positiveIncreaseMA'
    df = pd.concat([df, s1, s2, s3], axis=1)
    df = df.sort_values(by='date', ascending=False)
    return df


def extract_data_covid19_global(df):
    # to datetime, also renames date column for compatibility with covidtracking column names
    df.rename(columns={'Date': 'date', 'Confirmed': 'positiveIncrease', 'Deaths': "deathIncrease"}, inplace=True)
    df.date = pd.to_datetime(df.date, format='%Y-%m-%d')

    # converts aggregate df to daily increases
    df['positiveIncrease'] = df['positiveIncrease'].diff()
    df['deathIncrease'] = df['deathIncrease'].diff()
    df.dropna(inplace=True)
    df.sort_values('date', ascending=False, inplace=True)

    # adds moving average columns
    s1 = df.positiveIncrease.rolling(window=7).mean().round()
    s1.name = 'positiveIncreaseMA'
    s2 = df.deathIncrease.rolling(window=7).mean().round()
    s2.name = 'deathIncreaseMA'
    df = pd.concat([df, s1, s2], axis=1)
    return df
