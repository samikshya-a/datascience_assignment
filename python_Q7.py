#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the Earth meteorite data from the CSV file
url = "https://data.nasa.gov/resource/y77d-th95.json"
df = pd.read_csv(url)

# Convert the "year" column to datetime format
df["year"] = pd.to_datetime(df["year"])

# Get all the Earth meteorites that fell before the year 2000
before_2000 = df[df["year"].dt.year < 2000]

# Get all the Earth meteorites coordinates that fell before the year 1970
before_1970 = df[df["year"].dt.year < 1970]

# Assuming the mass is in kg, get all meteorites with mass more than 10000 kg
more_than_10000kg = df[df["mass"].astype(float) > 10000]

# Plot the distribution of meteorite masses
plt.hist(df["mass"].astype(float), bins=20)
plt.xlabel("Mass (kg)")
plt.ylabel("Count")
plt.title("Distribution of Earth Meteorite Masses")
plt.show()

# Print the results
print("Earth meteorites that fell before the year 2000:")
print(before_2000)

print("\nEarth meteorites coordinates that fell before the year 1970:")
print(before_1970)

print("\nEarth meteorites with mass more than 10000 kg:")
print(more_than_10000kg)-


# In[ ]:




