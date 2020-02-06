# Define a smallest_number function  that accepts a list of numbers.

# It should return the smallest value in the list.

# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3


def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))

