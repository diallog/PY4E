#!/usr/bin/env python3

# initialize variables
dataFile = None
weatherList = []

############ read data ############
# open file

dataFile = input("Please provide the name of the data file: ")
with open(dataFile, 'r') as weatherData:
    for line in weatherData:
        date, hiTemp, loTemp, rainFall = line.split(',')
        month, day, year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
        hiTemp = int(hiTemp)
        loTemp = int(loTemp)
        rainFall = float(rainFall)
        weatherList.append([year, month, day, loTemp, hiTemp, rainFall])

############ analyze data ############
# get user input

userDay = int(input("What day do you want to search for? (enter as one or two "
              "digit number, e.g. 5 or 12): "))
userMonth = int(input("What month do you want to search for? (enter as one or two "
                "digit number, e.g. 5 or 12): "))



############ report results ############
