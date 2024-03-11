import time

#2^n complexity which means as input increase time complexity increase by double
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# for i in range(1,36):
#     start = time.time()
#     fib(i)
#     end = time.time()
#     print(end-start)


from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

result = fib(40)
print(result)

