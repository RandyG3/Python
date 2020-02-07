def convert_to_float(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats


def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares


def even_or_odd(numbers):
    even_odd = []
    for number in numbers:
        if number % 2 == 0:
            even_odd.append(True)
        else:
            even_odd.append(False)
    return even_odd


# build brand new lists from powerball numbers
powerball_numbers = [4, 8, 15, 16, 23, 42]

print(powerball_numbers)
print(squares(powerball_numbers))
print(convert_to_float(powerball_numbers))
print(even_or_odd(powerball_numbers))