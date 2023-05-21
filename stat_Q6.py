#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import stats

# Define the blood pressure before and after as lists
blood_pressure_before = [130, 142, 120, 135, 148, 122, 137, 130, 142, 128, 135, 140, 132, 145, 124, 128, 136, 143, 127, 139,
                         135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127,
                         130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128,
                         136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132,
                         145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128,
                         136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127,
                         139]

blood_pressure_after = [120, 135, 118, 127, 140, 118, 129, 124, 137, 125, 129, 132, 125, 136, 118, 122, 130, 139, 123,
                        132, 131, 126, 120, 123, 139, 122, 129, 136, 127, 140, 119, 121, 129, 137, 122, 135, 129, 124,
                        119, 124, 139, 123, 131, 135, 127, 141, 118, 121, 129, 137, 123, 135, 130, 125, 121, 124, 139,
                        123, 131, 135, 127, 141, 118, 121, 129, 137, 123, 135, 130, 125, 121, 124, 139, 123, 131, 135,
                        127, 141, 118, 121, 129, 137, 123, 135, 130, 125, 121, 124, 139, 123, 131, 135, 127, 141, 118,
                        121, 129, 137, 123, 135, 130, 125, 121, 124, 139, 123, 131, 135, 127, 141, 118, 121, 129, 137,
                        123, 135, 130, 125, 121, 124, 139, 123, 131, 135, 127, 141]

# Perform Shapiro-Wilk test
before_w, before_p = stats.shapiro(blood_pressure_before)
after_w, after_p = stats.shapiro(blood_pressure_after)

# Print the test results
print("Shapiro-Wilk test for blood pressure before:")
print("W value:", before_w)
print("p-value:", before_p)
print("The blood pressure before", "follows a normal distribution." if before_p > 0.05 else "does not follow a normal distribution.")
print()

print("Shapiro-Wilk test for blood pressure after:")
print("W value:", after_w)
print("p-value:", after_p)
print("The blood pressure after", "follows a normal distribution." if after_p > 0.05 else "does not follow a normal distribution.")


# In[ ]:




