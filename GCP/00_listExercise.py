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

# get input
newName = input ("What is the person's name? (enter 'stop' to quit collecting names.)")
try:
    newName = newName.lower()
	while newName != 'stop':
		nameList[listIndex] = nameList.append(newName)
		
		newAge = input ("How old is {newName}? ".format(newName = newName.capitalize()))
		newAge = int(newAge)
		ageList[listIndex] = ageList.append(newAge)
		
		print ("Thank you. Name and age recorded for {newName}.".format(newName = newName))
		newName = input ("What is the person's name? (enter 'stop' to quit collecting names.)")
		newName = newName.lower()
except:
    print ("Something did not go right. Try again.")
	
print (nameList)
print (ageList)
	
