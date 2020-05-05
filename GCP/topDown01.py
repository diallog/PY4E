#!/usr/bin/env python3

# initialize variables
dataFile = None

############ read data ############
# open file

dataFile = input("Please provide the name of the data file: ")
with open(dataFile, 'r') as weatherData:
    for line in weatherData:
        print(line)
weatherData.close()
# read file contents
# close file


############ analyze data ############


############ report results ############
