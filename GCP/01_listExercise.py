#!/usr/bin/env python3

# obtain name and age data for multiple people until entering 'stop'
# then report who is the oldest person
# use lists for this exercise

import os
os.system('clear')

# initialize variables
nameList = []
ageList = []
newName = None
newAge = 0
maxAge = 0
maxIndex = 0

# get input
newName = input ("What is the person's name? (enter 'stop' to quit collecting names.) ")
newName = newName.lower()
while newName != 'stop':
	nameList.append(newName)

	newAge = input ("How old is {newName}? ".format(newName = newName.capitalize()))
	newAge = int(newAge)
	ageList.append(newAge)

	print ("Thank you. Name and age recorded for {newName}.".format(newName = newName.capitalize()))
	print ("\n")
	newName = input ("What is the person's name? (enter 'stop' to quit collecting names.) ")
	newName = newName.lower()

# process data
maxAge = max(ageList)
maxIndex = ageList.index(maxAge)

# report results
print ("\n")
print ("{oldest} is the oldest person with an age of {age}."
	   .format(oldest = nameList[maxIndex].capitalize(), age = ageList[maxIndex]))
