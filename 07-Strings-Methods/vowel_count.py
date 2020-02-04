# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")     => 3
# vowel_count("helicopter") => 4
# vowel_count("ssh")        =>


def vowel_count(word):
    return (word.count("a") + 
            word.count("e") + 
            word.count("i") + 
            word.count("o") + 
            word.count("u"))

print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("shh"))

