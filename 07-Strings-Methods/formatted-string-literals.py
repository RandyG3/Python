name = "Bobby"
adjective = "green"
noun = "alien"

#
# f is for formatted string; don't need name = name, etc.
mad_libs = f"{name} laughed at the {adjective} {noun}."
print(mad_libs)
mad_libs = F"{name} laughed at the {adjective} {noun}."
print(mad_libs)

print(f"2 + 2 is {2 + 2}") # curly braces can have a formula