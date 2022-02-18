import os
import shutil
import pandas as pd
from datetime import datetime

# configuration
UNPROCESSED_DIR = "./input/unprocessed"
PROCESSED_DIR = "./input/processed"
OUTPUT_DIR = "./output"
OUTPUT_LATEST = "./output/latest.csv"

# batch process incoming files
def batch_process():
    """
    This function batch processes files in the ./input/unprocessed directory and updates the latest.csv file in ./output.  Along the way, snapshots of the output data are created in the form asof_2022-02-15T2010.csv.  Processed data is removed from ./input/unprocessed and retained in the ./input/processed directory.

    inputs: None
    outputs: None
    """
    for root, _, files in os.walk(UNPROCESSED_DIR):
        dfs = []
        for file in files:
            print(root, " ", file)
            df = pd.read_csv(os.path.join(root, file))
            # add column for source_filename and give it a constant value of the variable file
            df['source_filename'] = file
            dfs.append(df)
            shutil.move(os.path.join(root, file), os.path.join(PROCESSED_DIR, file))
        concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
        concatenated_top_per_uuid_df = concatenated_df.sort_values('id', ascending=False).groupby('id').head(1)
        # initialize latest.csv if doesn't exists
        if not os.path.exists(OUTPUT_LATEST):
            concatenated_top_per_uuid_df.to_csv(f"./output/latest.csv", index=False)
        else:
            # save snapshot of old output
            shutil.copyfile(OUTPUT_LATEST, OUTPUT_DIR + f"/asof_{datetime.now().strftime('%Y-%m-%dT%H%M')}.csv")
            # compute new latest.csv
            previous_latest = pd.read_csv(OUTPUT_LATEST)
            previous_plus_batch_df = pd.concat([previous_latest,concatenated_top_per_uuid_df])
            previous_plus_batch_top_per_uuid_df = previous_plus_batch_df.sort_values('id', ascending=False).groupby('id').head(1)
            previous_plus_batch_top_per_uuid_df.to_csv(f"./output/latest.csv", index=False)

if __name__ == '__main__':
    pass