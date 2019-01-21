# Assignment 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Define function for integer test

def isInteger(x):
	even = 2 * x
	if (even % 2) > 0:
		# x is not an integer and the user must provide a different input value, i.e. input must be an integer
		print(even) # temporary statement
	else:
		# x is an integer and program execution can proceed
		print(even) # temporary statement
