# Declare a function right_words that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3) => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5) => ['heart']
# right_words([], 4) => []


def right_words(words, num_letters):
    return list(filter(lambda word: len(word) == num_letters, words))


print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))
