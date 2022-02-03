# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:20:10 2021

@author: Ivan6461
"""


import pyodbc

host = "dremtstent"
port = 31010
uid = 'Ivan6461'
# ***put in password***
pwd = ''
driver = "Dremio Connector"

conn = pyodbc.connect("Driver={}; ConnectionType=Direct; HOST={}; PORT={}; AuthenticationType=Plain; UID={}; PWD={}".format(driver, host,port,uid,pwd),autocommit=True)


print("Successfully connected to Dremio")

cursor = conn.cursor()

row_list = cursor.execute(
    """
    select *
    from EnterpriseData.InformationServices.BacklogProjects
    FETCH FIRST 5 ROWS ONLY
    """)
    
for row in row_list:
    print(row)