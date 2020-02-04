import random
def generate_comcast_id(first_name, last_name):
    first_init = first_name[0:1]
    first_five_last = last_name[0:5]
    min = 0
    max = 999
    digits = str(random.randint(min, max))
    digits = (len(str(max))-len(digits)) * '0' + digits
    return first_init + first_five_last + digits

print(generate_comcast_id("Randy", "Galinat"))
print(generate_comcast_id("Matthew", "Saviano"))   
print(generate_comcast_id("James", "Angelone")) 
