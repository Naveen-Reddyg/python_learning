# del keyword used to delete the object for garbage collection if we no need to use

x = 10
print(x)
del x
#print(x)   # gives error

s = 'naveen'
#del s[1]   # wont support item in string

#but it support delete entire s

del s
print(s) # give error


#NOne
# if you want to delet the object but not variable then we can use None

n = "kumar"
n = None
print(n)