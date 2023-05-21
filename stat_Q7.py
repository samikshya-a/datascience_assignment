#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

variance_X = 4
regression_equation_X = "2*X + 3 - 8 = 0"
regression_equation_Y = "2*Y + X - 5 = 0"

# Variance of Y
variance_Y = variance_X * (1 - (1 / (2 ** 2)))
print("Variance of Y:", variance_Y)

# Coefficient of Determination (R^2)
coefficient_determination = 1 - (variance_Y / variance_X)
print("Coefficient of Determination (R^2):", coefficient_determination)

# Standard Error of Estimate
standard_error_X_on_Y = math.sqrt((1 - coefficient_determination) * variance_X)
standard_error_Y_on_X = math.sqrt((1 - coefficient_determination) * variance_Y)
print("Standard Error of Estimate (X on Y):", standard_error_X_on_Y)
print("Standard Error of Estimate (Y on X):", standard_error_Y_on_X)


# In[ ]:




