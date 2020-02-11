def encrypt_message(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    idx = 0
    indices = ''
    for letter in string:
        idx = alphabet.index(letter)
        new_index = (idx + 2) % len(alphabet)
        print((idx + 2), "modulo % 26", new_index)
        indices += alphabet[new_index]

    return indices


print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))