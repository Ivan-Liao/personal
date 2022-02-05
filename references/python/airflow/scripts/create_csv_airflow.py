import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

def csvToJson():
    df=pd.read_csv('/mnt/c/all/ref/data_engineering_with_python/datas/data1.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('/mnt/c/all/ref/data_engineering_with_python/datas/from-airflow.json',orient='records')

	


default_args = {
    'owner': 'ivanli',
    'start_date': dt.datetime(2021, 5, 27, 22, 35),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'catchup_by_default' : False,
}


with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),      # '0 * * * *',
         ) as dag:

    print_starting = BashOperator(task_id='starting',
                               bash_command='echo "I am reading the CSV now....."')
    
    csvJson = PythonOperator(task_id='convertCSVtoJson',
                                 python_callable=csvToJson)


print_starting >> csvJson
