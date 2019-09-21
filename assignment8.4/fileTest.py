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
# Show that the two files are the same
print("This is the orginal file:")
for i in orginalFile: print(i.rstrip())
print("\n\n")
print("And here is the copy of the orginal:")
for i in outputFile: print(i.rstrip())
print("\n\n")

# Close all the files
orginalFile.close()
outputFile.close()
