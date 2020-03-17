#Remove nth occurance of the given word

def removenthOccurance(lis,n,word):
    newList  = []
    count = 0

    for i in lis:
        if i == word:
            count = count + 1
            if count != n:
                newList.append(i)
        else:
            newList.append(i)
    
    lis = newList

    if count == 0:
        print("Item not found")
    else:
        print("Updated list",lis)
    
    return newList

list = ['geeks','for','geeks']
n = 2
word = 'geeks'
removenthOccurance(list,n,word)