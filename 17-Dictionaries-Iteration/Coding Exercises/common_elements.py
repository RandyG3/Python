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

my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}


def common_elements(my_dict):
    new_list = []
    for key_char in my_dict.keys():
        for value in my_dict.values():
            if key_char == value:
                new_list.append(key_char)
    return new_list


print(common_elements(my_dict))
