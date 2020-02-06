# def sum_of_positive_numbers(values):
#     total = 0
#     for value in values:
#         if value > 0:
#             total += value
#     return total


def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value < 0:
            continue  # will skip the neg numbers in this case
        total += value
    return total


print(sum_of_positive_numbers([1, 2, -3, 4]))

for index, num in enumerate([1, 1, 2, 2, 5]):
    if index < num:
        continue
    print(num)