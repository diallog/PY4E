#!/usr/bin/env python3

daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0

# For days in month, only output the days in summer and total them

for i in daysInMonth[5:8]:
    print (i)
    total = total + i
print ("The total number of days in summer are {days}".format (days = total))
