'''The purpose of this script will be to open a file, copy its content
and write that output to another file'''

# Open the original file for reading
try:
	orginalFile = open('./romeo.txt', 'r')
except:
	print('Something bad happened. The requested file probably does not exist.')

# Open the output file for writing
try:
	outputFile = open('./copyOfOriginal.txt', 'w')
except:
	print('Something bad happened. The requested file probably does not exist.')

# Copy the contents of the orginal file
# Write the original contents to the output files
# Close all the files
orginalFile.close()
outputFile.close()
