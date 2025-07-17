import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import re
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download('stopwords')

ps = PorterStemmer()

# 1. Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[["v1", "v2"]]
df.columns = ["label", "text"]
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 2. Preprocessing function
def transform_text(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    tokens = [ps.stem(word) for word in tokens]
    return " ".join(tokens)

# 3. Transform all text
df['transformed'] = df['text'].apply(transform_text)

# 4. Vectorization
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['transformed'])
y = df['label']

# 5. Model training
model = MultinomialNB()
model.fit(X, y)

# 6. Save vectorizer and model
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model and vectorizer saved successfully!")
