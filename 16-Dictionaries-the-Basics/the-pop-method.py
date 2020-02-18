years = [1991, 1995, 2000, 2007]
years.pop()  # remove last; if number given, index pos to pop
print(years)

release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

year = release_dates.pop("Python")  # remove key/value by key
print(year)
print(release_dates)

if "Cobol" in release_dates:
    release_dates.pop("Cobol")

new_year = release_dates.pop("C++", 2000)  # '2000' is returned if C++ not found
print(new_year)

#
# del method
#
del release_dates["Java"]  # Doesn't retain the deleted value
print(release_dates)

confusion = {
    "a": "b",
    "b": "c",
    "c": "d"
}
value = del confusion