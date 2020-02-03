# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2) => "even"
# even_or_odd(0) => "even"
# even_or_odd(13) => "odd"
# even_or_odd(9) => "odd"


def even_or_odd(intnum):
    if intnum % 2 == 0:
        return "even"
    else:
        return "odd"    


print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))