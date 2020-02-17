def larger_num(one, two):
    if one > two:
        return one
    else:
        return two


values = [5, 3]             # Need to pass these in as *values
print(larger_num(values))
