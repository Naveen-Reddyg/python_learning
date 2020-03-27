# read group of command line arguments and sum of these values
from sys import argv
args = argv[1:]
sum = 0
for x in args:
    n = int(x)
    sum += n

print("The sum of argv is:",sum)