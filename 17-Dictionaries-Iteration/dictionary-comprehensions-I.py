languages = ["Python", "JavaScript", "Ruby"]
# create a dictionary key = lang, value = length

#           key           value            iterable
lengths = {language: len(language) for language in languages}
print(lengths)

# create for only with 't'
lengths = {language: len(language) for language in languages if "t" in language}
print(lengths)

word = "supercalifragilisticexpialidocious"
# how many times letters are in word
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts = {letter: word.count(letter) for letter in word if letter > "j"}
print(letter_counts)