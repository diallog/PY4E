# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

fName = input('Give a file in the current working directory: ')

try:
	fHandle = open(fName)
except:
	print('File not found. Please check file path/name and try again.')
	exit()

for eaLine in fHandle:
	print(eaLine)
