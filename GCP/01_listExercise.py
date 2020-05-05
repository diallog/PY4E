#!/usr/bin/env python3

# input name and age for multiple people until entering 'stop'
# then report who is the oldest person
# use lists for this exercise

# initialize variables
listIndex = 0
nameList = []
ageList = []
newName = None
newAge = 0

newName = input ("What is the person's name? (enter 'stop' to quit collecting names.) ")
newName = newName.lower()
while newName != 'stop':
	nameList.append(newName)
	
	newAge = input ("How old is {newName}? ".format(newName = newName.capitalize()))
	newAge = int(newAge)
	ageList.append(newAge)
	
	print ("Thank you. Name and age recorded for {newName}.".format(newName = newName.capitalize()))
	newName = input ("What is the person's name? (enter 'stop' to quit collecting names.) ")
	newName = newName.lower()

print (nameList)
print (ageList)
