# generalize the following code into a function that accepts the string and the target letter from user input
"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""

# Define function
def myCount(usrInput1,usrInput2):
	count = 0
	for letter in usrInput1:
		if letter == usrInput2:
			count = count + 1
	print(count)

# Get user input
mainInput1 = input('Give me a string (word, sentence..somthing): ')
mainInput2 = input('Give me a letter to search for: ')

myCount(mainInput1,mainInput2)
