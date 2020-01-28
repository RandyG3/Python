# Can only be True or False
# An expression of truth

print(True) # These are NOT strings
print(False) 
print("-" * 25)
# equality operator against 2 objects
print(5 == 5) # result will be T/F
print(5 == 8) # F
print(8.3 == 8.3) # T
print(8.3 == 4.1) # F
print(5 == "5") # will be False
print("-" * 25)
#same in same order, case sensitive
print("ham" == "ham") # T
print("ham" == "bacon") # F
print("ham" == "Ham") # F
print("5" == "5") # T
print( "" == "") # T
print("!==*" == "!==*") # T
print("-" * 25)
print(5 == 5.0) # T mathematically =; cvrts to fp
print(5 == 5.1) # F
print("-" * 25)
print(True == True) # T
print(False == False) # T
print(True == False) # F
print("-" * 25)
# inequality
print(10 != 8) # T
print(10 != 10) # F
print("music" != "music") # F
print("music" != "noise") # T
print("music" != "Music") # T - case matters
print("-" * 25)
print(10 != "10") # T one a string, other an int
print(8.3 != 9.8) # T
print(3.0 != 3) # F - considers both to be 3.0

