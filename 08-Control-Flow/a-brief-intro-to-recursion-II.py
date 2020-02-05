def reverse(word):
    start_index = 0
    last_index = len(word) - 1  # 4
    reverse_string = ""        # w

    while last_index >= start_index:
        reverse_string += word[last_index]
        last_index -= 1
    return reverse_string


def recurs(word):
    if len(word) <= 1:
        return word

    return word[-1] + reverse(word[:-1])

# Straw
# w + reverse(stra)
# w + a + reverse(str)
# w + a + r + reverse(st)
# w + a + r + t + reverse(s)
# w + a + r + t + s


print(reverse("boris"))
print(reverse("randy"))
print(reverse("russell"))
print(reverse("evert"))
print(reverse("junior"))
print(reverse("brutus"))
print(reverse("tralfaz"))
print("------ Recursion")
print(recurs("boris"))
print(recurs("randy"))
print(recurs("russell"))
print(recurs("evert"))
print(recurs("junior"))
print(recurs("brutus"))
print(recurs("tralfaz"))
