# Define a string_adder function that accepts two strings
#   (a and b) as arguments.
# It should return a concatenated version of the arguments
#   with a space in between.
# If the user does not pass in arguments, both arguments
#   should default to an empty string.

def string_adder(a="", b=""):
    return a + " " + b

print(string_adder("Randy", "Russell"))
print(string_adder())