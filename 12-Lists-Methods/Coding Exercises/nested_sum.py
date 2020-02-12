# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# nested_sum([[1, 2, 3], [4, 5]]) => # 15
# nested_sum([[1, 2, 3], [], [], [4], [5]]) => # 15
# nested_sum([[]]) => 0


def nested_sum(list_nums):
    sums = 0
    for number_list in list_nums:
        for number in number_list:
            sums += number
    return sums


print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))
