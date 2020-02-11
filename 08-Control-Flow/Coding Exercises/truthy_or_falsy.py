# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______"
# where the first space is the argument and the second space
# is either truthy or falsy.
#
# truthy_or_falsy(0) => "The value 0 is falsy"
# truthy_or_falsy(5) => "The value 5 is truthy"
# truthy_or_falsy("Hello") => "The value Hello is truthy"
# truthy_or_falsy("") => "The value  is falsy"


def truthy_or_falsy(sing_arg):
    if sing_arg:
        return "The value " + str(sing_arg) + " is truthy"
    else:
        return "The value " + str(sing_arg) + " is falsy"
    
print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))
