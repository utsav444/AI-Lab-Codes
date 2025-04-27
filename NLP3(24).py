from sklearn.preprocessing import LabelEncoder
import numpy as np

# Read the text files
with open('sample_text1.txt', 'r') as file:
    text1 = file.read()

with open('sample_text2.txt', 'r') as file:
    text2 = file.read()

with open('sample_text3.txt', 'r') as file:
    text3 = file.read()

# Combine all the text into a list
texts = [text1, text2, text3]

# Tokenize the texts into words
words = []
for text in texts:
    words.extend(text.split())

# Get unique words for vocabulary
vocabulary = list(set(words))

# Create one-hot encoding for each word
one_hot_encoded = []
for text in texts:
    encoded_text = []
    for word in vocabulary:
        # Append 1 if the word is in the text, otherwise 0
        encoded_text.append(1 if word in text.split() else 0)
    one_hot_encoded.append(encoded_text)

# Print the one-hot encoded result
print("Vocabulary:", vocabulary)
print("\nOne-Hot Encoded Texts:")
for i, encoded_text in enumerate(one_hot_encoded):
    print(f"Text {i+1}: {encoded_text}")
