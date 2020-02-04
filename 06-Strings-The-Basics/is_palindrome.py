# Define a is_palindrome function that accepts a string argument.
# The function should return True if the string is spelled
# the same backwards as it is forwards.
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar") => True
# is_palindrome("yummy")   => False


def is_palindrome(word):
    return word[:] == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))    