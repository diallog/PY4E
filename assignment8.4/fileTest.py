'''The purpose of this script will be to open a file, copy its content
and write that output to another file'''

# Open the original file for reading
try:
	originalFile = open('./romeo.txt', 'r')
except:
	print('Something bad happened. The requested file probably does not exist.')

# Open the output file for reading and writing
try:
	outputFile = open('./copyOfOriginal.txt', 'r+')
except:
	print('Something bad happened. The requested file probably does not exist.')

# Print the empty output files
print('And here is the empty output file:')
for i in outputFile: print(i.rstrip())
print('\n\n')

# Show the original file
print('This is the original file:')
for i in originalFile: print(i.rstrip())
print('\n\n')

# Write the original contents to the output file
for i in originalFile:
	print(i.rstrip())
	outputFile.write(i.rstrip())

# Show the output file after copying
print('And here is the copy of the orginal:')
for i in outputFile: print(i.rstrip())
print('\n\n')

# Close all the files
originalFile.close()
outputFile.close()
