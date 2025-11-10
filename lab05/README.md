# Lab 05: Professional Yapping

Learned how to use code that can randomly generate sentences based on pre-specified inputs.

## What it does
The `yap.py` program generates random sentences by:
- Defining a dictionary of word categories (nouns, verbs, adjectives, prepositions, adverbs, colors)
- Using a sentence template with placeholders for each word type
- Randomly selecting words from each category to fill in the template
- Generating 5 unique random sentences each time it runs

The program demonstrates:
- Working with dictionaries to organize data
- Using the `random.choice()` function for random selection
- String processing with `.split()` and `.join()`
- Template-based text generation