#!/usr/bin/env python
# coding: utf-8

# In[4]:


def is_valid_string(s):
    # Count the frequency of each character in the string
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Check if all characters have the same frequency
    frequency_set = set(char_frequency.values())
    if len(frequency_set) == 1:
        return "YES"  # All characters have the same frequency

    # Check if removing one character makes the string valid
    if len(frequency_set) == 2 and 1 in frequency_set:
        # Remove the character with frequency 1 and check if all remaining characters have the same frequency
        char_to_remove = max(char_frequency, key=char_frequency.get)
        char_frequency[char_to_remove] -= 1
        if len(set(char_frequency.values())) == 1:
            return "YES"  # Removing one character makes the string valid

    return "NO"  # The string is not valid


# Test the function with the example inputs
input_string_1 = "abc"
output_1 = is_valid_string(input_string_1)
print(output_1)

input_string_2 = "abcc"
output_2 = is_valid_string(input_string_2)
print(output_2)


# In[7]:


def is_valid_string(s):
    # Count the frequency of each character in the string
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Check if all characters have the same frequency
    frequency_set = set(char_frequency.values())
    if len(frequency_set) == 1:
        return "YES"  # All characters have the same frequency

    # Check if removing one character makes the string valid
    if len(frequency_set) == 2 and 1 in frequency_set:
        # Remove the character with frequency 1 and check if all remaining characters have the same frequency
        char_to_remove = max(char_frequency, key=char_frequency.get)
        char_frequency[char_to_remove] -= 1
        if len(set(char_frequency.values())) == 1:
            return "YES"  # Removing one character makes the string valid

    return "NO"  # The string is not valid


# Test the function with the example inputs
input_string_1 = "abc"
output_1 = is_valid_string(input_string_1)
print(output_1)

input_string_2 = "height"
output_2 = is_valid_string(input_string_2)
print(output_2)


# In[8]:


def is_valid_string(s):
    # Count the frequency of each character in the string
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Check if all characters have the same frequency
    frequency_set = set(char_frequency.values())
    if len(frequency_set) == 1:
        return "YES"  # All characters have the same frequency

    # Check if removing one character makes the string valid
    if len(frequency_set) == 2 and 1 in frequency_set:
        # Remove the character with frequency 1 and check if all remaining characters have the same frequency
        char_to_remove = max(char_frequency, key=char_frequency.get)
        char_frequency[char_to_remove] -= 1
        if len(set(char_frequency.values())) == 1:
            return "YES"  # Removing one character makes the string valid

    return "NO"  # The string is not valid


# Test the function with the example inputs
input_string_1 = "abc"
output_1 = is_valid_string(input_string_1)
print(output_1)

input_string_2 = "aabcdd"
output_2 = is_valid_string(input_string_2)
print(output_2)


# In[ ]:




