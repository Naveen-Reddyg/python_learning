#library example

import math
print(math.sqrt(9))

# same as above code(aliasing)

import math as m
print(m.sqrt(9))

#same as above

from math import sqrt
from math import pi

print(sqrt(9))

# also works

from math import *  # not advised to use
print(sqrt(9))


# sqrt()
# ceil()
# floor()
# pow(x,y)
# factorial()
# gcd()
# sin()
# cos()
# ......

# pi = 3.12
# e = 2.71
# inf = infinity
#nan = not a number
