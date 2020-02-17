students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes)
print(students == nerds)
print()
print(students is athletes)  # True, the same object in memory
print(students is nerds)     # False, same strings, but different objects in memory
print()

a = 1
b = 1
print(a == 1)
print(a is b)


