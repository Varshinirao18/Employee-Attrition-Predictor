import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample Data: [age, salary, experience, dept, edu, gender]
X = [
    [25, 50000, 2, 0, 0, 0],  # HR, Graduate, Male
    [32, 65000, 5, 1, 1, 1],  # Tech, Postgraduate, Female
    [45, 80000, 10, 2, 0, 0], # Sales, Graduate, Male
    [29, 70000, 4, 1, 1, 1],  # Tech, Postgrad, Female
    [40, 90000, 7, 2, 2, 0],  # Sales, PhD, Male
]
y = [1, 0, 0, 1, 0]  # 1 = likely to leave, 0 = not likely

model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, 'model.pkl')
print("✅ Model saved as model.pkl")
