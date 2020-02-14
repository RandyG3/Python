employee = ("Bob", "Johnson", "Manager", 50)
#
# Can use * only once in the statement

fn, ln, *details = employee  # fn= bob, ln=johnson, remainder to details
print(fn, ln)
print(details)

*names, pos, age = employee
print(names)
print(pos, age)

# get Bob & 50 then the rest
fn, *details, age = employee
print(fn)
print(details)
print(age)

fn, ln, pos, *details = employee
print(fn)
print(ln)
print(pos)
print(details)  # this will be in a list
