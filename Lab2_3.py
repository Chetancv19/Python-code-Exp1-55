#Python Program to Check if a Number is Odd or Even
#chetan velonde 3019155

a = int(input("Enter the year for check:"))
if (a % 4) == 0:
    print(str(a) + " is a leap year.")
else:
    print(str(a) + " is not a leap year.")