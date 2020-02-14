# print(dir([]))
# print(dir("pasta")  # methods available
#
print(len("pasta"))
print("pasta".__len__())  # This is what's happening behind the scenes
#
print("st" in "pasta")
print("pasta".__contains__("st"))
#
print("pasta" + " and meatballs")
print("pasta".__add__(" and meatballs"))
