#Chetan Velonde 3019155
#Python Program to Print the Fibonacci sequence

i = int(input("Enter the number of terms for fibonacci series:"))
sum = 0
num = 1
sum1 = 0
print("The fibonacci series is:\n")
for x in range(1, i+1):
    print(sum)
    sum1 = sum + num
    sum = num
    num = sum1