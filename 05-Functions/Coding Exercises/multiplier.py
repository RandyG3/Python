# Define a multiplier function that accepts three integers as arguments.
# Return the product of the arguments. The product is the total when
#   values are multiplied together.
# If the user does not provide any arguments, all three parameters
#   should have default arguments of 1.


def multiplier(a=1, b=1, c=1):
    return a * b * c


print(multiplier(2, 3, 4))
print(multiplier())
