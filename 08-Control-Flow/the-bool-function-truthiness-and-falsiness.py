# in Python 0 is False, all others are True
if 3:
    print("All nums except 0 are True")

if -1:
    print("All nums except 0 are True")

if 0:
    print("This is False and doesn't execute")

# Empty strings are False, all others are True

if "Hello":
    print("Goodbye")    

if "":   
    print("This is False and doesn't execute")

# to get the bool value:
print(bool(1))
print(bool(0))

user_num = 39
strnum = str(user_num)
if len(strnum) < 3:
    print("Pad with zeros")