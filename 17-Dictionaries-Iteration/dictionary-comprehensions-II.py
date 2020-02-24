# Create a new dict from an existing dict

capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin",
    "New Hampshire": "Concord"
}
print(capitals)

# Map from Capital to State - flip around

inverted = {capital: state for state, capital in capitals.items()}
print(inverted)

inverted = {capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(inverted)

