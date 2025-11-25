📧 SMS & Email Spam Classifier – ML + FastAPI Web App

An end-to-end Machine Learning + FastAPI web application that classifies SMS/Email messages as Spam or Not Spam using NLP and Multinomial Naive Bayes.

🚀 Features

🔍 Real-time spam detection

🧠 Multinomial Naive Bayes classifier

🧹 Text preprocessing (cleaning, stopwords, stemming)

📊 TF-IDF vectorization

🌐 FastAPI backend + HTML/CSS/JS frontend

💬 Supports SMS & Email classification

🎨 Color-coded results

🟥 Spam  🟩 Not Spam

🖥️ Tech Stack

#Backend
FastAPI Uvicorn Python 3 Scikit-Learn NLTK Pydantic Pickle (model & vectorizer)

#Frontend

HTML CSS JavaScript (Fetch API)

#Machine Learning

TF-IDF Vectorizer Multinomial Naive Bayes NLP Preprocessing



⚙️ How to Run the Project: 


# 1. Clone the repository
```bash
git clone https://github.com/yourusername/spam-classifier.git
```
```bash
cd sms-spam-classifier
```
# 2. Install required packages
```bash
pip install -r requirements.txt
```
# 3. Run the application
```bash
uvicorn app.main:app --reload
```



