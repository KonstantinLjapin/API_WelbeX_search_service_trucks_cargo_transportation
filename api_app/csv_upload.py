import csv

with open('uszips.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        break
