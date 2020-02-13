# Declare an only_odds function.
# It should return a list with only the odd numbers.
# Do NOT use list comprehension.
#
# only_odds([1, 3, 5, 6, 7, 8]) =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])       =>  []


def only_odds(nums):
    return list(filter(lambda num: num % 2 != 0, nums))


print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))