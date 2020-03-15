# find the largest of three numbers
 
num1 = float(input("Enter a number"))
num2 = float(input("Enter a number"))
num3 = float(input("Enter a number"))

if num1 > num2 and num1 > num3:
    largerNumber = num1

elif num2 > num3 and num2 > num1:
    largerNumber = num2

else:
    largerNumber = num3

print("THe largest number is ",largerNumber)
