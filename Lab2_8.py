#Chetan Velonde 3019155
#Python Program to Display the multiplication Table
i = int(input("Enter the integral value to get its multiplication table:"))
for x in range(1, 11):
    print(str(i) + "*" + str(x) + " = " + str(i*x))