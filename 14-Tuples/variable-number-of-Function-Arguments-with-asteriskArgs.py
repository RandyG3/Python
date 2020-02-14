def accept_stuff(*args):  # collect any number of arguments
    # print(type(args))
    print(args)


accept_stuff(1)
accept_stuff(1, 3, 5)
accept_stuff()


def my_max(*numbers):
    # assume 1st is the max value
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


def my_max2(nonsense, *numbers):
    # assume 1st is the max value
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(my_max2("Shazam", 1))
print(my_max2("Hoorah", 3))
print(my_max2("Yea", 1, 3, 6, 7, 8, -14))


def my_max3(*numbers, nonsense):
    # assume 1st is the max value
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(my_max3(1, nonsense = "Shazam"))
print(my_max3(3, nonsense = "Hoorah"))
print(my_max3(1, 3, 6, 7, 8, -14, nonsense ="Yea"))