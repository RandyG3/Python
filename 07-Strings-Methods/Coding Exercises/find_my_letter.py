# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a") => 1
# find_my_letter("bazooka", "z") => 2
# find_my_letter("lollipop", "z") => -1


def find_my_letter(word, char):
    return (word.find(char))

print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))
