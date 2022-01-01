#Find the smallest number in an array

def smallestNum(arr,n):

    small = arr[0]
    for i in range(1, n):
        if arr[i] < small:
            small = arr[i]
    return small

arr = [1,3,4,2,54,-3]
n = len(arr)
ans = smallestNum(arr,n)

print("smallest number of array {0} is {1}".format(arr,ans))