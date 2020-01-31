empty_space = "     content             "

print(empty_space.rstrip()) # Right only
print(empty_space.lstrip()) # Left only

print(empty_space.strip()) # both sides

website = "www.python.org"
print(website.lstrip("w"))
print(website.rstrip(".org"))
print(website.strip("worg.")) # any combo beginning & end only
