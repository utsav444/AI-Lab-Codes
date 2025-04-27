from sklearn.feature_extraction.text import CountVectorizer

with open('sample_text1.txt', 'r') as file:
    text1 = file.read()

with open('sample_text2.txt', 'r') as file:
    text2 = file.read()

with open('sample_text3.txt', 'r') as file:
    text3 = file.read()

texts = [text1, text2, text3]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

word_count_array = X.toarray()

vocabulary = vectorizer.get_feature_names_out()

print("Vocabulary:", vocabulary)
print("\n Bag of Words: ")
for i, word_counts in enumerate(word_count_array):
    print(f"Text {i+1}: {word_counts}")