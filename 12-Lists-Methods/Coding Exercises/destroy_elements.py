# Declare a function destroy_elements that accepts two lists.
# It should return a list of all elements from the first list
# that are NOT contained in the second list.
#
# Use list comprehension in your solution.
#
# destroy_elements([1, 2, 3], [1, 2]) => [3]
# destroy_elements([1, 2, 3], [1, 2, 3]) => []
# destroy_elements([1, 2, 3], [4, 5]) => [1, 2, 3]


def destroy_elements(list_one, list_two):
    for numa in list_one:
        for numb in list_two:
            print("List one", numa, "List_two", numb)


print(destroy_elements([1, 2, 3], [1, 2]))
# print(destroy_elements([1, 2, 3], [1, 2, 3]))
# print(destroy_elements([1, 2, 3], [4, 5]))
