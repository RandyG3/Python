# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]


def common_elements(in_dict):
    new_list = []
    for key_char, value in in_dict.items():
        print(key_char, value)
        for char in in_dict:
            print(char, in_dict)
    return new_list


my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

print(common_elements(my_dict))
