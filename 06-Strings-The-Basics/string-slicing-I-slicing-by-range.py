address = "Attractive Street, Beverly Hills, CA 90210"
addres1 = "25 Harvey Way, Hillsboro, NH 03244"
print(len(address))
print(len(addres1))
print(address[0:3]) # index start/end inclusive/exclusive (0,1,2)
print(address[0:4])
print(address[0:17])  # index start/end inclusive/exclusive (0 to 12)
print(address[19:32])
print(address[10:100]) # will stop @ end and not throw an error :-)
print("\n")
print(address[-8:-6])
print(address[34:-6])
print("*" * 30)
print("\n")
print(address[5:]) # from index to end
print(address[13:])
print(address[-10:])

print(address[:10]) # same as 0:10
print(address[:23])
print(address[:-3])

print(address[:])  # made a copy
