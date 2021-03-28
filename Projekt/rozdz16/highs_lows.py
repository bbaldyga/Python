import csv
from os import read
from matplotlib import pyplot as plt
from datetime import datetime
# Get dates and high temperatures from file.
filename = 'sitka_weather_2018_simple.csv'
#Get dates,lows and highs temperatures from station
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)
        low = int(row[6])
        lows.append(low)
        high = int(row[5])
        highs.append(high)
    print(highs)
    for index, column_header in enumerate(header_row): 
        print(index, column_header)

    #Plot data
    fig = plt.figure(dpi=128,figsize=(10,6))
    
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    #format plot
    plt.title("Daily high and low temperatures 2018",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()
    #362