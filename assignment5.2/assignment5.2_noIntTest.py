# Assignment 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Initialize variables

smallest = None # variable holds current smallest value
largest = None # variable holds current largest value
newNumber = 0 # variable holds new input for testing
intNewNumber = 0 # new input converted to integer
request = True

# Main program - build the list from user input

while request is True:
	newNumber = input('Give a number or "done": ')
	if newNumber == 'done':
		request = False
	else:
		try:
			intNewNumber = int(newNumber)
		except:
			print('''Invalid input''')
			continue
		if largest is None or intNewNumber > largest:
			largest = intNewNumber
		elif smallest is None or listValue < smallest:
			smallest = intNewNumber
		continue

# Output

print('Maximum is', largest)
print('Minimum is', smallest)
