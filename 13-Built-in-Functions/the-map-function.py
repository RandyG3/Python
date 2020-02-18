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
