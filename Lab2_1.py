#1.Python Program to Check if a Number is Positive, Negative or 0
#chetan velonde 3019155
a = int(input("Enter the number for check:"))
if a > 0:
    print(str(a) + " is positive and lies on right hand side on the number line")
elif a < 0:
    print(str(a) + " is negative and lies on left hand side on the number line")
else:
    print(str(a) + " is equal to zero position in a number line")