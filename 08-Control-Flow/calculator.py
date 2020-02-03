def calculator(operation, a, b):
    if operation == 'a':
        return a + b
    elif operation == 's':
        return a - b
    elif operation == 'd':
        return a / b
    elif operation == 'm':
        return a * b
    else:
        return "Unknown operation"


print(calculator("a", 3, 4))
print(calculator("s", 3, 4))
print(calculator("d", 16, 4))
print(calculator("m", 3, 4))
print(calculator("p", 3, 4))

