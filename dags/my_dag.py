import sys
from pathlib import Path

dag_folder = Path(__file__).parent
sys.path.insert(0, str(dag_folder))

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from src.model_development import load_data, build_model, data_preprocessing, separate_data_outputs
from src.success_email import send_success_email

default_args = {
    'owner': 'Jennifer Sharon - Diabetes Dataset with Random Forest',
    'start_date': datetime(2025, 10, 6),
    'retries': 0
}

dag = DAG(
    'Airflow_Lab3_Diabetes_RandomForest',
    default_args=default_args,
    description='ML Pipeline: Diabetes prediction using Random Forest',
    catchup=False,
    tags=['diabetes', 'random-forest', 'machine-learning']
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag
)

data_preprocessing_task = PythonOperator(
    task_id='data_preprocessing_task',
    python_callable=data_preprocessing,
    op_args=[None],
    dag=dag
)

separate_data_outputs_task = PythonOperator(
    task_id='separate_data_outputs_task',
    python_callable=separate_data_outputs,
    dag=dag
)

build_save_model_task = PythonOperator(
    task_id='build_save_model_task',
    python_callable=build_model,
    op_args=["diabetes_random_forest_model.pkl"],
    dag=dag
)

task_send_email = PythonOperator(
    task_id='task_send_email',
    python_callable=send_success_email,
    dag=dag,
)

load_data_task >> data_preprocessing_task >> separate_data_outputs_task >> build_save_model_task >> task_send_email
