import csv


filename = 'imountle13_2018-08-01_2018-09-30.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    