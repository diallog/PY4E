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

# Initialize variables

smallest = None # variable holds current smallest value
largest = None # variable holds current largest value
newNumber = 0 # variable holds new input for testing
request = True

# Obtain input from user and test values
print('''
===========================================================================
| The objective of this program will be gathering numeric input from the  |
| user and returning the largest and smallest value. The input should     |
| be limited to integer numbers, i.e. whole-numbers. When the user has    |
| no more input, they can finish by typing 'done'.                        |
===========================================================================
''')

while request is True:
	newNumber = input('Give another number or "done": ')
	if newNumber = 'done':
		request = False
		break # this may go in a different place
	else:
		try:
			newNumber = float(newNumber)
		except:
			print('''
			The user-provided input should be a whole-number. Please
			try again.
			''')
			continue
		# test to see if newNumber is an integer
		isInteger(newNumber)

# Temporary end of program execution
