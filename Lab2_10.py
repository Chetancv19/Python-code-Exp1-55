#Chetan Velonde 3019155
#Python Program to Check Armstrong Number

i = int(input("Enter a number for check of armstrong number:"))

sum = 0
temp = i
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if i == sum:
   print(str(i) + " is an Armstrong number")
else:
   print(str(i) + " is not an Armstrong number")