import random
def generate_comcast_id(first_name, last_name):
    first_init = first_name[0:1]
    first_five_last = last_name[0:5]
    num = str(random.randint(0,999))
    if len(num) = 2
        print("2")
    # if len(num) == 1
    #     num += "00"
    #     else:
    #         num += "0"
    return first_init + first_five_last + num 

print(generate_comcast_id("Randy", "Galinat"))
print(generate_comcast_id("Matthew", "Saviano"))   
print(generate_comcast_id("James", "Angelone")) 