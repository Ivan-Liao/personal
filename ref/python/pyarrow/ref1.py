import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow import parquet as pq


df = pd.DataFrame({'one': [20, np.nan, 2.5],'two': ['january', 'february', 'march'],'three': [True, False, True]},index=list('abc'))
# pandas to pyarrow
table = pa.Table.from_pandas(df)
# pandas to pyarrow no index
table5 = pa.Table.from_pandas(df, preserve_index=False)
# check metadata and schema
parquet_file = pa.parquet.ParquetFile('example.parquet')
parquet_file.metadata
parquet_file.schema
# csv to pyarrow
fn = 'data/demo.csv'
table2 = pa.csv.read_csv(fn)
# pyarrow to pandas 
df_new = table.to_pandas()
# pyarrow to parquet
pq.write_table(table, 'example.parquet')
# pyarrow to parquet with compatible timestamp, pandas uses nanoseconds
pq.write_table(table, 'example.parquet', coerce_timestamps='ms', allow_truncated_timestamps=True)
# pyarrow to parquet with compression configuration
pq.write_table(table, 'example.parquet', compression='snappy')
pq.write_table(table, 'example.parquet', compression='gzip')
pq.write_table(table, 'example.parquet', compression='brotli')
pq.write_table(table, 'example.parquet', compression='none')
pq.write_table(table, 'example_diffcompr.parquet', compression={b'one': 'snappy', b'two': 'gzip'})
# parquet to pyarrow
table3 = pa.read_table('example.parquet')
# parquet to pyarrow, specific columns
table4 = pa.read_table('example.parquet', columns=['one', 'three'])
# writing a partitioned Parquet table
pq.write_to_dataset(table, root_path='example.parquet',partition_cols=['one','two'])
# working with HDFS
# reading other data types (sas, excel, json)