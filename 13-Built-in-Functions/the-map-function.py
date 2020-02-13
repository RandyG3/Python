# As far as I can tell if you want to pull elements from the list and print a new list
# using those elements you use filter. Whereas map you can pull elements and carry out
# an operation on them and then print a new list with the results of the operation.
#
# From Boris
# That's basically it. filter to filter down the original list, map to return a new list
# of the same size.
numbers = [4, 8, 15, 16, 23, 42]
cubes = [number ** 3 for number in numbers]
print(cubes)


def cube(number):
    return number ** 3

#         func, iterable that func will operate on : returns same size list


print(map(cube, numbers))  # returns the object in memory
print(list(map(cube, numbers)))


animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(map(len, animals))
print(list(map(len, animals)))
