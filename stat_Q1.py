#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

# Given data
sat_scores = [1300, 1450, 1200, 1550, 1400]  # list of SAT scores
college_gpa = [3.2, 3.5, 2.8, 3.9, 3.6]      # list of college GPAs

# Convert lists to NumPy arrays
sat_scores_arr = np.array(sat_scores)
college_gpa_arr = np.array(college_gpa)

# Calculate the correlation coefficient
correlation_coef = np.corrcoef(sat_scores_arr, college_gpa_arr)[0, 1]

print("The correlation coefficient between SAT scores and college GPA is:", correlation_coef)


# In[ ]:




