"""
Documentation
Description: Creates a file called ivan_test.txt on /nfs/data_store/dremio/nas/tst/test_ivan.txt after
using SSHOperator to connect to dsutil1.

Changelog:
Date            Author          Description
2021-07-02      Ivan Liao       Converted from ssh_hook on local setup to EA airflow setup
2021-06-14      Ivan Liao       Created.
"""




"""
Imports
"""
# airflow imports
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.models import Variable
import logging


# common imports
from datetime import timedelta, datetime

# Operator list ... BranchPythonOperator, EmailOperator, SimpleHttpOperator, MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, JdbcOperator, Sensor, DockerOperator, HiveOperator, S3FileTransformOperator, PrestoToMysqlOperator, SlackOperator, DummyOperator
# airflow/contrib/ have community built operators 

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
append_to_text_dag = DAG(
    'append_to_text_file_dag',
    start_date=datetime(2021,5,12,6,0,00), # (year, month, day, hour, minute, second)
    default_args=default_args,
    description='A dag that appends the string "run" to a file in the home directory named "test_ivan.txt"',
    schedule_interval='*/1 * * * *', # every 10 minutes from 8 am to 6 pm, Monday through Friday,
    tags=['example'],
)

create_append_command = """
#!/bin/bash

if [ ! -f /nfs/data_store/dremio/nas/tst/test_ivan.txt ]
then
    touch /nfs/data_store/dremio/nas/tst/test_ivan.txt
fi
echo run >> /nfs/data_store/dremio/nas/tst/test_ivan.txt
"""

"""
Bitshift Composition, where we define the DAG edges
"""

ssh_create_append = SSHOperator(
    task_id='create_append',
    ssh_conn_id = Variable.get("SSH_DSUTIL1"),
    command=create_append_command,
    dag=append_to_text_dag,
)

# Define DAG below with bitshift composition
# example ... bash_task_1 >> [bash_task_2, python_task_1] >> python_task_2
ssh_create_append




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
