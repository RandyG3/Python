# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
#
# word_lengths("Mary Poppins was a nanny") => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut") => [8, 5, 2, 5]


def word_lengths(string):
    word_length = []
    words = string.split(" ")
    for word in words:
        word_length.append(len(word))
    return word_length


print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))