# Find the factorial of numbers

num = int(input("Enter number"))

def factorial(n):
    return 1 if (n ==0 or n ==1) else n * factorial(n - 1)


fact = factorial(num)
print("the factorial of {0} is {1} ".format(num,fact))