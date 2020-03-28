# Output values
# using sep operator(sep ===> space by deafult)
a,b,c = 10,20,30
print(a,b,c,sep=" < ", end=" ")
print(40,50,60,sep="-")

# using end operator (instead of printing in the next line we can use end)
# (end ===> default new line)
print("Hello World",end=" ")
print("python")

# print(object)

l = [10,20,30,40]
t = (10,20,30,40)
s = {10,20,30,40}
print(l,t,s)

#print (formatted string)
# %i == int type
# %d == int type
# %f == float type
# %s == Str type
# print("formatted string",%(variable list))

m,n,o = 10,20,30
print("m value is %i" %m)
print("n value %i and o value is %d" %(n,o))

# print() function with replacement operator
# {} ==> replacement operator

name = "Naveen"
salary = 85000
city = "Hyd"
print("Hello {0} your salary is {1} "
      "and your city is {2}".format(name,salary,city))
print("Hello {} your salary is {} "
      "and your city is {}".format(name,salary,city))
print("Hello {x} your salary is {z} "
      "and your city is {y}".format(x=name,z=salary,y =city))