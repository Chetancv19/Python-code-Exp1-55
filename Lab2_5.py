#Python Program to Check Prime Number
#chetan velonde 3019155

a = int(input("Enter the number for checking whether it is prime or not:"))
if a > 1:
    for x in range(2, a):
        if a % x == 0:
            print(str(a) + " is not a prime number.")
            break
    else:
        print(str(a) + " is a prime number.")

#main princple - every number has it two factors, 1 and the number itself-->then divisibilty test
#we initialize the code by checking the value of the input integer... then use range() for checking the divisibility of that
#input number
#if all the test cases are passed for divisibility check from 2 to the input integer, the number is declared as not a prime number