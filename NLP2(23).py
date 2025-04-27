import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

with open('sample_text.txt', 'r') as file:
    text = file.read()

text = re.sub(r'[^a-zA-Z\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

text = text.lower()
tokens = word_tokenize(text)

stopwords = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stopwords]

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

lemmatizer = WordNetLemmatizer()
lemmetized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

trigrams = []
for i in range(len(lemmetized_tokens) - 2):
    trigrams.append((lemmetized_tokens[i], lemmetized_tokens[i+1], lemmetized_tokens[i+2]))


print("\n Original Text: \n", text)
print("\n New Text: \n", lemmetized_tokens)
print("\n Trigrams: \n", trigrams)
