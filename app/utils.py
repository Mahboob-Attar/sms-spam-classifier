import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# AUTO-DOWNLOAD STOPWORDS IF NOT INSTALLED
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

# Initialize stemmer
ps = PorterStemmer()

#  LOAD MODEL + VECTORIZER
with open("models/vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# TEXT PREPROCESSING
def transform_text(text: str) -> str:
    """
    Preprocess the text: lowercase, tokenize, remove stopwords, and stem.
    """
    text = text.lower()

    # Extract words only
    tokens = re.findall(r'\b\w+\b', text)

    # Stopword removal
    english_stopwords = stopwords.words("english")
    filtered = [word for word in tokens if word not in english_stopwords]

    # Stemming
    stemmed = [ps.stem(word) for word in filtered]

    return " ".join(stemmed)

# PREDICT MESSAGE
def predict_message(text: str) -> str:
    """
    Preprocess message, vectorize it, and predict spam or ham.
    """
    transformed = transform_text(text)
    vector_input = tfidf.transform([transformed])
    result = model.predict(vector_input)[0]

    return "Spam" if result == 1 else "Not Spam"
