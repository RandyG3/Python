story = "Once upon a time"

print(story.capitalize())
print(story.title())
print(story.upper())
print("HELLO".lower())
print(story.swapcase()) # all lower to upper & all upper to lower
print("AbCdE".swapcase())

# method chaining - make the name proper case
print("RANDY GALINAT".lower().title())

story = story.title()
print(story)

print("lord of lies".title())
print("lord of lies".title().swapcase())
