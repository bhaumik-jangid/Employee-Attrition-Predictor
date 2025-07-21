# Employee Attrition Predictor

## Project Overview
This project aims to predict whether an employee is likely to leave the company (attrite) based on several key features. It's a classic binary classification problem in HR analytics, providing an early warning system for companies to implement targeted retention strategies.

## Goal
The primary goal is to build a machine learning model that can accurately predict employee attrition, allowing HR departments to proactively address factors contributing to churn and optimize retention efforts.

**Hosted Link**: [Employee Attrition Predictor](https://bhaumik-jangid.github.io/Employee-Attrition-Predictor/)

---

## Dataset Features
The project utilizes a dataset with the following features:

- **MonthlyIncome**: Employee's monthly income.  
- **Age**: Employee's age.  
- **JobSatisfaction**: Employee's satisfaction level with their job (e.g., on a scale of 1 to 4).  
- **YearsAtCompany**: Number of years the employee has worked at the company.  
- **OverTime**: Indicates if the employee works overtime (`Yes`/`No`).  
- **Attrition**: The target variable, indicating if an employee left the company (`1` for Attrition, `0` for No Attrition).  

---

## Machine Learning Approach
This project uses a **Binary Classification** approach.

- **Models Explored**:  
  - Logistic Regression  
  - Decision Tree Classifier

- **Current Model**:  
  The **Logistic Regression** model is used for prediction due to its better performance in identifying attrition, especially after applying feature scaling and addressing class imbalance.

---

## Project Structure

| File | Description |
|------|-------------|
| `employee_data.xlsx` | Raw dataset containing employee information |
| `attrition_predictor.py` | Python script for data loading, preprocessing, model training, and evaluation |
| `index.html` | Frontend HTML file for inputting custom data and getting predictions |
| `style.css` | CSS file for styling the web interface |
| `script.js` | JavaScript file for handling input, scaling, and prediction logic |

---

## Setup and Installation

### Python Environment
It's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate
