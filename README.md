Employee Attrition Predictor
Project Overview
This project aims to predict whether an employee is likely to leave the company (attrite) based on several key features. It's a classic binary classification problem in HR analytics, providing an early warning system for companies to implement targeted retention strategies.

Goal
The primary goal is to build a machine learning model that can accurately predict employee attrition, allowing HR departments to proactively address factors contributing to churn and optimize retention efforts.

Hosted Link : https://bhaumik-jangid.github.io/Employee-Attrition-Predictor/

Dataset Features
The project utilizes a dataset with the following features:

MonthlyIncome: Employee's monthly income.

Age: Employee's age.

JobSatisfaction: Employee's satisfaction level with their job (e.g., on a scale of 1 to 4).

YearsAtCompany: Number of years the employee has worked at the company.

OverTime: Indicates if the employee works overtime (Yes/No).

Attrition: The target variable, indicating if an employee left the company (1 for Attrition, 0 for No Attrition).

Machine Learning Approach
This project uses a Binary Classification approach.

Models Explored: Logistic Regression and Decision Tree Classifier.

Current Model: The Logistic Regression model, after feature scaling and addressing class imbalance, is used for prediction due to its better performance in identifying attrition.

Project Structure
The project consists of the following files:

employee_data.xlsx: The raw dataset containing employee information.

attrition_predictor.py: The Python script for data loading, preprocessing, model training, and evaluation.

index.html: The frontend HTML file for a simple web interface to input custom data and get predictions.

style.css: The CSS file for styling the web interface.

script.js: The JavaScript file that handles user input, applies preprocessing (scaling), and uses the trained model's parameters to make predictions in the browser.

Setup and Installation
To run this project, you'll need Python and a few libraries.

Python Environment:
It's recommended to use a virtual environment (like venv or conda).

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate
# Activate the virtual environment (macOS/Linux)
source venv/bin/activate

Install Dependencies:
Install the required Python libraries using pip:

pip install pandas openpyxl scikit-learn numpy

pandas: For data manipulation.

openpyxl: Required by pandas to read .xlsx files.

scikit-learn: For machine learning models and preprocessing.

numpy: For numerical operations.

How to Run the Python Model
Place the Dataset: Ensure employee_data.xlsx is in the same directory as attrition_predictor.py.

Run the Script: Execute the Python script from your terminal:

python attrition_predictor.py

This script will perform:

Data Loading

Data Cleaning & Preprocessing (handling missing values, encoding categorical features, ensuring binary target, feature scaling)

Data Splitting (into training and testing sets)

Model Training (Logistic Regression with class_weight='balanced')

Model Evaluation (Accuracy, Precision, Recall, F1-Score, Confusion Matrix, Classification Report)

Crucially, it will print the scaler.mean_, scaler.scale_, log_reg_model.coef_[0], and log_reg_model.intercept_[0] values. You will need these for the web frontend if you train your own model.

How to Run the Web Predictor
The web predictor allows you to input custom employee data and get a real-time prediction in your browser.

If you want to run the predictor locally or update it with a model trained on your own data:

Place Frontend Files: Ensure index.html, style.css, and script.js are in the same folder.

Extract Model Parameters (if you trained your own model):
After running attrition_predictor.py (especially if you've modified the data or model training), copy the values printed for:

Scaler Mean

Scaler Scale (Std Dev)

Model Coefficients

Model Intercept

Update script.js with New Parameters:
Open script.js and replace the placeholder values for scalerMean, scalerScale, modelCoefficients, and modelIntercept with the actual values you copied from your Python script's output. Ensure the order of coefficients in modelCoefficients matches the feature order used during training: MonthlyIncome, Age, JobSatisfaction, YearsAtCompany, OverTime.

// In script.js:
const scalerMean = [/* PASTE YOUR SCALER MEAN HERE */];
const scalerScale = [/* PASTE YOUR SCALER SCALE HERE */];
const modelCoefficients = [/* PASTE YOUR MODEL COEFFICIENTS HERE */];
const modelIntercept = /* PASTE YOUR MODEL INTERCEPT HERE */;

Open index.html:
Simply open the index.html file in your web browser.

Interact:
Enter values for the employee features and click "Predict Attrition" to see the prediction.

Model Performance Insights
With the larger dataset (2000 initial rows) and the class_weight='balanced' parameter for Logistic Regression, the model's performance significantly improved, especially in Recall for the 'Attrition' class. This means it's very effective at identifying employees who are likely to leave.

However, it's important to note the trade-off: while Recall for attrition is very high, the model might still produce a notable number of False Positives (predicting attrition when it won't happen). This is a common challenge in imbalanced classification and requires balancing business priorities (e.g., is it more costly to miss an attriter or to have too many false alarms?).

Real-life Skill
This project demonstrates skills in HR Analytics and Employee Churn Prediction. It provides a practical application of machine learning to identify and potentially mitigate employee turnover, a critical concern for businesses.