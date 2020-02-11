# Declare a function same_index_values that accepts two lists.
# The function should return a list of the index positions in
# which the two lists have equal elements
#
# same_values([1, 2, 3], [3, 2, 1]) => [1]
# same_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) => [1, 3]


def same_index_values(list1, list2):
    same_index = []
    for idx1, elem1 in enumerate(list1):
        for idx2, elem2 in enumerate(list2):
            if elem1 == elem2 and idx1 == idx2:
                same_index.append(idx1)
    return same_index


print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))