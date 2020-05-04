#!/usr/bin/env python3

# do calculations based on a list containing days in a month

i = 0
daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
daysInYear = 0

for i in range(len(daysInMonth)):
	print (daysInMonth[i])
	daysInYear = daysInYear + daysInMonth[i]
	
print ("The number of days in a year are {total}".format(total = daysInYear))
