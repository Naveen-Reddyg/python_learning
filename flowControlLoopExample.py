#Flow control
# 2) Iterative Statement
# loops
#
# for loop
s = input("Enter a string")
count = 0
index = 0
for i in s:
    print("the index of {} is".format(i),end=" ")
    print(index)
    index += 1
    count += 1
print(count)

l =[10,20,30]
for x in l:
    print(x)

for y in range(1,10):
    print(y)

# while loop
# iteration know in advance then we should go for loop
# if we dont know then we can use while loop
# while condition:
#     body

# Example 1 print 1 to 10 numbers
x  = 1
while x<= 5:
    print(x)
    x+=1

#example 2

name =""
pwd = ""
while (name != 'naveen') and (pwd != 1234):
    name= input("enter name:")
    pwd = eval(input("enter password"))

print("Hello",name,"Good morning")

# Example 3 infinite loop
# i = 0
# while True:
#     print(i)
#     i+=1

#nested loops
#loop inside another loop

for i in range(4):
    for j in range(4):
        print(1,j)

#example
n = eval(input("enter number of rows:"))
for i in range(1,n+1): # i represents rows number
    for j in range(1,i+1): # j represents the number of *
        print("*",end= " ")
    print()