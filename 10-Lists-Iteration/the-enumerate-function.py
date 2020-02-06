#               0             1                   2               3
errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))  # Generator Object
print()
for index, errand in enumerate(errands):  # index is always 1st
    print(f"{errand} is number {index} on my list of things to do today")
print()
for idx, task in enumerate(errands):  # index is always 1st
    print(f"{task} is number {idx + 1} on my list of things to do today")
print()
for idx, task in enumerate(errands, 1):  # index is always 1st; tell enumerate to use 1 as 1st
    print(f"{task} is number {idx} on my list of things to do today")

