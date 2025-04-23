from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ""
    if request.method == 'POST':
        age = int(request.form['age'])
        salary = int(request.form['salary'])
        experience = int(request.form['experience'])
        department = int(request.form['department'])
        education = int(request.form['education'])
        gender = int(request.form['gender'])

        input_data = np.array([[age, salary, experience, department, education, gender]])
        prediction = model.predict(input_data)
        prediction_text = "✔️ Likely to leave" if prediction[0] == 1 else "✔️ Not likely to leave"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
