# Define a easy_money function that accepts no parameters
# and always returns the value 100.


def easy_money():
    return 100


# Define a best_food_ever function that accepts
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    return "Sushi"


# Define a convert_to_currency function that accepts a single parameter (an integer).
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# Example: convert_to_currency(15) => "$15"
def convert_to_currency(dollars):
    convert = "$" + str(dollars)
    return convert


print(easy_money())
print(best_food_ever())
print(convert_to_currency(15))