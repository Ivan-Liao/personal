import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow import parquet as pq


df = pd.DataFrame({'one': [20, 40, np.nan, 2.5],'two': ['january', 'january', 'february', 'march'],'three': [True, True, False, True]},index=list('abcd'))
table = pa.Table.from_pandas(df)
pq.write_to_dataset(table, root_path='./data',partition_cols=['two'])