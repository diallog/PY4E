# Assignment 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Initialize variables

smallest = None # variable holds current smallest value
largest = None # variable holds current largest value
newNumber = 0 # variable holds new input for testing
floatNewNumber = 0.0 # new input converted to float
intNewNumber = 0 # new input converted to integer
isIntegerResult = 0 # receives return value from isInteger()
request = True

# Define function(s)

def isInteger(possibleInt):
	# tests to see if user-provided input is an integer
	maybeEven = 2 * possibleInt
	if (maybeEven % 2) > 0:
		# x is not an integer and the user must provide a different input value, i.e. input must be an integer
		# print(maybeEven,'- You did not provide a whole-number.') # temporary statement
		return 0
	else:
		# x is an integer and program execution can proceed
		# print(maybeEven, '- Congratulations! You provided a whole number.') # temporary statement
		return 1


# def valueCompare(value):
	# modifies stored values of smallest and largest based upon comparison
	# if value < smallest:
		# smallest = value
	# elif value > largest:
		# largest = value

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
	newNumber = input('Give a number or "done": ')
	if newNumber == 'done':
		request = False
		break # this may go in a different place
	else:
		try:
			floatNewNumber = float(newNumber)
		except:
			print('''The user-provided input should be a whole-number. Please try again.''') - this was my original version
			# print('Invalid input') # this is the version required for credit (to match output in the auto grader)
			continue
		# test to see if floatNewNumber is an integer
		isIntegerResult = isInteger(floatNewNumber)
		if isIntegerResult == 1:
			intNewNumber = int(floatNewNumber)
			if (smallest or largest) is None:
				smallest = intNewNumber
				largest = intNewNumber
			else:
				# valueCompare(intNewNumber) - this function needs correction before it can be used
				if intNewNumber < smallest:
					smallest = intNewNumber
				elif intNewNumber > largest:
					largest = intNewNumber
		else:
			continue

print('Maximum is',largest)
print('Minimum is',smallest)
