# https://youtu.be/kj850Y8y8FI?si=F62b9ztW4UEv5lzj

from functools import reduce
# num = int(input('Enter the number to find factorial:'))

list1 = [1,3,2,7]
# for i in range(1,num+1):
#     list1.append(i)
a = reduce(lambda a,b : a*b,list1)
print(a)

