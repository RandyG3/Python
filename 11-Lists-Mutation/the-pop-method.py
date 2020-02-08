action_stars = ["Noris", "Segal", "Van Damme", "Schwarzenegger"]

action_stars.pop()  # no args, removes the last element; it does return but not saving
print(action_stars)

action_stars = ["Noris", "Segal", "Van Damme", "Schwarzenegger"]
last_action_hero = action_stars.pop()
print(last_action_hero)

action_stars = ["Noris", "Segal", "Van Damme", "Schwarzenegger"]
# remove segal
second_star = action_stars.pop(1)
print(action_stars)
print(second_star)

action_stars = ["Noris", "Segal", "Van Damme", "Schwarzenegger"]
muscles_from_brussels = action_stars.pop(-2)  # remove Van Damme
print(action_stars)
print(muscles_from_brussels)