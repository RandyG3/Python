print(int(3.14)) # convert from float to int
print(int(3.99)) # again, no rounding]
print(int("3")) # str to int
print(int(3)) # no change - why?? :-)

print(float(5))
print(float("10.32")) # from str to float
print(float(5.23))  # no change - why?? :-)

print(str(5.35)) # no quotes are returned
print(str(5))
print(str("hello"))

# print(5 + "hello") # Throws an error; 5 isn't a str
print(str(5) + "hello")

print(3 + 3)
print(4.3 + 5.7)
print(3 + 5.8) # converts int to a float 1st then sum the values. auto-type cvrt