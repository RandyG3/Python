print("ABC", "DEF", "XYZ")
print("ABC", "DEF", "XYZ", sep='!')
print("ABC", "DEF", "XYZ", sep='--*--')

print("hello", "Goodbye", end="!&*")
print("hello")

print("a", "b", "c", sep='**', end='#')
# order doesn't matter as long as params are at end
print("a", "b", "c", end='#', sep='**')
