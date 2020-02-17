import copy

# a = [1, 2, 3]
#
# b = a[:]  # new list object
# print(a == b)
# print(a is b)
# print()
#
# c = a.copy()
# print(a == c)
# print(a is c)  # different objects
# print()
#
# d = copy.copy(a)  # using copy module
# print(a == d)
# print(a is d)
# print(copy)

numbers = [2, 3, 4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)

print(a == b)
print(a is b)
print(a[1] is b[1])

a[1].append(100)
print(b)
print(a)

b[1].append(200)
print(b)
print(a)
