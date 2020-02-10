# remove by value
nintendo_games = ["Zelda", "Mario", "Donkey Kong", "Zelda"]

nintendo_games.remove("Zelda")  # the 1st occurrance
print(nintendo_games)

nintendo_games.remove("Zelda")  # the 1st occurrance
print(nintendo_games)

# ValueError if element not found
if "Warrior" in nintendo_games:
    nintendo_games.remove("Warrior")
print(nintendo_games)

if "Mario" in nintendo_games:
    nintendo_games.remove("Mario")

print(nintendo_games)
