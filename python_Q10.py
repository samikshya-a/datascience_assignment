#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def count_pos_tags(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)

    # Initialize counters
    noun_count = 0
    verb_count = 0
    pronoun_count = 0
    adjective_count = 0

    # Count the occurrences of each POS tag
    for word, tag in tagged_words:
        if tag.startswith("NN"):
            noun_count += 1
        elif tag.startswith("VB"):
            verb_count += 1
        elif tag.startswith("PRP"):
            pronoun_count += 1
        elif tag.startswith("JJ"):
            adjective_count += 1

    # Create a dictionary of the counts
    pos_counts = {
        "nouns": noun_count,
        "pronouns": pronoun_count,
        "verbs": verb_count,
        "adjectives": adjective_count
    }

    return pos_counts

# Test the function with example phrases
phrase1 = "The cat chased the mouse."
phrase2 = "I love eating delicious food."
phrase3 = "She went to the store and bought a new dress."

# Count POS tags in each phrase
count1 = count_pos_tags(phrase1)
count2 = count_pos_tags(phrase2)
count3 = count_pos_tags(phrase3)

# Print the results
print(count1)
print(count2)
print(count3)


# In[ ]:




