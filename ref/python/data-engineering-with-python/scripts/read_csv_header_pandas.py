'''
Reading a csv with pandas package.
Limited to first 100 rows.

Also creates a dataframe and save some fake test data
'''
import pandas as pd
from faker import Faker

df1=pd.read_csv('../data/data1.csv', nrows=100)
print(df1.head(10))
fake = Faker()
name_list = [fake.name() for i in range(100)]
age_list = [fake.random_int(min=1, max=91, step=1) for i in range(100)]
temp = {'Name': name_list, 'Age': age_list}
df2 = pd.DataFrame(temp)
df2.to_csv('../data/data2.csv', index=True)