#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Blood Pressure Before and After data
blood_pressure_before = [130, 142, 120, 135, 148, 122, 137, 130, 142, 128, 135, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127, 130, 142, 128, 136, 140, 132, 145, 124, 128, 136, 143, 127, 139, 135, 131, 127]
blood_pressure_after = [120, 135, 118, 127, 140, 118, 129, 124, 137, 125, 129, 132, 125, 136, 118, 122, 130, 139, 123, 132, 131, 126, 120, 123, 139, 122, 129, 136, 127, 140, 119, 121, 129, 137, 122, 135, 131, 124, 119, 124, 139, 123, 131, 135, 130, 125, 121, 124, 139, 123, 131, 135, 130, 125, 121, 124, 139, 123, 131, 135, 130, 125, 121, 124, 139, 123, 131, 135, 130, 125, 121, 124, 139, 123, 131, 135, 130, 125, 121, 124, 139, 123, 131, 135, 130, 125]

# Dispersion
dispersion_before = np.var(blood_pressure_before)
dispersion_after = np.var(blood_pressure_after)

# Interpretation of Dispersion
print("Dispersion (Blood Pressure Before):", dispersion_before)
print("Dispersion (Blood Pressure After):", dispersion_after)
print()

# Mean and Confidence Interval
mean_before = np.mean(blood_pressure_before)
mean_after = np.mean(blood_pressure_after)
confidence_interval_before = stats.norm.interval(0.95, loc=mean_before, scale=np.std(blood_pressure_before)/np.sqrt(len(blood_pressure_before)))
confidence_interval_after = stats.norm.interval(0.95, loc=mean_after, scale=np.std(blood_pressure_after)/np.sqrt(len(blood_pressure_after)))

# Plotting mean and confidence interval
labels = ['Blood Pressure Before', 'Blood Pressure After']
means = [mean_before, mean_after]
confidence_intervals = [confidence_interval_before, confidence_interval_after]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, means, width, label='Mean')
rects2 = ax.errorbar(x, means, yerr=[(mean - interval[0], interval[1] - mean) for mean, interval in zip(means, confidence_intervals)], fmt='none', color='black', capsize=5)

ax.set_ylabel('Blood Pressure (mmHg)')
ax.set_title('Mean and 95% Confidence Interval')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

# Mean absolute deviation and Standard deviation
mad_before = np.mean(np.abs(blood_pressure_before - np.mean(blood_pressure_before)))
mad_after = np.mean(np.abs(blood_pressure_after - np.mean(blood_pressure_after)))
std_before = np.std(blood_pressure_before)
std_after = np.std(blood_pressure_after)

# Interpretation of Mean absolute deviation and Standard deviation
print("Mean Absolute Deviation (Blood Pressure Before):", mad_before)
print("Mean Absolute Deviation (Blood Pressure After):", mad_after)
print()
print("Standard Deviation (Blood Pressure Before):", std_before)
print("Standard Deviation (Blood Pressure After):", std_after)
print()

# Correlation coefficient and significance test
correlation_coef, p_value = stats.pearsonr(blood_pressure_before, blood_pressure_after)
alpha = 0.01

# Interpretation of correlation coefficient and significance test
print("Correlation Coefficient:", correlation_coef)
print("p-value:", p_value)
if p_value < alpha:
    print("The correlation coefficient is statistically significant at the 1% level.")
else:
    print("The correlation coefficient is not statistically significant at the 1% level.")


# In[ ]:




