import csv

from matplotlib import pyplot as plt
#Stores file location for csv module
filename = 'sitka_weather_07-2014.csv'

#Pull and store high temps to an array
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        #Parse Temperature data and convert to Freedom units and round.
        high = int(row[1])
        highs.append(high)

    #Pass data to matplot
    fig = plt.figure(dpi = 150, figsize = (10, 6))
    plt.plot(highs, c = 'red')

    #Format graphic
    plt.title("Daily high temperatures, July 2014, fotsize = 24")
    plt.xlabel('', fontsize = 16)
    plt.ylabel("Temperature(F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major',labelsize = 16)

    plt.show()
