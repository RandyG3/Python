bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],  # this is one element with 3 items
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
    ]

print(bubble_tea_flavors)       # All items
print(len(bubble_tea_flavors))  # number of lists
print(bubble_tea_flavors[0])    # First list
print(bubble_tea_flavors[1])    # 2nd list
print(bubble_tea_flavors[2])    # 3rd list
print(bubble_tea_flavors[-1])
print()
print(len(bubble_tea_flavors[0]))  # total elements in the list
print(len(bubble_tea_flavors[1]))  # total elements in the list
print(len(bubble_tea_flavors[2]))  # total elements in the list
print()
print(bubble_tea_flavors[1][2])  # get Strawberry
print(bubble_tea_flavors[0][0])  # get Honeydew
print(bubble_tea_flavors[2][1])  # get Chocolate
print()
#
# nested iteration to create a flat list
#
all_flavors = []
for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        all_flavors.append(flavor)
print(all_flavors)
