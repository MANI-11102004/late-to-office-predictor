# 🚗 Late to Office Predictor

A Machine Learning application that predicts whether a person is likely to be late to the office based on the distance they need to travel and the time remaining.

## 🌐 Live Demo

👉 https://late-to-office-predictor.streamlit.app/

## 📌 Project Overview

This project uses Machine Learning to predict whether a person will be:

- ✅ On Time
- ⚠️ Late

The prediction is based on two inputs:

- Distance from home to office
- Time remaining before the office deadline

## 🧠 Machine Learning

The main model used in this project is:

**Logistic Regression**

The project also includes a **Decision Tree** model for comparison.

## 📊 Dataset

The dataset contains **1,000 records** with balanced classes:

- 500 On-Time samples
- 500 Late samples

### Features

| Feature | Description |
|---|---|
| `distance_km` | Distance from home to office in kilometers |
| `time_left_minutes` | Time remaining in minutes |
| `will_be_late` | Target variable |

### Target Values

```text
0 → On Time
1 → Late

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Git
GitHub
🔄 Machine Learning Workflow
Dataset
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Cloud Deployment
📁 Project Structure
LATE/
│
├── app.py
├── train_model.py
├── late_to_office_dataset.csv
├── late_to_office_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── Late.ipynb
└── Late_Cleaned.ipynb
▶️ Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Train the model
python train_model.py
3. Run the Streamlit application
streamlit run app.py

The application will open at:

http://localhost:8501
🚀 Deployment

The application is deployed using Streamlit Community Cloud.

Live Application

👉 https://late-to-office-predictor.streamlit.app/

🔮 Future Improvements
Traffic conditions
Weather conditions
Average travel speed
Real-time location
Map integration
More Machine Learning models
👨‍💻 Author

Mani Shankar