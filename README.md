# 📩 Spam Message Classifier (NLP + Flask)
A mini NLP-based project that detects whether an SMS message is ✉️ Spam or ✅ Not Spam using machine learning (TF-IDF + Logistic Regression). The project includes a complete Flask-based front-end UI where users can type any message and get prediction in real-time.

----

## 🧠 Project Overview
Spam detection is one of the most common applications of Natural Language Processing. In this project:

We’ve built a machine learning model to classify messages as Spam or Not Spam.

Used TF-IDF vectorization to convert text into numeric features.

Created a Flask app with custom HTML frontend for real-time predictions.

----

## 📁 Dataset
We used the publicly available SMS Spam Collection dataset.

📦 Dataset Size: ~5.5k messages

📊 Classes: "ham" (Not Spam), "spam" (Spam)

📝 Source: UCI ML Repository / Kaggle

----

## 🔍 Tech Stack Used
Component	Technology
Language	Python 🐍
NLP	TF-IDF Vectorizer
ML Algorithm	Logistic Regression
Web Framework	Flask ⚙️
Frontend	HTML + CSS
Deployment	Localhost (for now)
Model Saving	Pickle (.pkl files)

⚙️ How to Run Locally
Clone the repository:

Install the required libraries:

pip install -r requirements.txt

Run the Flask app:

 
python app.py

Open browser & visit:


http://127.0.0.1:5000 (similar sort of link will show in terminal)

🖊️ Type your message and see if it's spam or not in real-time.

----

## 💡 Features
✅ TF-IDF based feature extraction
✅ Logistic Regression model
✅ 97%+ accuracy
✅ Clean and styled front-end with user input
✅ Pickled model and vectorizer for easy reuse
✅ Easy-to-use interface built in Flask

----

## 📦 Folder Structure

├── spam.csv                # Dataset

├── app.py                  # Flask backend

├── templates/

|

│   └── index.html          # Frontend HTML

|

├── spam_model.pkl          # Trained ML model

├── tfidf_vectorizer.pkl    # TF-IDF vectorizer

├── README.md               # This file

└── requirements.txt        # Python dependencies

----

## 🏁 Future Plans
✅ Deploy on Streamlit or Render

✅ Add message preprocessing & logging

✅ Add download PDF report feature
---

## 🙋‍♂️ Author

Made with ❤️ by Sachin Mahajan

Connect with me on https://www.linkedin.com/in/sachin-mahajan-24b815284/ 

