# Define a factorial function that accepts a single number

# A factorial represents the product of all numbers up to,
# and including, that number. For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120

# Return the factorial from your function. You should NOT
# use any kind of loops. Instead, utilize recursion. Your function MUST call itself.

# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120


# def count_down_from(num):
#     start = num
#     while start > 0:
#         print(start * num)
#         start -= 1


# def factorial(num):
#     loop = 1
#     if num == 0 or num == 1:
#         return num
#     elif num > loop:
#         return num * factorial(num - 1)

# I didn't use recursion - this is from one of the other
# students


def factorial(input_number):
    comparitor = 1
    if input_number == 1 or input_number == 0:
        return input_number
    elif input_number > comparitor:
        return input_number * factorial(input_number -1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# result = 1
# result = result * 1
# result = result * 2
# result = result * 3
# print(result)
