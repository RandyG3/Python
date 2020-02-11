# Declare a long_word_in_collection function that accepts a list and a string.
# The function should return True if
#   - the word exists in the list AND
#   - the word has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False


def long_word_in_collection(words, string):
    return True if string in words and len(string) > 4 else False


print(long_word_in_collection(["cat", "dog", "rhino"], "rhino"))
print(long_word_in_collection(["cat", "dog", "rhino"], "cat"))
print(long_word_in_collection(["cat", "dog", "rhino"], "monkey"))