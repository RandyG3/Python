candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

# combination of both sets, removing the dups

print(candy_bars.union(sweet_things))
print(sweet_things.union(candy_bars))

# shorthand
print(candy_bars | sweet_things)
print(sweet_things | candy_bars)
