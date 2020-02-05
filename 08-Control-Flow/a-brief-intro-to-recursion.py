# Recursion:
# When a function calls itself

# Traditional way

def count_down_from(num):
    start = num
    while start > 0:
        print(start)
        start -= 1


# print(count_down_from(5))

# Recursion
def count_down_from(num):
    if num <= 0:
        return
    print(num)
    count_down_from(num - 1)



print(count_down_from(5))
