print(all([True]))                  # True
print(all([True, True]))            # True
print(all([True, True, False]))     # False
print(all([1, 2, 3]))               # True
print(all([1, 2, 3, 0]))            # False
print(all(["a", "b"]))              # True
print(all(["a", "b", ""]))          # False
print(all([]))                      # True
print("-" * 20)
print(any([True, False]))           # True
print(any([False, False]))          # False
print(any([0, 1]))                  # True
print(any([0]))                     # False
print(any([" ", ""]))               # True
print(any([""]))                    # False
print(any([]))                      # False
