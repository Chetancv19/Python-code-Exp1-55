#Chetan Velonde 3019155
#Python Program to Find the Sum of Natural Numbers

i = int(input("Enter the value of integer till which the sum needs to be found:"))
print("The sum of all the numbers till the specified value is: ")
sum = 0
for x in range(1, i + 1):
    sum = sum + x
print(sum)