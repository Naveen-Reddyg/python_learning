from sys import argv
print("The number of values in argv:",len(argv))
print("the list of command line arguments",argv)
print("command line arguments one by one")
for x in argv:
    print(x)
print("slice operator example",argv[1:3])
