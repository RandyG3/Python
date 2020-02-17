flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices["Seattle"])  # Generates KeyError
# print(flight_prices["chicago"])  # Generates KeyError, case matters

gym_membership_packages = {
    29: ["Machines"],  # Price : items in the package
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
}

print(gym_membership_packages[49])
print(gym_membership_packages[79])
# print(gym_membership_packages[100])  # again, KeyError
#
print(gym_membership_packages.get(29, ["Basic Dumbbells"]))   # key : default if the key doesn't exist
print(gym_membership_packages.get(100, ["Basic Dumbbells"]))  # Key doesn't exist, so "Basic Dumbbells" returned
print(gym_membership_packages.get(100))                       # will return none instead of an error
