# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is longer than the second
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")   => True
# first_longer_than_second("cat", "mouse")     => False
# first_longer_than_second("Steven", "Seagal") => False


def first_longer_than_second(word1, word2):
    return len(word1) > len(word2)


print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))
