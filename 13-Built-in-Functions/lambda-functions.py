#  Lambda Function
#  An anonymous function
#  (a function without a name)
#
#  use once, then discard


metals = ["gold", "silver", "platinum", "palladium"]

# get words more than 5 char
print(filter(lambda metal: len(metal) > 5, metals))
print(list(filter(lambda metal: len(metal) > 5, metals)))

print(list(filter(lambda metal: "p" in metal, metals)))

# count the number of "l"s
print(list(map(lambda word: word.count("l"), metals)))

# return new list where lower "s" is replaced with a $
print(list(map(lambda val: val.replace("s", "$"), metals)))
