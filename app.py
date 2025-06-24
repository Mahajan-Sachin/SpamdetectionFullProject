from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# 🧠 Load the trained model and vectorizer
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    user_input = None

    if request.method == 'POST':
        user_input = request.form['message']
        if user_input.strip():  # avoid empty input
            transformed_input = vectorizer.transform([user_input])
            prediction = model.predict(transformed_input)[0]

    return render_template('index.html', prediction=prediction, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
