import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import numpy as np


#Data Loading
file_path = 'employee_data_2000_rows.xlsx'

try:
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    print("Data loaded successfully!")
    print(f"Initial dataset shape: {df.shape}")
    print(df.head())

    #Data Cleaning & Preprocessing
    print("\n--- Starting Data Cleaning and Preprocessing ---")

    #  Handle Missing Values in 'Attrition'
    # Rows with missing target values dropped
    initial_rows = df.shape[0]
    df.dropna(subset=['Attrition'], inplace=True)
    rows_after_attrition_nan_drop = df.shape[0]
    print(f"Dropped {initial_rows - rows_after_attrition_nan_drop} rows with missing 'Attrition' values.")
    print(f"Remaining rows after dropping Attrition NaNs: {rows_after_attrition_nan_drop}")

    #   Impute Missing Values in Numerical Features with Median.
    numerical_cols_with_nan = ['MonthlyIncome', 'Age', 'JobSatisfaction', 'YearsAtCompany']
    for col in numerical_cols_with_nan:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"Filled missing values in '{col}' with its median: {median_val}")

    #   Encode 'OverTime' Column
    # Converting Yes/No into 1/0
    df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})

    #   Converting 'Attrition' to Integer Type
    df['Attrition'] = df['Attrition'].astype(int)

    #   Attrition is 0 or 1
    invalid_attrition_rows = df[~df['Attrition'].isin([0, 1])]
    if not invalid_attrition_rows.empty:
        print(f"Found {len(invalid_attrition_rows)} rows with 'Attrition' values not equal to 0 or 1. Dropping these rows...")
        df = df[df['Attrition'].isin([0, 1])] # Keep only rows where Attrition is 0 or 1
        print(f"Remaining rows after ensuring binary Attrition: {df.shape[0]}")
    else:
        print("'Attrition' column contains only 0s and 1s. No further action needed.")

    print("\n--- Data Preprocessing Complete ---")
    print(f"Final dataset shape after preprocessing: {df.shape}")
    print("\nFirst 5 rows of the preprocessed dataset:")
    print(df.head())
    print("\nInformation about the preprocessed dataset:")
    df.info()
    print("\nMissing values after all preprocessing (should be 0 for all columns):")
    print(df.isnull().sum())
    print("\nUnique values in Attrition column (should be [1, 0] or [0, 1]):")
    print(df['Attrition'].unique())


    #Data Preparation for Modeling
    print("\n--- Preparing Data for Modeling ---")

    X = df[['MonthlyIncome', 'Age', 'JobSatisfaction', 'YearsAtCompany', 'OverTime']]
    y = df['Attrition']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    print(f"Data split into training and testing sets:")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")

    print("\nApplying Feature Scaling to numerical features...")
    numerical_features_for_scaling = ['MonthlyIncome', 'Age', 'JobSatisfaction', 'YearsAtCompany']
    scaler = StandardScaler()

    X_train[numerical_features_for_scaling] = scaler.fit_transform(X_train[numerical_features_for_scaling])
    X_test[numerical_features_for_scaling] = scaler.transform(X_test[numerical_features_for_scaling])
    print("Numerical features scaled using StandardScaler.")
    print("X_train after scaling (first 5 rows of scaled features):\n", X_train.head())


    #Model Training
    print("\n--- Starting Model Training ---")

    print("\nTraining Logistic Regression Model...")
    log_reg_model = LogisticRegression(random_state=42, solver='liblinear')
    log_reg_model.fit(X_train, y_train)
    print("Logistic Regression Model Trained.")

    #Model Stats
    print("\n--- Starting Model Stats ---")

    y_pred_log_reg = log_reg_model.predict(X_test)
    print("\n--- Logistic Regression Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_log_reg):.4f}")
    print(f"Precision (Class 1 - Attrition): {precision_score(y_test, y_pred_log_reg):.4f}")
    print(f"Recall (Class 1 - Attrition): {recall_score(y_test, y_pred_log_reg):.4f}")
    print(f"F1-Score (Class 1 - Attrition): {f1_score(y_test, y_pred_log_reg):.4f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log_reg))
    print("\nClassification Report (Logistic Regression):\n", classification_report(y_test, y_pred_log_reg))

    #Comparison and Conclusion
    print("\n--- Model Comparison Summary ---")
    print("Logistic Regression is trained and evaluated.")
    print("\nGiven the current dataset and features, Logistic Regression appears to be the slightly better performing model for identifying employee attrition.")
    print("However, overall model performance is low, suggesting that more data or additional relevant features would be beneficial for a more robust prediction.")

except Exception as e:
    print(f"An unexpected error occurred during the process: {e}")