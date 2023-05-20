#!/usr/bin/env python
# coding: utf-8

# In[1]:


def highest_frequency_length(string):
    word_frequency = {}
    max_frequency = 0
    max_length = 0

    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

        # Update the maximum frequency and corresponding length
        if word_frequency[word] > max_frequency:
            max_frequency = word_frequency[word]
            max_length = len(word)

    return max_length

# Test the function with the example input
input_string = "write write write all the number from from from 1 to 100"
output = highest_frequency_length(input_string)
print(output)


# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

# In[2]:


def highest_frequency_length(string):
    word_frequency = {}
    max_frequency = 0
    max_length = 0

    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

        # Update the maximum frequency and corresponding length
        if word_frequency[word] > max_frequency:
            max_frequency = word_frequency[word]
            max_length = len(word)

    return max_length

# Test the function with the example input
input_string = "How How many times times times do I have have have have to tell you this?"
output = highest_frequency_length(input_string)
print(output)


# Explanation - From the given string we can note that the most frequent words is "have" and its corresponding length is 4.

# In[3]:


def highest_frequency_length(string):
    word_frequency = {}
    max_frequency = 0
    max_length = 0

    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

        # Update the maximum frequency and corresponding length
        if word_frequency[word] > max_frequency:
            max_frequency = word_frequency[word]
            max_length = len(word)

    return max_length

# Test the function with the example input
input_string = "Rohit likes likes fish in in in his breakfast."
output = highest_frequency_length(input_string)
print(output)


# Explanation - From the given string we can note that the most frequent words "in" and its corresponding length is 2.
