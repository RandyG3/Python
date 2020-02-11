# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4 .
# It should return False otherwise.

# divisible_by_three_and_four(3) => False
# divisible_by_three_and_four(4) => False
# divisible_by_three_and_four(12) => True
# divisible_by_three_and_four(18) => False
# divisible_by_three_and_four(24) => true


def divisible_by_three_and_four(num):
    result = True if num % 3 == 0 and num % 4 == 0 else False
    return result


print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))


