# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# delete_all([1, 3, 5], 3) => [1, 5]
# delete_all([5, 3, 5], 5) => [3]
# delete_all([4, 4, 4], 4) => []
# delete_all([4, 4, 4], 6) => [4, 4, 4]


def delete_all(strings, target):
    i = 0
    while target in strings:
        strings.remove(target)
        i += 1

    return strings


print(delete_all([1, 3, 5, 3], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))