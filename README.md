

#Employee Attrition Predictor using Machine Learning

#Project Overview

Employee attrition (voluntary or involuntary resignation) is a major concern in HR management.  
This project uses a machine learning model to predict whether an employee is likely to leave, based on various features like job satisfaction, years at company, work-life balance, etc.

#Objectives

- Predict if an employee will leave the company or stay
- Help HR departments reduce turnover
- Provide actionable insights for retention strategies

#Technologies Used

| Component        | Tools & Libraries                       |
|------------------|------------------------------------------|
| Programming      | Python                                   |
| Model            | Random Forest / Logistic Regression      |
| Data Handling    | Pandas, NumPy                            |
| Visualization    | Matplotlib, Seaborn                      |
| Web Framework    | Flask (for deployment)                   |
| Frontend         | HTML, CSS, Bootstrap                     |
| Authentication   | SQLite                                   |
| Deployment Ready | Render / Railway Compatible              |

#Dataset Info

- Source: IBM HR Analytics Dataset (Kaggle)
- Records: ~1,470 employee records
- Target: `Attrition` (Yes/No)
- Features: Age, BusinessTravel, JobRole, JobSatisfaction, MonthlyIncome, etc.
- Data Cleaning: Null removal, encoding categorical variables, normalization


#Model Details

- ✅ Model: Random Forest / Logistic Regression
- 📊 Accuracy: ~88% on test data
- 📁 Vectorizer: Label Encoding + Scaling
- 🧪 Evaluation: Confusion Matrix, Classification Report

#Features

- User Login/Register System (SQLite)
- Prediction Page (Input employee data → Get result)
- Result Output: “Likely to leave” / “Likely to stay”
- Model Performance Insights

#How to Run the App Locally

-->bash
# Step 1: Clone the repo
git clone https://github.com/Varshinirao18/employee-attrition-predictor.git
cd employee-attrition-predictor

# Step 2: Install packages
pip install -r requirements.txt

# Step 3: Run the Flask app
python app.py
```

Then visit: `http://127.0.0.1:5000`

---

## 📸 Screenshots

### 🔐 Login Page  
<img src="https://raw.githubusercontent.com/yourusername/employee-attrition-predictor/main/screenshots/login.png" width="500"/>

### 📊 Dashboard / Input Page  
<img src="https://raw.githubusercontent.com/yourusername/employee-attrition-predictor/main/screenshots/dashboard.png" width="500"/>

### 📍 Prediction Result  
<img src="https://raw.githubusercontent.com/yourusername/employee-attrition-predictor/main/screenshots/result.png" width="500"/>


#License

This project is licensed under the **Apache 2.0 License**.  
See `LICENSE` file for full details.


##Developed by

**Varshini** – Machine Learning Enthusiast  
🔗 [GitHub](https://github.com/yourusername) • [LinkedIn](https://linkedin.com/in/yourprofile)
=======
# Employee Attrition Predictor

This project is a machine learning-based web application to predict whether an employee is likely to leave the company.

## Features
- Trained ML model (`model.pkl`)
- Flask web app (`app.py`)
- HTML templates for frontend
- Training script (`train_model.py`)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`

## Output
The app gives predictions based on input employee data.
>>>>>>> e36c23edd8e2b01587eea2c77806d71e7698b11c
