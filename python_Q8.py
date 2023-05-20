#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# Fetch the data from the URL
response = requests.get("http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes")
data = response.text

# Create a file-like object using StringIO
csv_data = StringIO(data)

# Read the data from the file-like object
df = pd.read_csv(csv_data)
print(df.columns)


# Convert the "airdate" column to datetime format
df["airdate"] = pd.to_datetime(df["airdate"])

# Get all the overall ratings for each season
season_ratings = df.groupby("season")["rating"].mean()

# Plot the ratings for each season
plt.plot(season_ratings.index, season_ratings.values, marker="o")
plt.xlabel("Season")
plt.ylabel("Average Rating")
plt.title("Average Ratings by Season")
plt.show()

# Get all the episode names whose average rating is more than 8 for every season
high_rated_episodes = df.groupby(["season", "name"]).filter(lambda x: x["rating"].mean() > 8)
high_rated_episode_names = high_rated_episodes["name"].unique()

# Get all the episode names that aired before May 2019
before_may_2019 = df[df["airdate"] < pd.Timestamp(2019, 5, 1)]["name"].unique()

# Get the episode name from each season with the highest and lowest rating
highest_rated_episode = df.groupby("season")["rating"].idxmax().apply(lambda x: df.loc[x, "name"])
lowest_rated_episode = df.groupby("season")["rating"].idxmin().apply(lambda x: df.loc[x, "name"])

# Get the summary for the most popular (highest ratings) episode in every season
most_popular_summary = df.loc[df.groupby("season")["rating"].idxmax(), ["season", "summary"]]

# Print the results
print("Overall ratings for each season:")
print(season_ratings)

print("\nEpisode names whose average rating is more than 8 for every season:")
print(high_rated_episode_names)

print("\nEpisode names that aired before May 2019:")
print(before_may_2019)

print("\nEpisode name from each season with the highest rating:")
print(highest_rated_episode)

print("\nEpisode name from each season with the lowest rating:")
print(lowest_rated_episode)

print("\nSummary for the most popular episode in every season:")
print(most_popular_summary)


# In[ ]:




