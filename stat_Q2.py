#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scipy.stats as stats

# Given information
mean_height = 170
std_dev = 10
sample_size = 1000

# a. Percentage of individuals with heights between 160 cm and 180 cm
z_score_160 = (160 - mean_height) / std_dev
z_score_180 = (180 - mean_height) / std_dev
percentage_between_160_180 = stats.norm.cdf(z_score_180) - stats.norm.cdf(z_score_160)
percentage_between_160_180 *= 100
print(f"a. Percentage of individuals with heights between 160 cm and 180 cm: {percentage_between_160_180}%")

# b. Probability that the average height of 100 individuals is greater than 175 cm
sample_mean = mean_height
sample_std_dev = std_dev / (sample_size ** 0.5)  # Standard deviation of the sample mean
z_score_175 = (175 - sample_mean) / sample_std_dev
probability_avg_height_gt_175 = 1 - stats.norm.cdf(z_score_175)
print(f"b. Probability that the average height of 100 individuals is greater than 175 cm: {probability_avg_height_gt_175}")

# c. Z-score corresponding to a height of 185 cm
z_score_185 = (185 - mean_height) / std_dev
print(f"c. Z-score corresponding to a height of 185 cm: {z_score_185}")

# d. Approximate height corresponding to a threshold of 5%
threshold_5 = stats.norm.ppf(0.05) * std_dev + mean_height
print(f"d. Approximate height corresponding to a threshold of 5%: {threshold_5} cm")

# e. Coefficient of variation (CV)
cv = (std_dev / mean_height) * 100
print(f"e. Coefficient of variation (CV) for the dataset: {cv}%")

# f. Skewness of the dataset
skewness = 0  # Given that skewness is approximately zero
print("f. Skewness of the dataset: The dataset is symmetrically distributed around the mean.")


# In[ ]:




