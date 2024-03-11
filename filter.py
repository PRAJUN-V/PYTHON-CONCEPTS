# https://youtu.be/kj850Y8y8FI?si=F62b9ztW4UEv5lzj

list1 = [1,3,2,3,5,6,7,8,4,6,78,34,23,57]

def num(n):
    if n%2 == 1:
        return True
a = set(filter(num,list1))

#
# a = set(filter(lambda n : n%2==0,list1))
# print(a)

