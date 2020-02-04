# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty") => "dyn"
# first_three_characters("empire")  => "emp"


def first_three_characters(chars):
    return chars[0:3]


print(first_three_characters("dynasty"))
print(first_three_characters("empire"))
