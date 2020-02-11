# Define a last_five_characters function that accepts a string argument.
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty") => "nasty"
# last_fiee_characters("empire") => "mpire"


def last_five_characters(chars):
    return chars[-5:]


print(last_five_characters("dynasty"))
print(last_five_characters("empire"))
