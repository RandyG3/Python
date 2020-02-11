# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"]) => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"]) => "cat er pillar"
# cleanup(["", "", " "]) => ""


def cleanup(strings):
    new_string = ""
    str1 = ' '.join(strings)
    words = str1.split(" ")
    for word in words:
        if len(word) >= 1:
            new_string += word
    print(new_string)

    # final_string = (" ".join(words))
    # print(len(final_string))
    # print(final_string)


print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))