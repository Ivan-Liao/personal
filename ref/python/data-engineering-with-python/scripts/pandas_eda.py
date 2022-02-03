import pandas as pd
import datetime
import time

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_min(time_str):
    """Get Minutes from time."""
    h, m, s = time_str.split(':')
    return int(h) * 60 + int(m) + int(s) / 60

# reading csv
df=pd.read_csv('../data/scooter.csv')

# pandas configuration
pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,}'.format

# display columns, dtypes, first 5 rows, last 5 rows
print('\n\nprinting columns:')
print(df.columns)
print('\n\nprinting dtypes')
print(df.dtypes)
print('\n\nprinting first 5 rows')
print(df.head())

# describe statistics
print('\n\nprinting describe statistics of entire dataset')
print(df.describe(include='all'))
print('\n\nprinting describe statistics of DURATION column')
print(df['DURATION'].describe())

print(df.DURATION.unique)
# value counts
print('\n\nprinting value counts')
print(df.DURATION.value_counts())
print('\n\nvalue counts with bins')
df['DURATION_minutes'] = [get_min(str(duration)) if ':' in str(duration) else None for duration in df['DURATION']]
# condition where duration is less than an hour
cond_lt_one_hour = (df.DURATION_minutes <= 60) & (df.DURATION_minutes) > 0
print(df.DURATION_minutes.where(cond_lt_one_hour).value_counts(dropna=False, bins=20, sort=False))

# display multiple specified columns
print('\n\nprinting user_id, DURATION')
print('\n\n', df[['user_id', 'DURATION']])

# sample data
print(df.sample(5))

# filtering on multiple conditions
one=df['user_id']==8417864
two=df['trip_ledger_id']==1488838
df.where(one & two)

# finding out number of null values
print('\n\ncounting null values')
print(df.isnull().sum())

# dropping columns and rows
# df.drop(columns=['region_id'], inplace=True)
# df.drop(index=[34225],inplace=True)
# df.dropna(subset=['start_location_name'],inplace=True)
# # to pass a threshold of 25% or less nulls
# thresh=int(len(df)*.25)
# df.dropna(thresh=thresh, inplace=True)

# fillna
startstop=df[(df['start_location_name'].isnull())&(df['end_location_name'].isnull())]
value={'start_location_name':'Start St.','end_location_name':'Stop St.'}
startstop.fillna(value=value)
startstop[['start_location_name','end_location_name']]

# standardizing column names, can also use upper() or capitalize()
# df.columns=[x.lower() for x in df.columns]
df.rename(columns={'DURATION':'duration'},inplace=True)