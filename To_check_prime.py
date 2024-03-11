# # To check a number is prime
#
# # Done by myself
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2 or num ==3:
#         return True
#     else:
#         flag = 1
#         for i in range(2,num):
#             if num % i == 0:
#                 flag = 0
#                 break
#             else:
#                 flag = 1
#         if flag == 0:
#             return False
#         else:
#             return  True

# prime = list(filter(is_prime,range(80000,89217)))
# print(prime)
# print(len(prime))

# print(is_prime(170141183460469231731687303715884105727))
#
# a = [x for x in range(1,100) if is_prime(x)]  # using list comprehension
# print(a)


def is_prime(num):
    try:
        if num <= 1:
            return False
        elif num == 2 or num == 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w  # Switch between 2 and 4 (2, 4, 2, 4, ...)
        return True
    except KeyboardInterrupt:
        print(i)

print(is_prime(170141183460469231731687303715884105727))



