print("erm" in "watermelon")
print("z" in "watermelon")
print("z" not in "watermelon")
print()

print(10 in [10, 20, 25])
print(30 in [10, 20, 25])
print(30 not in [10, 20, 25])
print()

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
}

print("Fire" in pokemon)            # Looking for the keys within
print("Grass" in pokemon)
print("Electric" in pokemon)
print("fire" in pokemon)
print()
print("Electric" not in pokemon)
print("fire" not in pokemon)
print("Zombie" not in pokemon)
print("Water" not in pokemon)
#
if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The category of Zombie does not exist!")