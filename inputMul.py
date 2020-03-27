#read multiple values from keyboard

a,b=[int(x) for x in input("enter two numbers:").split()]
print("the sum of {} and {} is ".format(a,b),a+b)