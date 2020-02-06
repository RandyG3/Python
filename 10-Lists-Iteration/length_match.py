# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0


def length_match(strings, number):
    num_strings = 0
    for string in strings:
        if len(string) == number:
            num_strings += 1
    return num_strings


print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([], 5))
