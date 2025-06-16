# Bank Deposit Subscription Predictor

This Streamlit app predicts whether a client is likely to subscribe to a term deposit based on various factors (e.g. personal, campaign-related data) using a trained Random Forest classifier.

📦 bank-subscription-app-structure/

├── Bank_Sub.py                 # Streamlit app

├── sub_pred_model.pkl          # Trained ML model

├── model_features.pkl          # List of model features

├── requirements.txt            # Python dependencies

├── Client Sub Prediction.ipynb # Project Notebook

├── README.md                   # Project documentation

└── bank-full.csv/              # Raw data

---

## Project Overview

The project uses classification techniques to predict if a client will subscribe (`yes` or `no`) to a term deposit, based on factors such as age, job, marital status, balance, loan status, and campaign details. 
The machine learning model is trained with consideration of class imbalance using class weights.

---

## Features

- Streamlit web interface for inputting client data
- Real-time prediction
- Pretrained machine learning model using Random Forest
- Includes categorical feature encoding and engineered features
- Handles class imbalance with `class_weight='balanced'`

---

## Machine Learning Workflow

1. **Data Preprocessing**
   - Handled missing values and data types
   - Engineered features such as `age_group`, `balance_level`, and `campaign_efficiency`
   - One-hot encoded categorical variables

2. **Model Training**
   - Model used: `RandomForestClassifier` with `class_weight='balanced'` to handle class imbalance
   - Performance metrics used:
     - Accuracy
     - Precision
     - Recall
     - F1 Score

3. **Model Evaluation**
   - Compared baseline model with class-weighted and SMOTE-enhanced versions
   - Selected the class-weighted model for deployment based on better balance between precision and recall

4. **Deployment**
   - Created a Streamlit app
   - Saved the model and feature schema using `joblib`

---

## How to Run the App

1 **Clone the repository**  
   ```bash
   git clone https://github.com/AfiaAF/TMP_project.git
   ```
2 **Create and activate a virtual environment(Optional)**
   ```
      python -m venv venv
      venv\Scripts\activate # Windows
     
      python3 -m venv venv
      source venv/bin/activate  # macOS/Linux
   ```

 2 **Install dependencies**
  ```pip install -r requirements.txt ```

 3 **Run the Streamlit app**
  ```streamlit run Bank_Sub.py```


## Input Features Used

  Age, 
  Job, 
  Marital status, 
  Education, 
  Default (has credit in default?), 
  Balance, 
  Housing loan, 
  Personal loan, 
  Contact type, 
  Month, 
  Campaign count, 
  Previous contacts, 
  Poutcome (previous campaign outcome)

  Engineered features:
    Age group, 
    Balance level, 
    Campaign efficiency


## Model Overview
  Model: Random Forest Classifier
  
  Handling Imbalance: Class weights
  
  Features Used: 
    Age, Job, Marital Status, Education, Balance, Contact Type, etc.
    
  Target: Whether the client subscribed (yes/no)



## Model Performance Summary
  Model |	Accuracy |	Precision	| Recall	| F1 Score
  
  Random Forest (raw)	| 0.88	| 0.57	| 0.23	| 0.33
 
  Weighted Model |	✅ Improved Recall and F1 Score	        


## Conclusion: 
  This project demonstrates the full machine learning lifecycle:

  Data exploration and preprocessing
  
  Feature engineering and model building
  
  Evaluation with class imbalance consideration
  
  Real-time deployment using Streamlit
  
  The live app serves as a practical decision support tool.
