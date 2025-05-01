from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from ingest import ingest_data
from transform import transform_data
from model import run_model


default_args = {
    'owner': 'nisha',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer_analytics_pipeline',
    default_args=default_args,
    description='Customer analytics pipeline with PostgreSQL and Python',
    schedule_interval=timedelta(days=1),
)

ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

model_task = PythonOperator(
    task_id='run_model',
    python_callable=run_model,
    dag=dag,
)

ingest_task >> transform_task >> model_task
