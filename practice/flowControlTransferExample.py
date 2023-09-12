#     3) Transfer statement
# break
# continue
# pass
#break examples
# we can use else with for loop in break
i = 0
while True:
    print("Hello")
    i += 1
    if i == 5:
        break

#example2
cart = [12,30,50,302,500,900]
for i in cart:
    if i > 500:
        break;
    print(i)
else:
    print("Congrts all processed")


#Continue examples

for i in range(10):
    if i%2 == 0:
        continue
    print(i)

#example2
cart = [12,30,50,302,500,900]
for i in cart:
    if i >= 500:
        print("Sorry we cant process this item",i)
        continue
    print(i)


#pass statement examples
# it is a keyword in python
# it is a empty stmt
# it won't do anything

if True:
    pass
else:
    print("Hello")

#example 2
def f1():
    print("Hello")
def f2():
    pass

f1()

#example 3
for i in range(100):
    if i % 10 == 0:
        print(i)
    else:
        pass