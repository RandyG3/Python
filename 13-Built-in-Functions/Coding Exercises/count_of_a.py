# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# count_of_a(["alligator", "aardvark", "albatross"] => [2, 3, 2]
# count_of_a(["plywood"]) => [0]
# count_of_a([]) => []


def count_of_a(animals):
    return list(map(lambda animal: animal.count("a"), animals))


print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))







