import csv


#Stores file location for csv module
filename = 'imountle13_2018-08-01_2018-09-30.csv'

#Pull and store temps to an array
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    temps = []
    for row in reader:
        #Parse Temperature data and convert to Freedom units and round.
        temp = round(float(row[2]) * 1.8 + 32)
        temps.append(temp)
    print (temps)
