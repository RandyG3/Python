# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
#
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""


def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    new_idx = 0

    for idx, char in enumerate(string):
        start_idx = alphabet.index(char)
        if start_idx == 24:
            new_idx = 0
        elif start_idx == 25:
            new_idx = 1
        else:
            new_idx = start_idx + 2
        encrypted += alphabet[new_idx]

    return encrypted


print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))
