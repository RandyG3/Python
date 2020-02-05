# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# product([1, 2, 3]) => 6
# product([4, 5, 6, 7]) => 840
# product([10]) => 10


def product(list_nums):
    total = 1
    for num in list_nums:
        total = total * num
    return total


print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))