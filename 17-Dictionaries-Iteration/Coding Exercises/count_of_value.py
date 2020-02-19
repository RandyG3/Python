# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears
# as a value among the dictionary’s values.
#
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1


my_dict = {"a": 5, "b": 3, "c": 5}


def count_of_value(count_dict, num):
    count = 0
    for _, number in count_dict.items():
        if num == number:
            count += 1
    return count


print(count_of_value(my_dict, 5))
print(count_of_value(my_dict, 3))