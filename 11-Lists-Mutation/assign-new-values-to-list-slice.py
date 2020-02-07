coworkers = ["Michael", "Jim", "Dwight", "Pam", "Creed", "Angela"]
# Replace values Pam & Creed
# print(coworkers[3:5])
# coworkers[3:5] = ["Oscar", "Ryan"]
# print(coworkers)
# print()

coworkers = ["Michael", "Jim", "Dwight", "Pam", "Creed", "Angela"]
# Python will replace Pam and remove creed - not enough values supplied
# if you supply more, the 2 will be replaced and the other values will be added to the list
# coworkers[3:5] = ["Oscar"]
print(coworkers)
#
# coworkers[3:5] = ["Creed", "Pam", "Oscar", "Angela", "Ryan"]
# print(coworkers)

coworkers[-3:-1] = ["Ryan", "Andy"]  # Replace Pam & Creed with Ryan & Angela. Upto but not including Angela
print(coworkers)

