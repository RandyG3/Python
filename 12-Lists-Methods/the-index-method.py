pizzas = [
    "Mushroons",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
    ]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))  # Returns only the 1st
print(pizzas.index("Sausage"))

# print(pizzas.index("Olives")) raises an error
# Solve by:

if "Olives" in pizzas:
    print(pizzas.index("Olives"))

print(pizzas.index("Pepperoni", 2))  # index pos to start the search
print(pizzas.index("Sausage", 3))
print(pizzas.index("Sausage", 2))  # Starts at the index, so it will return 2
