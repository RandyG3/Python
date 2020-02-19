# Declare an invert function that accepts a dictionary object.
# The function should return a new dictionary where the keys and
# values from the original dictionary are inverted.
# Each key should now be a value, and each value should be a key.
# Assume both the keys and values of the dictionary are immutable.
#
# my_dict = {
#   "A": "B",
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}


my_dict = {
  "A": "B",
  "C": "D",
  "E": "F"
}


def invert(orig_dict):
    new_dict = {}
    for orig_key, orig_value in orig_dict.items():
        new_dict[orig_value] = orig_key
    return new_dict


print(invert(my_dict))