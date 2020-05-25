#!/usr/bin/env python3

# Some basic file manipulation trying alternate 'open' method.

import os
os.system('clear')

# with open ('00_test.txt', 'r') as inputForPlay:
	# read the file and output to a list
	# theFile = inputForPlay.read()

fileList = theFile.split()
print("The original list is: \n", fileList, "\n")

# sort() method sorts the list in place
fileList.sort()
print("The sorted list is: \n", fileList, "\n")

'''
**Notes for ongoing work**
In order to get the sorted list sorted (the way I want it sorted), going to have
to process fileList to be all lower case. Would be interesting to "remember" all
of the items that were originally capitalized in the list.
'''
