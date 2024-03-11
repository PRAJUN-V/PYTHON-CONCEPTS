# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib (n - 2)
#
# for i in range(1,1001):
#     print(i,':',fib(i))


from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib (n - 2)

for i in range(1,1001):
    print(i,':',fib(i))


