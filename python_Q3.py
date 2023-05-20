#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import pandas as pd

# Define the URL to download the data from
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# Send a GET request to the URL and download the data
response = requests.get(url)

# Parse the downloaded data as JSON
data = response.json()

# Extract the relevant attributes from the data
pokemon_data = []
for pokemon in data["pokemon"]:
    multipliers = pokemon.get("multipliers")
    if multipliers is not None:
        multipliers = ", ".join(map(str, multipliers))
    else:
        multipliers = ""
        
    pokemon_entry = {
        "id": pokemon["id"],
        "num": pokemon["num"],
        "name": pokemon["name"],
        "img": pokemon["img"],
        "type": ", ".join(pokemon["type"]),
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "candy": pokemon.get("candy", ""),
        "candy_count": pokemon.get("candy_count", ""),
        "egg": pokemon.get("egg", ""),
        "spawn_chance": pokemon.get("spawn_chance", ""),
        "avg_spawns": pokemon.get("avg_spawns", ""),
        "spawn_time": pokemon.get("spawn_time", ""),
        "multipliers": multipliers,
        "weakness": ", ".join(pokemon.get("weaknesses", []))
    }
    pokemon_data.append(pokemon_entry)

# Convert the extracted data to a pandas DataFrame
df = pd.DataFrame(pokemon_data)

# Write the DataFrame to an Excel file
output_file = "pokemon_data.xlsx"
df.to_excel(output_file, index=False)

# Print a success message
print(f"Data has been downloaded, parsed, and saved to {output_file}.")


# In[ ]:




