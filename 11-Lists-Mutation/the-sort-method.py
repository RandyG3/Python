# Sort list in-place num low to hi, chars a-z

temps = [40, 28, 52, 66, 36]
temps.sort()
print(temps)
temps.reverse()
print(temps)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort()  # Caps sort before lowercase
print(coffees)
coffees.reverse()
print(coffees)

coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
coffees.sort()  # uppercase sort before lowercase
print(coffees)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees))  # doesn't modify the existing