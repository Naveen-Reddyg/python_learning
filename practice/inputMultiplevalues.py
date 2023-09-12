#read two float valiues from the keyboard which are specified with , separation and print sum

x,y = [float(x) for x in input("enter 2 values:").split(",")]
print("the mul of {} and {} is".format(x,y),x*y)