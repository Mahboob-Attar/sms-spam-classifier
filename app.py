import streamlit as st
import pickle
import string
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize stemmer
ps = PorterStemmer()

# Custom tokenizer (no nltk.word_tokenize needed)
def transform_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation and tokenize
    tokens = re.findall(r'\b\w+\b', text)

    # Remove stopwords
    filtered = [word for word in tokens if word not in stopwords.words('english')]

    # Stemming
    stemmed = [ps.stem(word) for word in filtered]

    return " ".join(stemmed)

# Load the vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    # 4. Display
    if result == 1:
        st.error("🚨 Spam")
    else:
        st.success("✅ Not Spam")
