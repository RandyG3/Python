if 5 < 7 and "rain" == "rain":
    print("Both are True")

if 5 < 7 and "rain" == "fire":
    print("at least one is False, this code doesn't execute")

# Python checks the 1st condition and if false, immediately stops the evaluation

value = 95

# if value > 90 and value < 100:
# Below is a better way of coding
if 90 < value < 100:
    print("This is a shortcut for the win!")
