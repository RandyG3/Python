alphabet = "abcdefghijklmnopqrstuvwxyz"

print(len(alphabet))
print(alphabet[:10:2])  # 3rd is 'jump by value' 0,2,4,6,8 - 10 not included

print(alphabet[0:26:3])  # jump by 3
print(alphabet[:26:3])  # 0 no needed
print(alphabet[0::3])
print(alphabet[::3])

print(alphabet[4:20:5])
print(alphabet[-20:-8:5])

print(alphabet[::-3])
print(alphabet[::-2])
print(alphabet[::-1])
 
print("paradise"[3:7])
