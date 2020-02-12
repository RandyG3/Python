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

m_list = [1,1,2,2,3,3,3,4,4,4,4]
unq_list = list(set(m_list))
print(unq_list)

list_nums = [1, 2, 3], [1, 2]
# unq_list = list(set(list_nums))
# print(unq_list)

for idx, val in enumerate(list_nums):
    print(idx, val)