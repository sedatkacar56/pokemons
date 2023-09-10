import pokebase as pb

# Function to retrieve Pokémon type by name
def get_pokemon_type(pokemon_name):
    try:
        pokemon = pb.pokemon(pokemon_name.lower())
        types = [t.type.name.capitalize() for t in pokemon.types]
        return types
    except Exception as e:
        return None

# Main interactive loop
while True:
    pokemon_name = input("Enter a Pokémon name (or 'exit' to quit): ").strip().lower()

    if pokemon_name == 'exit':
        break

    types = get_pokemon_type(pokemon_name)

    if types:
        print(f"{pokemon_name.capitalize()} is a {', '.join(types)} Pokémon.")
    else:
        print(f"Sorry, {pokemon_name.capitalize()} not found. Try another name.")
