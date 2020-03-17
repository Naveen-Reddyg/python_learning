# python the list length

def lengthOfList(lis):

    count = 0
    for i in lis:
        count = count +1
    
    return print(count)

list = ['a','b','c','d','e']
lengthOfList(list)

count2 = print(len(list))

#for performence wise len() is better than 