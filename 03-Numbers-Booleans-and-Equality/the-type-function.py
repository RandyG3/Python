"""
An object is an instance of a class.

Class:
A blueprint from which objects are made.

Instance:
An object made from a class
"""

# returns the class of the object
print(type(5)) # Ints
print(type(10))

print(type(3.8)) # Floats
print(type(3.0))

print(type("computer")) # Strings
print(type("laptop"))
print("*" * 25) 

# Classes can be compared
print(type(5) == type(10))
# holds the same for strings
print(type("computer") == type("laptop")) # str == str?
print(type(5) == type(5.0)) # int == float?
print(type(5) == type("5")) # int == str?
print("*" * 25)

print(type(True))
print(type(False))
print(type(True) == type(False)) # bool == bool?
print("*" * 25)

print(type([1, 2, 3])) # List
print(type({"NH": "Hillsboro"})) # Dict

print(type(3 <= 3))