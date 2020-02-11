# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# push_or_pop([10]) => [10]
# push_or_pop([10, 4]) => []
# push_or_pop([10, 20, 30]) => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]


def push_or_pop(numbers):
    new_list = []
    for num in numbers:
        if num > 5:
            new_list.append(num)
        elif num <= 5:
            del new_list[-1]

    return new_list


print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))