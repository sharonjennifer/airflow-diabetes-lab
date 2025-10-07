# Airflow Diabetes Prediction Lab — Standalone Deployment on VM

## Overview

This lab demonstrates the setup, configuration, and execution of **Apache Airflow** in a **Standalone environment** on a Virtual Machine (VM).  
The workflow automates a **machine learning pipeline** for predicting diabetes outcomes using the **Pima Indians Diabetes dataset** and a **Random Forest classifier**.  

The project follows the standard Airflow DAG structure, incorporating data loading, preprocessing, model training, and email notification upon successful completion.

---

## Key Modifications from the Original Template

Compared to the base lab structure provided in the course repository, the following modifications were implemented:

- **Execution Mode:** Used `airflow standalone` instead of running separate webserver and scheduler instances in multiple terminals.  
- **Dataset Change:** Replaced the sample dataset with the **Pima Indians Diabetes dataset** (`diabetes.csv`) containing 768 samples and 8 features.  
- **Model Change:** Implemented a **Random Forest Classifier** with 100 estimators and a maximum depth of 10, replacing the placeholder model used in the original template.  
- **Pipeline Customization:** Defined a five-step DAG to automate data loading, preprocessing, splitting, model training, and email notification.  
- **Email Notification:** Added a Python-based email function that triggers upon successful DAG completion (`success_email.py`).  
- **Simplified Deployment:** Used Airflow’s standalone mode to manage all services within a single process for easier execution and testing.

---

## Environment Setup (Standalone Airflow on VM)

### 1. Create and Configure a VM
- Launch a virtual machine (minimum **2 vCPUs**, **4 GB RAM**).
- Allow inbound connections on port **8080** to access the Airflow web interface.

### 2. Install Dependencies
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y

3. Set Up Virtual Environment
