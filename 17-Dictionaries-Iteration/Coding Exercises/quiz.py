def my_func(a, b, **kwargs):
    print(kwargs)


my_func(a=2, b=3, c=4, d=5)
my_func(b=5, a=10, c=15)


def my_func(a, b, *args, **kwargs):
    print(kwargs)


my_func(20, 30, 40, 50)


sentences = [
    "Bobby went to the store on the corner",
    "Sally ate a candy bar",
    "Justin played on his deluxe piano"
]

word_counts = {sentence: len(sentence.split(" ")) for sentence in sentences}
print(word_counts)

# This will make each key = to the sum of the values up to a given index
# position in the list
values = [1, 2, 3, 4, 5]
print({value: sum(values[:index+2]) for index, value in enumerate(values)})

prices = {
    "Big Mac": 3.99,
    "FF": 0.99,
    "Soda": 0.99
}

calories = {
    "Big Mac": 600,
    "FF": 300,
    "Soda": 200
}

#                newkey:   newvalue   for         iterate over each item
cheap_options = {meal: calories[meal] for meal, price in prices.items() if price < 1}

print(cheap_options)  # FF: 300, soda: 200
