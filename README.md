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

- Data Preprocessing
  - Encoding categorical variables using `pd.get_dummies`
  - Feature engineering: age groups, campaign efficiency, balance level, etc.
- Model Training
  - Random Forest Classifier with class weights
- Model Evaluation
  - Accuracy, Precision, Recall, F1 Score
- Export
  - Trained model saved using `joblib`
  - Feature list saved for prediction alignment

---

## How to Run the App

1 **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/bank-subscription-predictor.git
   cd bank-subscription-predictor
   ```
2 **Create and activate a virtual environment(Optional)**
   ```
      python -m venv venv
      venv\Scripts\activate # Windows
     
      python3 -m venv venv
      source venv/bin/activate  #macOS/Linux
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
