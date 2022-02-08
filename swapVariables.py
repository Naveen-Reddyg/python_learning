# Python program to swap two variables

val1 = int(input("Enter a number "))
val2 = int(input("Enter a number "))

temp = val1
val1 = val2
val2 = temp

print("The values of val1 after swapping: {0}".format(val1))
print("The vale of val2 after swapping: {0}".format(val2))

