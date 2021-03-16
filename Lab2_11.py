#Chetan Velonde 3019155
#Python Program to Find Armstrong Number in an Interval
print("For the Armstrong number series:")
a = int(input("Enter the start of the interval:"))
b = int(input("Enter the end of the interval:"))

for x in range(a, b + 1):

    order = len(str(x))
    sum = 0

    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if x == sum:
        print(x)