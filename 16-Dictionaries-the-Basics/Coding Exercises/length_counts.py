# Define a length_counts function that accepts a list of strings.
# The function should return a dictionary where the keys represent
# a length and the values represent how many strings have that length.
#
#
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 2 strings with 7 letters,
# and 1 string with 4 letters.


def length_counts(sa_countries):
    counts = {}
    for country in sa_countries:
        sa_len = len(country)    # get the length of the string (key)
        if sa_len in counts:     # is the key in the dictionary?
            counts[sa_len] += 1  # sa_len is key, after the = is the value for the key
        else:
            counts[sa_len] = 1   # This is a new key/value pair
    return counts


sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))