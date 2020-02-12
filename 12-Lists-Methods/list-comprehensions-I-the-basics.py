numbers = [3, 4, 5, 6, 7]
# create a new list with squares
#
# Traditional:
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)
#
# better way:
squares2 = [number ** 2 for number in numbers]  # will not preserve number variable
print(squares2)

rivers = ["Amazon", "Nile", "Yangtze"]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([expression.upper() for expression in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])
