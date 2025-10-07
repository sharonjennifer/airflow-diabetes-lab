Airflow Diabetes Prediction Lab — Standalone Deployment on VM
Overview

This lab demonstrates the setup, configuration, and execution of Apache Airflow in a Standalone environment on a Virtual Machine (VM).
The workflow automates a machine learning pipeline for predicting diabetes outcomes using the Pima Indians Diabetes dataset and a Random Forest classifier.

The project follows the standard Airflow DAG structure, incorporating data loading, preprocessing, model training, and email notification upon successful completion.

Key Modifications from the Original Template

Compared to the base lab structure provided in the course repository, the following modifications were implemented:

Execution Mode: Used airflow standalone instead of running separate webserver and scheduler instances in multiple terminals.

Dataset Change: Replaced the sample dataset with the Pima Indians Diabetes dataset (diabetes.csv) containing 768 samples and 8 features.

Model Change: Implemented a Random Forest Classifier with 100 estimators and a maximum depth of 10, replacing the placeholder model used in the original template.

Pipeline Customization: Defined a five-step DAG to automate data loading, preprocessing, splitting, model training, and email notification.

Email Notification: Added a Python-based email function that triggers upon successful DAG completion (success_email.py).

Simplified Deployment: Used Airflow’s standalone mode to manage all services within a single process for easier execution and testing.

Environment Setup (Standalone Airflow on VM)
1. Create and Configure a VM

Launch a virtual machine (minimum 2 vCPUs, 4 GB RAM).

Allow inbound connections on port 8080 to access the Airflow web interface.

2. Install Dependencies
sudo apt update
sudo apt install python3-pip python3-venv -y

3. Set Up Virtual Environment
python3 -m venv airflow_venv
source airflow_venv/bin/activate
pip install apache-airflow

4. Initialize and Start Airflow in Standalone Mode
airflow standalone


This command initializes the database, creates a default admin user, and starts both the webserver and scheduler automatically.
Access the web interface at:
http://<VM-IP>:8080

Admin credentials are stored in:

~/airflow/standalone_admin_password.txt

Project Folder Structure
airflow-diabetes-lab/
│
├── dags/
│   ├── my_dag.py                    # Main Airflow DAG definition
│   ├── data/
│   │   └── diabetes.csv             # Dataset used in the pipeline
│   └── src/
│       ├── model_development.py     # Random Forest model training script
│       └── success_email.py         # Email notification function
│
├── screenshots/
│   ├── 01_dag_run_success.png
│   ├── 02_load_data_task_log.png
│   ├── 03_data_preprocessing_task_log.png
│   ├── 04_separate_outputs_task_log.png
│   └── 05_build_model_task_log.png
│
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation

DAG Workflow Description

The Directed Acyclic Graph (DAG) in this lab consists of five Python-based tasks that execute sequentially to complete the machine learning workflow.

The process begins with load_data_task, which reads the diabetes dataset into memory and verifies its shape and structure.
Next, data_preprocessing_task performs basic data cleaning, handles missing values if present, and splits the dataset into training and test sets using a 70/30 ratio.

Following preprocessing, separate_data_outputs_task manages the organization and saving of the preprocessed data to disk, ensuring the next stage can access the correct input files.
The build_save_model_task then trains a Random Forest classifier using the training data, evaluates its accuracy (approximately 0.74 on the test set), and saves the trained model as a .pkl file.

Finally, the task_send_email serves as a notification task that triggers only upon successful completion of all previous tasks, confirming that the workflow ran end-to-end without errors.

Execution Process

Place the project folder (airflow-diabetes-lab/) inside your VM’s Airflow directory (~/airflow).

Run Airflow in standalone mode:

airflow standalone


Access the web interface at http://<VM-IP>:8080.

Locate and enable the DAG named:

Airflow_Lab3_Diabetes_RandomForest


Trigger the DAG manually or schedule it.

Monitor execution using the Graph View or Grid View.

Results Summary

All five tasks executed successfully in sequence.

The trained Random Forest model achieved an accuracy of approximately 0.74.

Execution completed with no task dependency errors.

Email notification successfully triggered after DAG completion.

Visual proof of execution and logs are available in the screenshots/ folder.

Requirements

Install dependencies with:

pip install -r requirements.txt


Typical contents include:

apache-airflow
pandas
scikit-learn
joblib

Lab Submission Details

Submitted Lab: Airflow Diabetes Prediction using Random Forest
Execution Mode: Airflow Standalone on VM
Submission Format: GitHub Repository
Repository Link: https://github.com/sharonjennifer/airflow-diabetes-lab

Author: Sharon Jennifer Justin Devaraj
