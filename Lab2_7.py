#Chetan Velonde 3019155
#Python Program to Find the Factorial of a Number

i = int(input("Please enter the value of the number whose factorial value need to be found:"))
fact = 1
if i == 0:
    print("Value of factorial of zero is 1")
if i < 0:
    print("Factorial does not exist")
if i > 0:
    for x in range(1, i+1):
        fact = fact*x
    print("Value of factorial of " + str(i) + " is " + str(fact))