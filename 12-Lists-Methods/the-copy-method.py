# returns a "shallow" copy: a single dimension list

units = [
    "meter",
    "Kilogram",
    "second",
    "ampere",
    "kelvin",
    "candela",
    "mole"
]

more_units = units.copy()
print(units)       # original
print(more_units)  # copy

units.remove("kelvin")
print(units)       # original, modified
print(more_units)  # copy, untouched

# shorthand
even_more_units = units[:]
print(even_more_units)
