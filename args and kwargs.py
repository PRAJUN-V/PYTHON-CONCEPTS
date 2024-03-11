# args
# def sum(*nums): # number is
#     sum = 0
#     for i in nums:
#         sum += i
#
#     return sum
#
# print(sum(2,45))


# kwargs
def person_info(**kwargs):
    print(kwargs)
person_info(name = 'hari',age = 20)
person_info(name = 'Rahul',age = 21,sub = 'cs')


def fun(var1,*var2,**var3):  # we should only pass in this order only if we are passing all type of
    pass                     # variable else error will strike eg:def fun(**var3,*var2,var1)
