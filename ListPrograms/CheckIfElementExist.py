# find the element in a list
def elementInList(lis,n):
    for i in lis:
        if i == n:
            print("Element exists in list")
    

list = [1,2,4,5,6,7]
n = 2
elementInList(list,n)

# Second way
if n in list:
    print("Element exists")