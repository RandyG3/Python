def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254


print(height_to_meters(5, 11))  # Boris' height

stats = {  # must be exact that the function is expecting
    "feet": 5,
    "inches": 11,
}

print(height_to_meters(**stats))


