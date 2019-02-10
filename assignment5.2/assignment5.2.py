# Assignment 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Initialize variables

smallest = None # variable holds current smallest value
largest = None # variable holds current largest value
newNumber = 0 # variable holds new input for testing
floatNewNumber = 0.0 # new input converted to float
intNewNumber = 0 # new input converted to integer
isIntegerResult = 0 # receives return value from isInteger()
numbersToTest = list() # list created by user input
request = True

# Define function(s)

def isInteger(possibleInt):
	# tests to see if user-provided input is an integer
	maybeEven = 2 * possibleInt
	if (maybeEven % 2) > 0:
		# maybeEven is not an integer; user needs to provide new value
		# print(maybeEven,'- You did not provide a whole-number. Please try again.')
		return 0
	else:
		# maybeEven is an integer and program execution can proceed
		# print(maybeEven, '- Congratulations! You provided a whole number.') # temporary statement
		return 1

# Main program - build the list from user input

while request is True:
	newNumber = input('Give a number or "done": ')
	if newNumber == 'done':
		request = False
	else:
		try:
			floatNewNumber = float(newNumber)
		except:
			print('''Invalid input''')
			continue
		# test to see if floatNewNumber is an integer
		isIntegerResult = isInteger(floatNewNumber)
		if isIntegerResult == 1:
			intNewNumber = int(floatNewNumber)
			numbersToTest.append(intNewNumber)
		else:
			# user did not provide an integer; they need to provide a new value
			continue

# Output

# Print Maximum
for listValue in numbersToTest:
    if largest is None or listValue > largest:
        largest = listValue
print('Maximum is', largest)

# Print Minimum
for listValue in numbersToTest:
    if smallest is None or listValue < smallest:
        smallest = listValue
print('Minimum is', smallest)
