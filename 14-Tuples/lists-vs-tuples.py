birthday = (8, 4, 1956)

print(len(birthday))
print(birthday[0])
print(birthday[1])
print(birthday[2])
print(birthday[-1])
print(birthday[-2])
print(birthday[-3])

# Cannot change any of the values in a tuple
# Lists are mutable
# Mutable objects can be contained in a tuple

addresses = (
    ['Harvey Way', 'Hillsboro', 'NH'],
    ['Island Pond Rd', 'Manchester', 'NH']
)

#  addresses[1] = "Something else" - this can't be done
addresses[1][0] = "School St"
print(addresses)

print(dir(birthday))  # no append, pop, etc.
