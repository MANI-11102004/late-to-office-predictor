# 🚗 Late to Office Predictor

> A Machine Learning web application that predicts whether a person is likely to be late to the office based on distance and remaining time.

## 🌐 Live Demo

🚀 **[Open the Late to Office Predictor](https://late-to-office-predictor.streamlit.app/)**

---

## 📌 About the Project

The **Late to Office Predictor** is a Machine Learning application that predicts whether a person is likely to reach the office on time.

The prediction is based on two factors:

- 🚗 Distance from home to office
- ⏱️ Time remaining before the deadline

The application provides:

- ✅ On-Time prediction
- ⚠️ Late prediction
- 📊 On-Time probability
- 📊 Late probability
- 🎯 Prediction confidence
- 🖥️ Interactive Streamlit interface

---

## 🧠 Machine Learning

The main Machine Learning model used in this project is:

### Logistic Regression

A **Decision Tree Classifier** is also trained for comparison.

### Model Accuracy

| Model | Accuracy |
|:---|---:|
| Logistic Regression | **99.33%** |
| Decision Tree | **99.67%** |

---

## 📊 Dataset

The dataset contains **1,000 balanced samples**.

| Class | Number of Samples |
|:---|---:|
| 🟢 On Time | 500 |
| 🔴 Late | 500 |
| **Total** | **1,000** |

### Features

| Feature | Description |
|:---|:---|
| `distance_km` | Distance from home to office in kilometers |
| `time_left_minutes` | Time remaining before the deadline |
| `will_be_late` | Target variable |

### Target Values

| Value | Meaning |
|:---:|:---|
| `0` | 🟢 On Time |
| `1` | 🔴 Late |

---

## 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 📦 Joblib
- 🎈 Streamlit
- 🔧 Git
- 🐙 GitHub

---

## 🔄 Machine Learning Workflow

```text
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
Streamlit Cloud Deployment