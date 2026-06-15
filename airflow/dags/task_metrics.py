from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta, UTC

from analytics.etl.pipeline import run_pipeline


default_args = {
    "owner": "data-engineering",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="task_metrics_etl",
    description="Create task analytics metrics",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "analytics"],
) as dag:
    
    run_task_metrics_etl = PythonOperator(
        task_id="run_metrics_etl",
        python_callable=run_pipeline
    )

    run_task_metrics_etl