#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset from a local file
data = pd.read_csv('https://www.kaggle.com/datasets/rxsraghavagrawal/instagram-reach')

# Split the dataset into input features (X) and target variables (y)
X = data[['Username', 'Caption', 'Hashtag', 'Followers']]
y_likes = data['Likes']
y_time_since_posted = data['Time_Since_posted']

# Split the data into training and testing sets
X_train, X_test, y_likes_train, y_likes_test, y_time_train, y_time_test = train_test_split(X, y_likes, y_time_since_posted, test_size=0.2, random_state=42)

# Train a random forest regression model for predicting the number of likes
rf_likes = RandomForestRegressor(n_estimators=100, random_state=42)
rf_likes.fit(X_train, y_likes_train)

# Make predictions on the test set for the number of likes
likes_predictions = rf_likes.predict(X_test)

# Evaluate the model for the number of likes using mean squared error
likes_mse = mean_squared_error(y_likes_test, likes_predictions)
print("Mean Squared Error for likes:", likes_mse)

# Train another random forest regression model for predicting the time since posted
rf_time_since_posted = RandomForestRegressor(n_estimators=100, random_state=42)
rf_time_since_posted.fit(X_train, y_time_train)

# Make predictions on the test set for the time since posted
time_predictions = rf_time_since_posted.predict(X_test)

# Evaluate the model for the time since posted using mean squared error
time_mse = mean_squared_error(y_time_test, time_predictions)
print("Mean Squared Error for time since posted:", time_mse)


# In[ ]:




