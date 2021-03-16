#Python Program to get Prime Number
#chetan velonde 3019155

a = int(input("Enter the number for start:"))
b = int(input("Enter the number for end:"))
for x in range(a, b+1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x)

#main princple - every number has it two factors, 1 and the number itself-->then divisibilty test
#we initialize the code by checking the value of the input integer... then use range() for checking the divisibility of that
#input number
#if all the test cases are passed for divisibility check from 2 to the input integer, the number is declared as not a prime number