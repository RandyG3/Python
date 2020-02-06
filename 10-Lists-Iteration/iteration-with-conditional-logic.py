values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]


def odds_sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total


print(odds_sum(values))       #48
print(odds_sum(other_values)) #45


def greatest_number(numbers):
    greatest = -1
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest


print(greatest_number([1, 2, 3]))  # 3
print(greatest_number([3, 2, 1]))  # 3
print(greatest_number([4, 5, 5]))  # 5
print(greatest_number([3, 6, 9, 12, 24, 18, 21, 15]))  # 24
print(greatest_number([5, 10, 30, 20, 25, 15]))  # 30
print(greatest_number([-3, -2, -1]))  # -1


def boris_greatest(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(boris_greatest([1, 2, 3]))  # 3
print(boris_greatest([3, 2, 1]))  # 3
print(boris_greatest([4, 5, 5]))  # 5
print(boris_greatest([3, 6, 9, 12, 24, 18, 21, 15]))  # 24
print(boris_greatest([5, 10, 30, 20, 25, 15]))  # 30
print(boris_greatest([-3, -2, -1]))  # -1