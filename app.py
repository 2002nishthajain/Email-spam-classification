import pickle
import os
from flask import Flask, render_template, request

script_dir = os.path.dirname(os.path.abspath(__file__))

app =  Flask(__name__)
cv_path = os.path.join(script_dir, "models", "cv.pkl")
clf_path = os.path.join(script_dir, "models", "clf.pkl")
@app.route('/', methods=['GET','POST'])
def home():
    text =""
    if request.method == 'POST' :
        text = request.form.get('email-content')
    return render_template('index.html', text=text)

@app.route('/predict', methods=["POST"])
def predict():
    email = request.form.get('email-content')
    if email is not None:
        tokenized_email = cv.transform([email])
        prediction = clf.predict(tokenized_email)
        prediction = 1 if prediction == 1 else -1
        return render_template("index.html", prediction=prediction, email=email)
    else:
        # Handle the case where email is None (e.g., display an error message)
        return render_template("index.html", prediction=None, email=None)

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=8080, debug=True)