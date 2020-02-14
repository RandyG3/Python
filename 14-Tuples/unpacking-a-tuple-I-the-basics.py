employee = ("Bob", "Johnson", "Manager", 50)

# Traditional unpacking
# fn = employee[0]
# ln = employee[1]
# pos = employee[2]
# age = employee[3]
#
# print(fn, ln, pos, age)

# Alternate syntax
# fn, ln, pos, age = employee
# print(fn, ln, pos, age)
#
# subject, verb, adjective = ["Python", "is", "fun"]
# print(subject, verb, adjective)

# Ways things can go wrong:
# must extract the exact same number of variables
# fn, ln, title = employee # didn't provide enough variables
# fn, ln, title, age, salary = employee # provided too many variables

a = 5
b = 10
print(a, b)
# Swap variables
b, a = a, b  # creating a tuple on right-hand side, eval 1st
print(a, b)
