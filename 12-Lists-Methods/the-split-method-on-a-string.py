users = "Bob, Dave, John, Sue, Randy, Meg"  # Split at ', ' into a new list

print(users.split(", "))
print()
print(users.split(", ", 2))  # max split, remainder concatenated into a single list
print()
sentence = "I am learning to code"
words = sentence.split(" ")
print(len(words))
print(words)
