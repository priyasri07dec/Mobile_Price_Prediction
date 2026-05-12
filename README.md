# Mobile_Price_Prediction

## Project Overview
This project is a Machine Learning based web application that predicts the price of a mobile phone based on its specifications such as RAM, battery capacity, processor details, camera quality, internal memory, and display features.

The project was developed using Python, Scikit-learn, and Streamlit.

## Features
- Predicts mobile phone prices using machine learning
- Performs complete Exploratory Data Analysis(EDA)
- Handles skewness and outliers
- Applies feature scaling using standard scaler
- Compares multiple regression algorithms
- Interactive streamlit web application
- User friendly interface

## Dataset

### Dataset Used:
Mobile Price Prediction dataset is used from Kaggle

### Features included:
- Sale
- Weight
- Resolution
- PPI
- CPU Core
- CPU Frequency
- Internal Memory
- RAM
- Rear Camera
- Front Camera
- Battery Capacity

### Target Variable:
- Price

## Machine Learning Workflow
The following steps were performed:

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Visualization
5. Skewness Treatment using Log Transformation
6. Outlier Detection and Treatment using IQR Method
7. Feature Scaling using StandardScaler
8. Train-Test Split
9. Model Building
10. Model Evaluation
11. Streamlit Web App Deployment

## Algorithms Used

The following regression algorithms were compared:

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression

## Model Performance

### Model              Performance
Linear Regression          0.866
Ridge Regression           0.870
Lasso Regression           0.866
ElasticNet                 0.875

ElasticNet achieved the best performance among all the models

## Streamlit Application

The Project also includes an interactive web application where user can input the mobile specifications and get the predicted price

## Project Structure

Mobile Price Prediction

app.py
cellphone.csv
mobile_phone_prediction_model.pkl
scaler.pkl
requirements.txt
README.md

## How to run the project

### Step 1: Clone the Repository

bash
git clone 

### Step 2: Install Dependencies

bash
pip install -r requirements.txt

### Step 3: Run Streamlit App

bash
streamlit run app.py

## Conclusion

This project successfully predicts mobile phone prices using Machine Learning techniques. Different regression models were compared, and ElasticNet Regression achieved the best performance. The project demonstrates the complete Machine Learning workflow from data preprocessing to deployment.




