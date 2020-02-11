def delete_all(strings, target):
    i = 0
    while target in strings:
        strings.remove(target)
        i += 1
    return strings


print(delete_all([4, 4, 4], 4))
