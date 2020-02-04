def positive_or_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "negative"
    elif number == 0:
        return "neither: it's 0"

print(positive_or_negative(5))
print(positive_or_negative(0))
print(positive_or_negative(-5))
