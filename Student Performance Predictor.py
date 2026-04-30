# Student Score Prediction (simple project)

from sklearn.linear_model import LinearRegression
import numpy as np

# data sederhana (jam belajar vs nilai)
hours_data = np.array([[1], [2], [3], [4], [5], [6]])
score_data = np.array([50, 55, 65, 70, 80, 90])

# bikin model
lr_model = LinearRegression()

# training model
lr_model.fit(hours_data, score_data)

# input dari user
user_input = input("Enter how many hours you study per day: ")

try:
    hours = float(user_input)

    # prediksi nilai
    result = lr_model.predict([[hours]])

    print("Your predicted score is:", round(result[0], 2))

except:
    print("Invalid input, please enter a number.")
print("Note: This prediction is based on a very small dataset, so it may not be very accurate.")