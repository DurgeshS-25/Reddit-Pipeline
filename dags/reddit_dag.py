import os 
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline  # Import is correct

# Adjusting sys.path to include parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Default arguments for the DAG
default_args = {
    'owner': 'Durgesh Sakhardande',
    'start_date': datetime(2025, 1, 13),
}

# File postfix for dynamic naming
file_postfix = datetime.now().strftime("%Y%m%d")

# Define the DAG
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline'],
)

# Task: Extraction from Reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,  # Callable function
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100,
    },
    dag=dag,
)


#UPLOADING IT TO S3

upload_s3 = PythonOperator(
  task_id = 's3_upload',
  python_callable= upload_s3_pipeline,
  dag = dag 
)

extract >> upload_s3