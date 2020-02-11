# Define a sum_of_values_and_indices function that accepts a list of numbers.
# It should return the sum of all of the elements along with their index values.
#
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0


def sum_of_values_and_indices(numbers):
    sum_numb_indx = 0
    for index, number in enumerate(numbers):
        sum_numb_indx = sum_numb_indx + index + number
    return sum_numb_indx


print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))