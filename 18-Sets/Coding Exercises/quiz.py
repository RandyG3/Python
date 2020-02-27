values = [0, 0.0, "0.00"]
print(set(values))  # I think {0} returned; returns {0, '0.0} (Numeric & a string)

pages = {10, 20, 30}
# element = pages.remove(30)  # invalid syntax
pages.remove(30)
print(pages)

pages.add(30)
print(pages)

# pages.add([30, 40, 50])  # Unhashable list error - use below
pages.update([30, 40, 50])
print(pages)

test = set("zyx")
print(test)
