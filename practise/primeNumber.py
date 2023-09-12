#FInd the number prime number

num = int(input("Enter number"))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(" number is not prime")
            break
    else:
        print("The number is prime number")

else:
    print("Num is not prime number")

