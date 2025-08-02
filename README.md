# 📧 Spam Message Classifier – ML Web App
An end-to-end machine learning web application to classify SMS and email messages as Spam or Not Spam using NLP and Naive Bayes.

🚀 Features:

🔍 Real-time spam detection through a simple web form

🧠 Machine Learning (Multinomial Naive Bayes) for classification

🧹 Text preprocessing: tokenization, stopword removal, stemming

📊 TF-IDF vectorization to convert text into numerical features

🌐 Web app built with Streamlit and Python

💬 Supports both email and SMS classification

🧠 Tech Stack & Key Skills:
| Category           | Tools & Libraries                          |
| ------------------ | ------------------------------------------ |
| Programming        | Python                                     |
| NLP Tools          | NLTK (stopwords, tokenizer, stemmer)       |
| ML Algorithm       | Multinomial Naive Bayes                    |
| Feature Extraction | TF-IDF Vectorizer                          |
| Web Framework      | Streamlit (frontend + backend integration) |
| Others             | Scikit-learn, pandas, NumPy                |

📂 Project Structure:

sms-spam-classifier/
│
├── app.py                 # Streamlit app for user interaction

├── model.pkl              # Trained ML model

├── vectorizer.pkl         # TF-IDF vectorizer object

├── trainmodel..py         # Text preprocessing functions

├── README.md              # Project documentation

└── requirements.txt       # Python dependencies


⚙️ How to Run the Project: 


# 1. Clone the repository
```bash
git clone https://github.com/yourusername/spam-classifier.git
```
```bash
cd spam-classifier
```
# 2. Install required packages
```bash
pip install -r requirements.txt
```
# 3. Run the application
```bash
streamlit run app.py
```



