#!/usr/bin/env python3

# input name and age for multiple people until entering 'stop'
# then report who is the oldest person
# use lists for this exercise

# initialize variables

newName = None
newAge = 0

# get input
newName = input ("What is the person's name?")
try:
    if type(newName) == str:
        newName.lower()
except:
    print ("Expected to get a name. This doesn't look like a name.")
	
print ("The name just received is: "{newName}.format(newName=newName))
