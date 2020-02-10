# elements removed will not be saved like the pop method

soups = ["French Onion", "Clam Chowder", "Chicken Noodle", "Miso", "Wonton"]

del soups[1]
print(soups)

soups = ["French Onion", "Clam Chowder", "Chicken Noodle", "Miso", "Wonton"]
del soups[-1]
print (soups)

soups = ["French Onion", "Clam Chowder", "Chicken Noodle", "Miso", "Wonton"]
del soups[1:3] # delete 1 & 2
print(soups)