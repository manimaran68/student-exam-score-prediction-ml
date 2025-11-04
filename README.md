# 🎓 Student Exam Score Prediction

Student exam score prediction using Machine Learning — includes preprocessing, EDA, feature engineering, and model comparison (LR, RF, GB, DT, SVM) with a Streamlit app based on study habits, sleep, attendance, and previous scores.
---

## 🚀 Project Overview
The goal of this project is to build a predictive model that estimates a student's exam score using various input features.  
It demonstrates the full ML pipeline — from **data collection** to **model deployment**.

---

## 🧩 Dataset
The dataset contains the following features:

| Feature | Description |
|----------|-------------|
| hours_studied | Number of study hours per day |
| sleep_hours | Average sleep duration per day |
| attendance_percent | Attendance percentage |
| previous_scores | Previous exam scores |
| exam_score | Target variable (final predicted score) |

---

## 📘 Project Structure
1. **Data Collection** – Importing and exploring raw data  
2. **Data Preprocessing** – Cleaning, imputing missing values, feature scaling  
3. **EDA (Univariate & Bivariate)** – Understanding feature distributions and correlations  
4. **Feature Selection & Modeling** – Building and comparing ML models  
5. **Deployment** – Streamlit web app for live predictions

---

## 🧠 Models Used
- Linear Regression ✅ *(Best performing model)*
- Random Forest
- Gradient Boosting
- Decision Tree
- Support Vector Machine (SVM)

---

## 📊 Model Performance
| Model | R² | MAE | RMSE |
|--------|----|-----|------|
| Linear Regression | 0.85 | 2.31 | 2.78 |
| Random Forest | 0.79 | 2.95 | 3.30 |
| Gradient Boosting | 0.77 | 2.91 | 3.44 |
| Decision Tree | 0.70 | 3.12 | 3.60 |
| SVM | 0.81 | 2.65 | 3.05 |

---

## 🌐 Deployment
The project includes a **Streamlit app** (`app.py`) that allows users to input:
- Study hours  
- Sleep hours  
- Attendance %  
- Previous exam score  

and get a predicted final exam score instantly.

Run the app locally:
```bash
streamlit run Deployment/app.py

