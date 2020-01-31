# # Name, adjective, noun
# mad_libs = "{} laughed at the {} {}."

# # args by relative position
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Jennifer", "silly", "tomato")) # extra args ignored; too few = error

# # by numeric pos
# mad_libs = "{0} laughed at the {1} {2}."
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Jennifer", "silly", "tomato"))
# mad_libs = "{2} laughed at the {1} {0}."
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Jennifer", "silly", "tomato"))

mad_libs = "{name} laughed at the {adjective} {noun}."

# args by keywords, now order doesn't matter
#print(mad_libs.format(name = "Bobby", adjective = "green", noun = "alien"))

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))
