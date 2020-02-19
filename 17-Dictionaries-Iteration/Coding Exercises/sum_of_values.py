# Declare a sum_of_values that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])  => 5
# sum_of_values(my_dict, ["a", "c"])  => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])  => 0


def sum_of_values(nums_dict, in_char):
    total = 0
    for dict_char, number in nums_dict.items():
        for char in in_char:
            if char == dict_char:
                total += number
    return total


my_dict = {"a": 5, "b": 3, "c": 10}

print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["a", "c", "b"]))
print(sum_of_values(my_dict, ["z"]))
