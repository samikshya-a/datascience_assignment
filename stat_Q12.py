#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats

# Data for Group A
group_a_mean = 2.5
group_a_std = 0.8
group_a_size = 30

# Data for Group B
group_b_mean = 2.2
group_b_std = 0.6
group_b_size = 30

# Calculate the degrees of freedom
degrees_of_freedom = group_a_size + group_b_size - 2

# Calculate the pooled standard deviation
pooled_std = ((group_a_size - 1) * group_a_std**2 + (group_b_size - 1) * group_b_std**2) / degrees_of_freedom
pooled_std = pooled_std**0.5

# Calculate the t-statistic
t_statistic = (group_a_mean - group_b_mean) / (pooled_std * (1/group_a_size + 1/group_b_size)**0.5)

# Calculate the p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), degrees_of_freedom))

# Check if the p-value is less than the significance level (0.05)
if p_value < 0.05:
    conclusion = "Reject the null hypothesis. There is a significant difference in the mean improvement scores."
else:
    conclusion = "Failed to reject the null hypothesis. There is no significant difference in the mean improvement scores."

# Print the t-test results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
print("Conclusion:", conclusion)


# In[ ]:




