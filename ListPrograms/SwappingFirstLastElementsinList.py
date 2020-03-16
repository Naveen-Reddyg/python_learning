#Swap the elements in the list first and last

def SwapFirstLastElement(arr):

    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp

    return arr

arr = [1,2,3,4,5]
ans = SwapFirstLastElement(arr)

print("after swapping from the list",ans)