from ast import operator
from audioop import mul
from itertools import *
import operator
a=[2,3,7]
b=[4,5,7,6,9,8]
print(list(product(a,b)))
print(list(permutations(a)))
print(list(combinations(a,3)))
print(list(accumulate(b)))
print(list(accumulate(b,func=operator.mul)))
print(list(accumulate(b,func=max)))