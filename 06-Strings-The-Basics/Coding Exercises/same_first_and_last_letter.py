# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner") => True
# same_first_and_last_letter("Runner") => False
# same_first_and_last_letter("clock")  => False
# same_first_and_last_letter("q")      => True


def same_first_and_last_letter(letter):
    return letter[0] == letter[-1]


print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner"))
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q"))
