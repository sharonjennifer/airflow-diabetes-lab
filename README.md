# Airflow Lab: Diabetes Prediction with Random Forest

## Project Overview
This project implements a machine learning pipeline using Apache Airflow to predict diabetes using the Pima Indians Diabetes dataset.

## Modifications from Original Lab
- **Dataset**: Changed to Pima Indians Diabetes dataset (768 samples, 8 features)
- **Model**: Random Forest Classifier (100 estimators, max_depth=10)
- **Pipeline**: 5-task workflow for data loading, preprocessing, training, and notifications

## Project Structure
dags/
├── my_dag.py
├── data/
│   └── diabetes.csv
└── src/
    ├── model_development.py
    └── success_email.py

## DAG Tasks
1. load_data_task – loads dataset
2. data_preprocessing_task – split and scale data (70/30)
3. separate_data_outputs_task – manages data flow
4. build_save_model_task – trains Random Forest model
5. task_send_email – sends success notification

## Results
All tasks completed successfully; accuracy metrics logged in Airflow.

## Setup Instructions
1. Install Apache Airflow
2. Copy files into Airflow’s `dags/` folder
3. Start Airflow and trigger DAG via UI
4. Verify logs for model accuracy

## Author
Jennifer Sharon
