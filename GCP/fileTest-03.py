#!/usr/bin/env python3

'''This script will read input from MyDataFile.txt and write the output (a copy of the original file) to results.txt'''

# Open the original file for reading
try:
	originalFile = open('./MyDataFile.txt', 'r')
except:
	print('Something bad happened. The requested file probably does not exist.')

# Open the output file for reading and writing
try:
	outputFile = open('./results.txt', 'r+')
except:
	print('Something bad happened. The requested file probably does not exist.')

# write the original file to the new files

for i in originalFile:
	outputFile.writelines(i)

# Close all the files
originalFile.close()
outputFile.close()
