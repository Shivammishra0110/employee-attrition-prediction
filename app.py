

from flask import Flask, render_template, request
import numpy as np
import joblib

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load('model.pkl')

print("Model Loaded Successfully")


# Home route
@app.route('/')
def home():
    return render_template('index.html')


# Prediction API
@app.route('/predict', methods=['POST'])
def predict():


    # Extract form input features
    satisfaction_level = float(request.form['satisfaction_level'])
    last_evaluation = float(request.form['last_evaluation'])
    number_project = int(request.form['number_project'])
    monthly_hours = int(request.form['monthly_hours'])
    time_spend_company = int(request.form['time_spend_company'])
    promotion_last_5years = int(request.form['promotion_last_5years'])

    department = request.form['department']
    salary = request.form['salary']

    # Convert categorical values into numbers
    department_mapping = {
        'sales': 0,
        'technical': 1,
        'support': 2,
        'IT': 3,
        'hr': 4,
        'marketing': 5,
        'product_mng': 6,
        'RandD': 7,
        'accounting': 8,
        'management': 9
    }

    salary_mapping = {
        'low': 0,
        'medium': 1,
        'high': 2
    }

    department = department_mapping.get(department, 0)
    salary = salary_mapping.get(salary, 0)

    
# Convert input into 2D array
    input_data = np.array([
    [
        satisfaction_level,
        last_evaluation,
        number_project,
        monthly_hours,
        time_spend_company,
        promotion_last_5years,
        department,
        salary
    ]
])

      # Prediction
    prediction = model.predict(input_data)

    # Return result
    result = prediction[0]

    if result == 1:
        output = "Employee May Leave"
    else:
        output = "Employee Will Stay"

    return f"<h1>{output}</h1>"


# Run Flask app
if __name__ == '__main__':
    app.run(debug=False)