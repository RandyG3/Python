number = 0.123456789

print(format(number, "f"))          # Returns a string
print(type(format(number, "f")))

print(format(number, ".2f"))        # digits after decimal
print(format(number, ".1f"))
print(format(number, ".3f"))

print(format(0.5, "f"))
print(format(0.5, "%"))
print(format(0.5, ".2%"))

print(format(123456, ","))          # follows traditional
print(format(1234567890, ","))
