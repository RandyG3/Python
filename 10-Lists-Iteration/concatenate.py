# Define a function concatenate that accepts a list of strings.

# The function should return a concatenated string which consists
# of all list elements whose length is greater than 2 characters.

# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""


def concatenate(word_str):
    new_string = ""
    for chars in word_str:
        if len(chars) > 2:
            new_string = new_string + chars
    return new_string


print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"]))