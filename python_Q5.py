#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from bs4 import BeautifulSoup

# Define the API URL to download the data from
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to the API URL and download the data
response = requests.get(url)

# Parse the downloaded data as JSON
data = json.loads(response.content)

# Extract the relevant attributes from the data
episode = data["_embedded"]["episodes"][0]  # Assuming we are interested in the first episode

episode_data = {
    "id": int(episode["id"]),
    "url": episode["url"],
    "name": episode["name"],
    "season": int(episode["season"]),
    "number": int(episode["number"]),
    "type": episode["type"],
    "airdate": episode["airdate"],
    "airtime": episode["airtime"],
    "runtime": float(episode["runtime"]),
    "average_rating": float(episode["rating"]["average"]),
    "summary": BeautifulSoup(episode["summary"], "html.parser").text,
    "medium_image_link": episode["image"]["medium"],
    "original_image_link": episode["image"]["original"]
}

# Print the extracted episode data
print(episode_data)


# In[ ]:




