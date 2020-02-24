def length(word):
    return len(word)


print(length("Hello"))
print(length(word="Hello"))  # Keyword arg used

# print(length())  # Returns error
# print(length(something = "Hello"))  # what is something? error returned
# print(length(word = "Hello", something = "Goodbye"))  # similar error


def collect_keyword_arguments(**kwargs):  # kwargs is conventional name
    # **kwargs creates a dictionary with k/v pairs
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}")


collect_keyword_arguments(a=2, b=3, c=4, d=5)


def args_and_kwargs(a, b, *args, **kwargs):
    #               the above is the order for mixed input
    print(f"The total of your regular arguments a and b is {a + b}")
    print(f"The total of your args tuple is {sum(args)}")

    dict_total = 0
    for value in kwargs.values():
        dict_total += value

    print(f"The total of your kwargs dictionary is {dict_total}")


#               a  b  ..tuple...  kwargs
args_and_kwargs(1, 2, 3, 4, 5, 6, x=8, y=9, z=10)
