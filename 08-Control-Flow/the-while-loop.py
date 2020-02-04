# count = 0
#
# while count <= 5:
#     print(count)
#     count += 1
#
# print(count)

invalid_num = True

while invalid_num:
    user_value = int(input("enter a number above 10: "))
    if user_value > 10:
        print("that works {user_value} is a great choice")
        invalid_num = False
    else:
        print("try again")

