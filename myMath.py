PI = 3.141592653589793


def factorial(number):
    if number in [0, 1]:
        return 1
    else:
        return number * factorial(number - 1)


def permutation(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

def combination(n,r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n-r))


if __name__ == '__main__':
    print(factorial(5))
    print(permutation(4, 4))
    import math

    print(math.perm(4, 4))
    print(combination(4,2))
