# Define a sum_of_lengths function that accepts a list of strings.

# The function should return the sum of the string lengths.

# sum_of_lengths(["Hello", "Bob"]) => 8
# sum_of_lengths(["Nonsense"])     => 8
# sum_of_lengths(["Nonsense", "or", "confidence"]) => 20


def sum_of_lengths(strings):
    total = 0
    for word in strings:
        for char in word:
            total += 1
    return total


print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]))