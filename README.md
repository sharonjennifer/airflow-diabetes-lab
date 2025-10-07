# Airflow Lab: Diabetes Prediction with Random Forest

## Project Overview
This project implements a machine learning pipeline using Apache Airflow to predict diabetes using the Pima Indians Diabetes dataset.

## Modifications from Original Lab
- **Dataset**: Changed from original to Pima Indians Diabetes dataset (768 samples, 8 features)
- **Model**: Changed to Random Forest Classifier (100 estimators, max_depth=10)
- **Pipeline**: 5-task workflow for data loading, preprocessing, training, and notifications

## Project Structure
dags/
├── my_dag.py                    # Main DAG definition
├── data/
│   └── diabetes.csv             # Dataset
└── src/
    ├── model_development.py     # ML pipeline functions
    └── success_email.py         # Notification handler
DAG Tasks

load_data_task: Loads diabetes.csv
data_preprocessing_task: Splits and scales data (70/30 split)
separate_data_outputs_task: Manages data flow
build_save_model_task: Trains Random Forest model
task_send_email: Sends success notification

Results
All tasks completed successfully. Model trained with accuracy metrics logged in Airflow.
Setup Instructions

Install Apache Airflow
Copy files to Airflow dags folder
Ensure diabetes.csv is in dags/data/
Start Airflow scheduler and webserver
Trigger DAG from UI

Author
Sharon Jennifer Justin Devaraj
