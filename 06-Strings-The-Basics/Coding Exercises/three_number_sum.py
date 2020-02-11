# Define a three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123") => 6
# three_number_sum("567") => 18
# three_number_sum("444") => 12
# three_number_sum("000") => 0


def three_number_sum(nums):
    # a longer way
    num1 = int(nums[0])
    num2 = int(nums[1])
    num3 = int(nums[2])
    return num1 + num2 + num3
    # return int(nums[0]) + int(nums[1]) + int(nums[2])

print(three_number_sum("123"))
print(three_number_sum("567"))
print(three_number_sum("444"))
print(three_number_sum("000"))
