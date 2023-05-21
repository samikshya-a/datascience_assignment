#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import f_oneway

# Sample data of scores for each student
student_scores = {
    'Karan': [85, 90, 92],
    'Deepa': [70, 80, 85],
    'Karthik': [90, 85, 88],
    'Chandan': [75, 70, 75],
    'Jeevan': [95, 92, 96]
}

# Extracting the scores for all students
scores = list(student_scores.values())

# Performing one-way ANOVA test
_, p_value = f_oneway(*scores)

# Checking if the mean scores are the same
if p_value < 0.05:
    print("The mean scores of the students are different.")
    
    # Finding the student with the highest score
    max_score = max([np.mean(score) for score in scores])
    for student, score in student_scores.items():
        if np.mean(score) == max_score:
            print("The student with the highest score:", student)
else:
    print("The mean scores of the students are the same.")


# In[ ]:




