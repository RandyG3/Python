# Declare a function destroy_elements that accepts two lists.
# It should return a list of all elements from the first list
# that are NOT contained in the second list.
#
# Use list comprehension in your solution.
#
# destroy_elements([1, 2, 3], [1, 2]) => [3]
# destroy_elements([1, 2, 3], [1, 2, 3]) => []
# destroy_elements([1, 2, 3], [4, 5]) => [1, 2, 3]


def destroy_elements(lista, listb):
    return [el for el in lista if el not in listb]


print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))
