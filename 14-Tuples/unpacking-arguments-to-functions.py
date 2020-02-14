def product(a, b):
    return a * b


print(product(3, 5))

numbers = [3, 4]  # a, b
numbers = (3, 4)  # a, b

print(product(*numbers))