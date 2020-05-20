#!/usr/bin/env python3

# PURPOSE: studying function side effects

import os
os.system('clear')

orgList = [5, 3, 2, 1, 4]

def sumList(myList):
    for i in range(1, len(myList)):
        myList[i] += myList[i-1]
    return myList[len(myList)-1]

print(sumList(orgList))
print(orgList)
