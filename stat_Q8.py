#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scipy.stats as stats

# Data
before_therapy = [10, 8, 12, 15, 6, 9, 11, 7, 14, 10]
after_therapy = [7, 6, 10, 12, 5, 8, 9, 6, 12, 8]
differences = [after - before for before, after in zip(before_therapy, after_therapy)]

# Perform the Wilcoxon signed-rank test
statistic, p_value = stats.wilcoxon(differences)

# Print the results
print("Wilcoxon signed-rank test results:")
print("Statistic:", statistic)
print("p-value:", p_value)


# In[ ]:




