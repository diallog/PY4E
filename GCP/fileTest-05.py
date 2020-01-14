#!/usr/bin/env python3

# Some basic file manipulation trying alternate 'open' method.

with open ('00_test.txt', 'r') as inputForPlay:
	#read the file and output to a list
	theFile = inputForPlay.read()
	# print(list(theFile))
	splitFile = theFile.split()
	print(sorted(splitFile))
