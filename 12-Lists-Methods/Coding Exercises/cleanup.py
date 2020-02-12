# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"]) => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"]) => "cat er pillar"
# cleanup(["", "", " "]) => ""

# The solution came from another student with a little cleanup from me


def cleanup(strings_list):
    cleanup_join = ""
    for StrL in strings_list:
        if StrL == " " or "":
            strings_list.remove(" ")
            strings_list.remove("")
            cleanup_join = " ".join(strings_list)
        else:
            cleanup_join = " ".join(strings_list)
    return cleanup_join





print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))
