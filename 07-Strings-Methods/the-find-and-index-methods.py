# Method: A function that acts upon a specific object

browser = "Google Chrome" # Where is C by index position. Finds, returns index, if not, -1

print(browser.find("C")) # Stops at 1st occurrance
print(browser.find("Ch"))  # Stops at 1st occurrance
print(browser.find("o"))  # Stops at 1st occurrance
print(browser.find("G"))  # Stops at 1st occurrance
print(browser.find("z"))  # Stops at 1st occurrance
print(browser.find("c"))  # Stops at 1st occurrance

print()

print(browser.find("o"))  # Stops at 1st occurrance
print(browser.find("o", 2))  # Stops at 1st occurrance
print(browser.find("o", 5))  # Stops at 1st occurrance

# index works the same a find, but if value not found, it rasies a valueError