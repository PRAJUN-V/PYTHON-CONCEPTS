# The walrus operator, represented by :=, is indeed a relatively recent
# addition to Python, introduced in Python 3.8. It is also known as the
# assignment expression. The primary purpose of the walrus operator is
# to simplify code by allowing you to assign a value to a variable as
# part of an expression.

# Without the walrus operator
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive:", number)
else:
    print("The number is non-positive:", number)


# With the walrus operator

if (number := int(input("Enter a number: ")))> 0:
    print("The number is positive:", number)
else:
    print("The number is non-positive:", number)

