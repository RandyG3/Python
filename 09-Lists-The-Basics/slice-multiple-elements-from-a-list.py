print("programming"[3:6])  # from 3 upto but not including
print()
#             0          1          2           3
#            -4         -3         -2          -1
muscles = ["Biceps", "Triceps", "Deltoid", "Sartorius"]
print("1:3", muscles[1:3])
print("1:2", muscles[1:2])
print()
print("0:2", muscles[0:2])
print(":2 ", muscles[:2])
print("2:5", muscles[2:5])
print("2: ", muscles[2:])
print()
print("-4:-2", muscles[-4:-2])
print("-3:  ", muscles[-3:])
print(":-1  ", muscles[:-1])
print("1:-1 ", muscles[1:-1])
print()
print("::2  (increments of 2)", muscles[::2])
print("::-2 (increments of -2)", muscles[::-2])
print("::-1 (increments of -1)", muscles[::-1])  # reverse the list
print("2                      ", muscles[2])  # returns a string, not a list
print("2:-2                   ", muscles[2:-2])
print()
print("From the a quiz on lists")
actors = [
          "Schwarzenegger",
          "Seagal",
          "Lundgren",
          "Stallone",
          "Snipes",
          "Van Damme",
          "Willis",
          "Norris",
          "Li",
          "Statham",
          "Chan"]
# 0 -11 Schwarzenegger
# 1 -10 Seagal
# 2  -9 Lundgren
# 3  -8 Stallone
# 4  -7 Snipes
# 5  -6 Van Damme
# 6  -5 Willis
# 7  -4 Norris
# 8  -3 Li
# 9  -2 Statham
# 10 -1 Chan
print(actors[2:-2], "From index pos 2 up to but not including the 2nd to the last")
print(actors[-1], actors[-11])
print(actors[:4])
print(actors[6:])
print(actors[:-5])  # these two return
print(actors[:6])   # the same results
