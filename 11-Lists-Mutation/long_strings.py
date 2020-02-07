# Define a long_strings function that accepts a list of strings.
#
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# long_strings(["Hello", "Goodbye", "Sam"] => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"] => []
# long_strings([] => []


def long_strings(words):
    long_words = []
    for word in words:
        if len(word) >= 5:
            long_words.append(word)
    return long_words


print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))