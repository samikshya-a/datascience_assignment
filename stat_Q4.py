#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def calculate_probability(num_trials):
    perfect_squares = [1, 4, 9, 16]
    count_perfect_squares = 0

    for _ in range(num_trials):
        drawn_number = random.randint(1, 20)
        if drawn_number in perfect_squares:
            count_perfect_squares += 1

    probability = count_perfect_squares / num_trials
    return probability

num_trials = 1000000  # Number of trials to simulate
probability = calculate_probability(num_trials)
print("Probability:", probability)


# In[ ]:




