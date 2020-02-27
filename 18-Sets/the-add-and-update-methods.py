disney_characters = {
    "Mickey Mouse",
    "Minnie Mouse",
    "Elsa"
}

add_set = {
    "Bugs Bunny",
    "Foghorn Leghorn",
    "Daffy Duck",
    "Porky Pig"
}
disney_characters.add("Ariel")  # single element added
print(disney_characters)

disney_characters.add("Elsa")  # Won't add because it's a dup (No errors)
print(disney_characters)

# add list
disney_characters.update(["Donald Duck", "Goofy"])
print(disney_characters)

# add tuple
disney_characters.update(("Simba", "Pluto", "Donald Duck"))
print(disney_characters)

# add set
disney_characters.update(add_set)
print(disney_characters)