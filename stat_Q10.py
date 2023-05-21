#!/usr/bin/env python
# coding: utf-8

# In[1]:


#a
import math

n = 500
k = 20
p = 0.05

# Calculate binomial coefficient
binomial_coefficient = math.comb(n, k)

# Calculate the probability
probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))

print("The probability of exactly 20 bulbs being defective is:", probability)


# In[2]:


#b
import math

n = 500
p = 0.05

probability = 0

# Calculate the probability of at least 10 defective bulbs
for k in range(10, n + 1):
    binomial_coefficient = math.comb(n, k)
    probability += binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))

print("The probability of at least 10 bulbs being defective is:", probability)


# In[3]:


#c
import math

n = 500
p = 0.05

probability = 0

# Calculate the probability of at most 15 defective bulbs
for k in range(16):
    binomial_coefficient = math.comb(n, k)
    probability += binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))

print("The probability of at most 15 bulbs being defective is:", probability)


# In[4]:


#d
n = 500
p = 0.05

expected_defective_bulbs = n * p

print("The expected number of defective bulbs in a batch of 500 is:", expected_defective_bulbs)


# In[ ]:




