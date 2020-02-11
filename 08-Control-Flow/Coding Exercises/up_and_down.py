# Define an up_and_down function that accepts a string argument
# If the string consists of all uppercase letters, return a new string
# consisting of all lowercase letters. If the string consists of all
# lowercase letters, return a new string consisting of all uppercase
# characters. If the string has a mix of uppercase and lowercase
# characters, return a new string where the casing of each letter is swapped.
#
# up_and_down("HELLO") => "hello"
# up_and_down("genius") => "GENIUS"
# up_and_down("ESPreSso") => "espREsSO"


def up_and_down(str_arg):
    if str_arg.isupper():
        return str_arg.lower()
    elif str_arg.islower():
        return str_arg.upper()
    elif str_arg.upper() + str_arg.lower():
        return str_arg.swapcase()


print(up_and_down("HELLO"))
print(up_and_down("genius"))
print(up_and_down("ESPreSso"))
