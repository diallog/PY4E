#!/usr/bin/env python3

'''This is an exercise to write multiple lines to a file'''

# set some variables

volume = [23, 96]

# write strings to output

outputFile = open('./theVolumesAre.txt', 'a')

for i in range(2):
	outputFile.write('Volume' + str(i + 1) + ' is: ' + str(volume[i]) \n)

outputFile.close()
