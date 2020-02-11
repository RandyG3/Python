car_lot = ["Ford", "Dodge", "Toyota", "Ford", "Toyota", "Chevrolet", "Ford"]
print(car_lot.count("Dodge"))
print(car_lot.count("Toyota"))
print(car_lot.count("Ferrari"))  # 0 if item not found
print(car_lot.count("dodge"))  # Case sensitive
print()

hrs_of_sleep = [7.3, 7.0, 8.0, 6.5, 7.0, 8.0]
print(hrs_of_sleep.count(7.3))
print(hrs_of_sleep.count(7.0))
print(hrs_of_sleep.count(7))  # same as 7.0