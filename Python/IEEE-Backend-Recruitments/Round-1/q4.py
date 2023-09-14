from math import gcd
from functools import reduce
print(reduce(gcd, map(int, input().split())))
