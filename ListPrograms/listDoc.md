# List

List is the collection of similar or different types of data. we use square brackets to store data as list and python lists are mutable that means
we can change the values in the list. 
suppose we want to store a group of numbers in list we can store lie
    e.g:    [1,2,3,4]
    we can use list to store different data type values as well like
    e.g: ["naveen",3,4,4.5]

we can create a list like below
1) num = [1,2,3]

## Access values from list:

    we can access the elements of a list by using the index from the list. index is basically location where the
    elements store
    e.g: to access the number 3 from the above variable num is n[2] here we are using index 2 because in list
    the index numbers starts from 0 and increments by 1 from left to right.
        We can even access data from right to left as well by using the negative index where the index will starts
    from -1. We can get the result 3 by using num[-1]

## Slicing of python list:

    We can get the group of values by slicing the list, and also we can get the group of words by slicing the list like below

    suppose we have a list with couple of letters

    str = ['h','e','l','l','o','w','o','r','l','d']

    we can get the first 5 letters from the above list by using the str[0:4]  ===> ['h','e','l','l','o']
    and we can also use the negative index i.e we can get the values from the right side.

## Adding element to the list:
    python provides different methods to add the elements to the list, where we can use this by add elements to the list
    
    append()
        by using the append() method we can add the element at the end of the list
        e.g:  test = [1,2,3,4]
            
        we can add the number 5 to the list by using the append method like
                test.append(5)
        
        output: [1,2,3,4,5]
    
    extend()
        By using the extend() method we can add all the elements of one list to another
        But the elements will be added at the end of initial list
        e.g: even_numbers = [2,4,6,8]
             odd_numbers = [1,3,5,7]
             whole_numbers = even_number.extend(odd_numbers)
        output:
            [2,4,6,8,1,3,5,7]


## Changing the Values in the list

As we know python lists are mutable so we can change the values of the list by using the index and replace with other items.

e.g: fruits = ['apple','banana','grapes']

here we want to replace the banana fruit with melon like below
    fruits[1] = 'melon'

finally when we print the fruits we get the below values
    output: fruits = ['apple','melon','grapes']


## Removing an element from the list

we have different methods available to delete the values from the list. 
    
    del()
    By using the del() method we can delete one or more elements from the list. 
    e.g: fruits = ['apple','banana','grapes']
        to delete the banana fruit we can use the index like below
        del fruits[1]
        the result of the above statement gives the belo list
        ['apple','grapes']
    
        We can also delete the multiple elements from the list
    e.g: fruits = ['apple','banana','grapes','berries']
        del fruits[2:3]
        the result list will be ['apple','banana']

    
    remove()
    Unline the del() method where we delete the element from the list by using the index, here we use the actual element to 
    delete from the list.
    e.g: fruits = ['apple','banana','grapes']
        fruits.remove('banana')
    the result list will be ==> ['apple','grapes']
    