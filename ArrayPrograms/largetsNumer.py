#Find the largest number from the array

def largest(arr,n):

    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1,5,2,3,4]
n = len(arr)
ans = largest(arr,n)
print(ans)