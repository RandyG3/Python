# As far as I can tell if you want to pull elements from the list and print a new list
# using those elements you use filter. Whereas map you can pull elements and carry out
# an operation on them and then print a new list with the results of the operation.
#
# From Boris
# That's basically it. filter to filter (subset) down the original list, map to return a new list
# of the same size.

animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]
long_words = [animal for animal in animals if len(animal) > 5]
print(long_words)

#
# Needs to return a bool
#


def is_long_animal(animal):
    return len(animal) > 5  # This returns the bool


print(list(filter(is_long_animal, animals)))
print(list(filter(is_long_animal, ["Doggies", "Cat"])))
