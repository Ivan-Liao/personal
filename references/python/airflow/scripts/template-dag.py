"""
Documentation
Description: 

Changelog:
Date            Author          Description
2021-06-14      Ivan Liao       Created.
"""




"""
Imports
"""
# airflow imports
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
# Operator list ... BranchPythonOperator, EmailOperator, SimpleHttpOperator, MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, JdbcOperator, Sensor, DockerOperator, HiveOperator, S3FileTransformOperator, PrestoToMysqlOperator, SlackOperator, DummyOperator
# airflow/contrib/ have community built operators like SSHOperator

# common imports
from datetime import timedelta, datetime
import time
import sys
import os
import pandas as pd
import numpy as np




"""
General Configuration
"""
# bring in Scripts dir for importing
sys.path.append('/opt/airflow_repo/Scripts')

# default_args configuration
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup_by_default': False, # prevents schedule backfilling
}




"""
Dags and Tasks
"""
# template dag is instantiated
template_dag = DAG(
    'dag_name',
    start_date=datetime(2021,5,12,6,0,00), # (year, month, day, hour, minute, second)
    # start_date=days_ago(2),
    # end_date=datetime(2016, 1, 1), # (year, month, day)
    default_args=default_args,
    description='A template DAG',
    schedule_interval='*/10 8-18 * * 1-5', # every 10 minutes from 8 am to 6 pm, Monday through Friday,
    tags=['example'],
)

# example of PythonOperator task referencing python function in the same file
def csv_to_json():
    df=pd.read_csv('input file path')
    for i, row in df.iterrows():
        print(row['column name'])
    df.to_json('output file path',orient='records')

python_task_1 = PythonOperator(
    task_id='csv_to_json',
    python_callable = csv_to_json
)
python_task_1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""

# example of PythonOperator task referencing python script
# import ExtractDremioMetadata_RefreshDataSet # remember to import in import section
def refreshdataset_list(ti):
    print("Starting data set extract..")
    ExtractDremioMetadata_RefreshDataSet.ExtractDremioObjectDataSet()
    print("Finished extracting data set")

python_task_2 = PythonOperator(
    task_id='refreshing_dataset',
    python_callable=refreshdataset_list
)

# simple example of BashOperator Task referencing bash command in the same file with task documentation
bash_task_1 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=template_dag,
)

# example of BashOperator task referencing bash shell script
scripted_bash_command = "bash_script_name.sh"
bash_task_2 = BashOperator(
    task_id='scripted',
    depends_on_past=False,
    bash_command=scripted_bash_command,
    params={'my_param': 'Parameter I passed in'},
    dag=template_dag,
)




"""
Bitshift Composition, where we define the DAG edges
"""
# Define DAG below with bitshift composition
# example ... bash_task_1 >> [bash_task_2, python_task_1] >> python_task_2




"""
Schedule Interval Reference
https://crontab.guru/ is a useful tool for creating cron expressions
#Using cron presets
* None ... unscheduled, only runs upon external trigger
* @once ... only runs once at start_date
* @hourly ... translates to '0 * * * *'
* @daily ... translates to '0 0 * * *'
* @weekly ... translates to '0 0 * * 0'
* @monthly ... translates to '0 0 1 * *'
* @yearly ... translates to '0 0 1 1 *'
#Using cron expressions
* syntax is '<minute 0-59> <hour 0-23> <day of month 1-31> <month 1-12> <day of week 0-6 (0 is sunday)>' 
* '*' means any
* use '*/x' for every x interval ... '*/5 * * * *' is every 5 minutes
* use 'x-y' for ranges from x to y ... '0 8-17 * *' is once every hour between 08:00 and 17:00 inclusive
* use 'x,y,z' for a list of values x, y, and z ... '0,15,30 * * * *' is every 0th, 15th, and 30th minute for any hour
* '* * * * 0' is every Sunday
* '*/10 1,3,5 5 1-3 6' is every 10 minutes on 1 a.m., 3 a.m., and 5 a.m. on the 5th day of January, Februrary, and March if it is a Saturday
#Using timedelta 
* import statement is 'from datetime import timedelta'
* schedule_interval=timedelta(days=1) # other arguments ... weeks, hours, minutes, seconds, microseconds milliseconds
"""
