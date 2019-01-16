# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# initialize constants
studentScore = 0.0
gradeA = 0.9
gradeB = 0.8
gradeC = 0.7
gradeD = 0.6

# get input from student

studentScore = input("Please enter our score as a decimal number between 0.0 and 1.0, e.g. if your score is 90, please enter it as 0.9.: ")

#convert input string to a float
try:
	studentScore = float(studentScore)
except:
	print("The score provided does not represent a numerical value. Please re-run the program and modify your input so that it complies with the reuqirements: a decimal number between 0.0 and 1.0, e.g. if your score is 90, please enter it as 0.9.")
	quit()

if studentScore >= gradeA:
	print("A")
elif studentScore >= gradeB:
	print("B")
elif studentScore >= gradeC:
	print("C")
elif studentScore >= gradeD:
	print("D")
else:
	print("F")

# end run
