import math as mt
from math import *
import numpy
i=2
print("Its mathematics {0} ".format(pi,i))
print("Its math Pi Function {:.4}".format(mt.pi))
s = "dadad"
print(s[0:])
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

list = [1, 2, 4, 5]
#  Numpy behaves differently
#   x = list + 3
# TypeError: can only concatenate list (not "int") to list
# but
print(rolls + 2)
# numpy lists are different you can add integer to lists

