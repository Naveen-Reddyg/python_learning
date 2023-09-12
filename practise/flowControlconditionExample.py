# Flow control decided at run time such as if else
# 3 types

#     1)conditional statement/selection statements
# if
# if-else
# if-elif-else
# switch not available

#Example 1
name = input("Enter name:")
if name == "naveen":
    print("Hello {} Good morning good to see you".format(name))
else:
    print("Hello {} Good Morning".format(name))
print("How are you")

#Example 2
brand = input("Enter your brand:")
if brand == "RC":
    print("It is children brand")
elif brand == "RM":
    print("It is not that much good")
elif brand == "sh":
    print(" buy one get one")
else:
    print("not available")


