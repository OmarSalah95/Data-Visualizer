import csv

from datetime import datetime
from matplotlib import pyplot as plt


#Stores file location for csv module
filename = 'sitka_weather_2014.csv'

#Pull and store dates, high, and low temps to respective arrays
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        #Strip, format, and store dates.
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        #Strips and stores high temps.
        high = int(row[1])
        highs.append(high)

        #Strips and stores lows.
        low = int(row[3])
        lows.append(low)

    #Pass and plot data
    fig = plt.figure(dpi = 150, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha  = 0.5)
    plt.plot(dates, lows, c = 'blue', alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

    #Format graphic
    plt.title("Daily high and low temperatures - 2014", fontsize = 24)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major',labelsize = 16)

    plt.show()
