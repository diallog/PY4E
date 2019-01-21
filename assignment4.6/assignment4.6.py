# Assignment 4.6 Write a program to prompt the user for hours and payRate per hour using input to compute gross pay. Pay should be the normal payRate for hours up to 40 and time-and-a-half for the hourly payRate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a payRate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

# Initialize global variables
overtimeRate = 1.5 # multiuplier for overtime hours
otThreshold = 40.0
otHrs = 0.0
hrs = 0.0
payRate = 0.0

# Define functions
def computePay(oHrs,oRate):
	oPay = (otThreshold * oRate) + (oHrs * oRate * overtimeRate)
	return oPay

# Obtain how many hours the user worked
hrs = input("Please enter how many hours worked for current period (hr): ")

# Obtain the employees payRate
payRate = input("Please enter your current Rate of Pay ($/hr): ")

# convert input strings to float values
try:
	hrs = float(hrs)
except:
	print("Floating point conversion failed for Hours Worked.")
try:
	payRate = float(payRate)
except:
	print("Floating point conversion failed for Rate of Pay.")

# Calculate wages
if hrs <= otThreshold:
	wages = hrs * payRate
else:
	otHrs = hrs - otThreshold
	wages = computePay(otHrs,payRate)

# Output
# print("The wages for the current period are: ",wages)
print(wages)
