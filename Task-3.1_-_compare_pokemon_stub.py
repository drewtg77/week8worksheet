"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def compare_pokemon(pokemon1, pokemon2):
    """Compare the calculated stats of two Pokémon."""
    # TODO: Fetch data for both Pokémon from the PokéAPI
    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1.lower()}"
    url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2.lower()}"
    
    response1 = httpx.get(url1)
    response2 = httpx.get(url2)

    data1 = response1.json()
    data2 = response2.json()

    # TODO: Extract relevant stats (HP, attack, defense, speed)
    stats1 = {s['stat']['name']: s['base_stat'] for s in data1['stats']}
    hp1 = stats1['hp']
    attack1 = stats1['attack']
    defense1 = stats1['defense']
    speed1 = stats1['speed']


    stats2 = {s['stat']['name']: s['base_stat'] for s in data2['stats']}
    hp2 = stats2['hp']
    attack2 = stats2['attack']
    defense2 = stats2['defense']
    speed2 = stats2['speed']

    
    # TODO: Calculate stats at level 50 for both Pokémon
    hp1 = calculate_hp(hp1)
    attack1 = calculate_stat(attack1)
    defense1 = calculate_stat(defense1)
    speed1 = calculate_stat(speed1)

    hp2 = calculate_hp(hp2)
    attack2 = calculate_stat(attack2)
    defense2 = calculate_stat(defense2)
    speed2 = calculate_stat(speed2)


    
    # TODO: Compare the calculated stats and print the results
    print(f'At level 50, {pokemon1}s hp is {hp1}, its attack is {attack1}, its defense is {defense1} and its speed is {speed1}.')
    print(f'At level 50, {pokemon2}s hp is {hp2}, its attack is {attack2}, its defense is {defense2} and its speed is {speed2}.')


# Example usage
if __name__ == "__main__":
    compare_pokemon("pikachu", "bulbasaur")

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""
