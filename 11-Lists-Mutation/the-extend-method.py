mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)

extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)

steaks = ["Tenderlion", "NY Strip"]
more_steaks = ["T-Bone", "Ribeye"]
my_meal = steaks + more_steaks  # Combine both into a new list
print(my_meal)

steaks += more_steaks  # Reassign
print(steaks)