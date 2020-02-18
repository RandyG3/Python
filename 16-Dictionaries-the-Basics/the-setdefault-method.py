film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}


print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys"))
print(film_directors.get("Bad Boys", "Michael Bay"))  # Key doesn't exist; MB is default
print(film_directors)

film_directors.setdefault("Bad Boys")  # This return none for director
print(film_directors)

film_directors.setdefault("Bad Boys", "Michael Bay")  # This will add if not found
print(film_directors)

film_directors.setdefault("Bad Boys", "A good director") # only adds if key doesn't exisr
print(film_directors)
#
# film_directors.setdefault("Bad Boys", "A good director")
# print(film_directors)