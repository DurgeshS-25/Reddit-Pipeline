from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    # Corrected `xcom_pull` method: use `task_ids`
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    if not file_path:
        raise ValueError("No file path was returned from the 'reddit_extraction' task.")

    # Connect to S3
    s3 = connect_to_s3()
    
    # Ensure the bucket exists
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    
    # Extract filename from the path
    s3_file_name = file_path.split('/')[-1]
    
    # Upload file to S3
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, s3_file_name)
