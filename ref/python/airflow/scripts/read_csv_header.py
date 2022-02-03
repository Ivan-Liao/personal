# with csv package
import csv

with open('../data/data1.csv') as f:
    reader = csv.DictReader(f)
    header = next(reader)
    count = 0
    for row in reader:
        if (count < 100):
            print(row['name'], ' ', row['city'])
            count += 1