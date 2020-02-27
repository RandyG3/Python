agents = {"Mulder", "Scully", "Doggett", "Reyes"}

# Remove raises a keyError if the value is not found; discard will not raise an error

agents.remove("Doggett")
print(agents)

# agents.remove("Randy")  # Raises KeyError

agents.discard("Randy")  # No error raised in this case
print(agents)
