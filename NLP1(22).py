import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
    

nltk.download('punkt')
nltk.download('stopwords')

with open('sample_text.txt', 'r') as file:
    text = file.read()

text = re.sub(r'[^a-zA-Z\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

text = text.lower()
tokens = word_tokenize(text)

stopwords = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stopwords]

corrected_tokens = []
for word in filtered_tokens:
    corrected_word = TextBlob(word).correct()
    corrected_tokens.append(str(corrected_word))

print("\n Original Text:")
print(text)
print("\n New Text: ")
print(corrected_tokens)
