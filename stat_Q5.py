#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_probability():
    p_company_a = 0.8  # Probability of selecting a taxi from Company A
    p_company_b = 0.2  # Probability of selecting a taxi from Company B
    p_on_time_a = 0.95  # Probability that a taxi from Company A is on time
    p_on_time_b = 0.9  # Probability that a taxi from Company B is on time
    
    p_late = (p_company_a * (1 - p_on_time_a)) + (p_company_b * (1 - p_on_time_b))
    p_a_given_late = (p_company_a * (1 - p_on_time_a)) / p_late
    
    return p_a_given_late

probability = calculate_probability()
print(f"The probability that a randomly selected late taxi belongs to Company A is: {probability}")


# In[ ]:




