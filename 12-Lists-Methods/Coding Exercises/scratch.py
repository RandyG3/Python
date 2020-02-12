# from Quiz

quote = "four score and seven years ago"
words_of_wisdom = quote.split(" ")
print(words_of_wisdom)

print("!".join(["who", "let", "the", "dogs", "out?"]))

lotto = [
    [10, 5, 8],
    [8, 5, 10],
    [10, 8, 5]
]
# print(lotto[-3][3])  # IndexError

for el in lotto:
    for value in el:
        print(value)

list = [1, 1, 3, 1, 1]
print(.issp