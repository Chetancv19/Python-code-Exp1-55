#4) Python Program to Find the Largest Among Three Numbers *
#chetan velonde 3019155

a = int(input("Enter the first number for check:"))
b = int(input("Enter the second number for check:"))
c = int(input("Enter the third number for check:"))
if (a > b)&(a > c):
    print(str(a) + " is the largest among all the given number.")
elif (b > a)&(b > c):
    print(str(b) + " is the largest among all the given number.")
else:
    print(str(c) + " is the largest among all the given number.")