#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Get all the cars and their types that do not qualify for clean alternative fuel vehicle
non_qualifying_cars = df.loc[df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"] == "No", ["Make", "Vehicle Type"]]

# Get all TESLA cars with the model year and model type made in Bothell City
tesla_cars = df.loc[(df["Make"] == "TESLA") & (df["City"] == "BOTHELL"), ["Model Year", "Model Type"]]

# Get all the cars that have an electric range of more than 100 and were made after 2015
electric_cars = df.loc[(df["Electric Range (Adjusted)"] > 100) & (df["Model Year"] > 2015), :]

# Draw plots to show the distribution between city and electric vehicle type
city_vehicle_type_counts = df.groupby(["City", "Electric Vehicle Type"]).size().unstack()
city_vehicle_type_counts.plot(kind="bar", stacked=True)
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Distribution of Electric Vehicle Types by City")
plt.show()

# Print the results
print("Cars and their types that do not qualify for clean alternative fuel vehicle:")
print(non_qualifying_cars)

print("\nTESLA cars with the model year and model type made in Bothell City:")
print(tesla_cars)

print("\nCars with an electric range of more than 100 and made after 2015:")
print(electric_cars)


# In[ ]:




