# Write a function super_sum that accepts a list of strings.

# The function should sum the index positions of the first
# occurrence of the letter “s” in each word.

# Not every word is guaranteed to have an “s”.

# Don’t use the sum keyword as it’s a built-in keyword.
#
# super_sum([]) => 0
# super_sum(["mustache"]) => 2
# super_sum(["mustache", "greatest"]) => 8
# super_sum(["mustache", "pessimist"]) => 4
# super_sum(["mustache", "greatest", "almost"]) => 12


def super_sum(words):
    total = 0
    for word in words:
        if word.find("s") > 0:
            total += word.find("s")
    return total


print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))