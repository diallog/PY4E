# This assignment will obtain two pieces of data from the user and perform a calculation.

# This script begins with a hint from the course...but lets do a little over-achievement.

print("Alright, let's do our first calculation in Python using information obtained from the user.\r")

# This first line is provided for you

hrs = input("Please enter the number of hours worked: ")
# hrs = float(hrs)
rate = input("Thank you. Now enter the rate ($/hr): ")
# rate = float(rate)

# calculation...
pay = float(hrs) * float(rate)

# output
# print("Pay: " + str(pay))
# alternative approach
print("Pay:", pay)
