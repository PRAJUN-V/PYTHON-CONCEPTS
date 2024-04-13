import operator
from itertools import accumulate

a = [1,2,3,4,5,8]
print(list(accumulate(a)))

print(list(accumulate(a, operator.mul)))
print(list(accumulate(a, operator.sub)))

