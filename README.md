# Employee Attrition Prediction and Deployment

## Project Overview

Employee attrition is a major challenge for organizations because employee turnover can increase recruitment costs, affect productivity, 
and impact business performance.

This project uses Machine Learning to predict employee attrition based on HR analytics data. A Decision Tree Classification model is 
developed to identify employees who may be at risk of leaving an organization. The trained model is integrated with a Flask web application and deployed on AWS EC2 to make predictions accessible through a web interface.

## Objectives

- Analyze HR analytics data to identify patterns associated with employee attrition.
- Perform exploratory data analysis (EDA) to understand employee characteristics.
- Clean and preprocess the dataset for Machine Learning.
- Build a Decision Tree classification model to predict employee attrition.
- Develop a Flask web application for interactive predictions.
- Deploy the application on AWS EC2.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Decision Tree Classification
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Web Framework:** Flask
- **Cloud Platform:** AWS EC2
- **Version Control:** Git and GitHub

## Project Workflow

1. **Data Collection:** Load the HR analytics dataset.
2. **Exploratory Data Analysis:** Examine employee attributes and identify patterns related to attrition.
3. **Data Preprocessing:** Handle missing values where applicable, encode categorical variables, and prepare the features for model training.
4. **Feature Engineering:** Prepare relevant input variables for the classification model.
5. **Model Development:** Train a Decision Tree classifier using the prepared dataset.
6. **Model Evaluation:** Evaluate model performance using appropriate classification metrics.
7. **Model Serialization:** Save the trained model for reuse by the application.
8. **Flask Integration:** Build a web interface that accepts employee information and returns an attrition prediction.
9. **AWS Deployment:** Host the application on an AWS EC2 instance and configure the required access and security settings.

## Machine Learning Model

The project uses a Decision Tree Classifier, a supervised Machine Learning algorithm suitable for classification problems.

The model learns patterns from historical HR data and predicts the employee attrition class based on the input features.

Model evaluation can include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help assess the model's ability to identify attrition cases and avoid misleading conclusions from accuracy alone.

## Web Application

The Flask application connects the trained Machine Learning model to a user-facing interface.

The application workflow is:

1. The user enters employee-related information.
2. Flask receives the submitted information.
3. The input data is prepared using the same preprocessing steps expected by the trained model.
4. The Decision Tree model generates a prediction.
5. The application displays the predicted attrition class.

## AWS Deployment

The application is deployed on an AWS EC2 instance.

Deployment activities include:

- Launching and accessing an EC2 instance.
- Connecting to the instance using SSH.
- Setting up the required Python environment and dependencies.
- Configuring the application's network access through EC2 security group rules.
- Running the Flask application on the server.

**Note:** Configure production access securely. Avoid exposing development servers or unnecessary ports publicly.

## Business Use Case

This project demonstrates how Machine Learning can support HR analytics by helping organizations:

- Identify potential employee attrition risks.
- Understand workforce patterns.
- Support employee retention planning.
- Make more informed, data-driven HR decisions.

The predictions are intended to support HR decision-making and should not be treated as definitive judgments about individual employees.

## Skills Demonstrated

- Python programming
- Exploratory data analysis
- Data preprocessing and feature engineering
- Supervised Machine Learning
- Classification model evaluation
- Flask application development
- Model integration and serialization
- AWS EC2 deployment
- Git and GitHub version control

## Future Improvements

- Compare Decision Tree performance with Random Forest and other classification algorithms.
- Improve model evaluation and address class imbalance if present.
- Add clearer visualizations of attrition patterns.
- Improve application validation and error handling.
- Implement more robust production deployment and monitoring.

## Conclusion

This project demonstrates an end-to-end Machine Learning workflow, from HR data preparation and classification model development to web application integration and cloud deployment. It combines data analysis, Machine Learning, Python web development, and cloud computing in a practical HR analytics use case.
