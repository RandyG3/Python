# variables always link to objects - never to other variables

a = 3
b = a

a = 5
print(a)  # a is now a new object
print(b)  # b remains the same object which was a
#  have to create a new object to modify a immutable object (which these are)

a = [1, 2, 3] # referencing same list which is mutable
b = a

a.append(4)
print(a)  # these point to
print(b)  # the same object

b.append(5)
print(a)
print(b)
