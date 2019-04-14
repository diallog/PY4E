# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# open file
fName = input('Give a file in the current working directory: ')

try:
	fHandle = open(fName)
except:
	print('File not found. Please check file path/name and try again.')
	exit()

# intialize counter and total
numOfLines = 0
totConfidence = 0

# start parsing for interesting lines
for eaLine in fHandle:
	if not eaLine.startswith('X-DSPAM-Confidence:'): continue
	numOfLines = numOfLines + 1
	label, confInterval = eaLine.rsplit()
	print(confInterval)

# print the total number of identified noLines
# print('The total number of identified lines is: ',noLines)
print('Average spam confidence: ',numOfLines)
