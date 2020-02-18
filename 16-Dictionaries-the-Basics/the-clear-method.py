websites = {
    "Wikipedia": "http://www.wikipedia.org",
    "Google": "http://www.google.com",
    "Netflix": "http://www.netflix.com"
}

websites.clear()
print(websites)  # Still exists as an object

del websites

print(websites)