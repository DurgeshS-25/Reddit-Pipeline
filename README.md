# Reddit Pipeline Project

## Overview
The Reddit Pipeline Project is an ETL (Extract, Transform, Load) pipeline designed to extract posts from Reddit, process them, and upload the resulting data to AWS S3. This pipeline is implemented using Apache Airflow and includes features such as data extraction, transformation, and storage.

## Features
- **Data Extraction**: Extracts Reddit posts from specified subreddits using the Reddit API.
- **Data Transformation**: Cleans and processes the data for better usability.
- **Data Storage**: Saves the transformed data locally and uploads it to an AWS S3 bucket.
- **Containerized Environment**: Uses Docker for easy deployment and reproducibility.

## Project Structure
```
Reddit-Pipeline/
├── .gitignore
├── Dockerfile
├── airflow.env
├── dags/
├── data/
├── docker-compose.yml
├── etls/
├── pipelines/
├── reddit/
├── requirements.txt
├── tests/
├── utils/
```
- **`dags/`**: Contains the Airflow DAGs.
- **`data/`**: Stores the locally saved CSV files.
- **`etls/`**: Contains ETL scripts.
- **`pipelines/`**: Holds scripts for handling data pipelines.
- **`utils/`**: Utility scripts and constants.

## Requirements
- Docker
- Python 3.9
- Apache Airflow 2.10.4
- AWS credentials for S3 access

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Reddit-Pipeline.git
    cd Reddit-Pipeline
    ```

2. Build and start the Docker containers:
    ```bash
    docker-compose up -d --build
    ```

3. Access the Airflow web interface at [http://localhost:8080](http://localhost:8080) and log in using the credentials defined in `airflow.env`.

## Usage
1. **Configure the Pipeline**:
   - Update `utils/constants.py` with your Reddit API credentials, AWS S3 bucket name, and output path.

2. **Trigger the DAG**:
   - Navigate to the Airflow web interface and trigger the `etl_reddit_pipeline` DAG.

3. **Data Output**:
   - Transformed data is saved locally in the `data/` directory.
   - The file is also uploaded to the specified AWS S3 bucket.

## Key Files
- **`dags/reddit_dag.py`**: Defines the Airflow DAG.
- **`etls/reddit_etl.py`**: Handles Reddit data extraction and transformation.
- **`pipelines/aws_s3_pipeline.py`**: Manages uploading files to AWS S3.
- **`docker-compose.yml`**: Sets up the Airflow environment.
- **`requirements.txt`**: Specifies Python dependencies.

## Troubleshooting
- **CSV Not Overwritten**:
  Ensure the `OUTPUT_PATH` in `utils/constants.py` points to the correct directory.

- **File Not Uploaded to S3**:
  Verify AWS credentials and ensure the S3 bucket exists.

- **Airflow Errors**:
  Check Airflow logs for detailed error messages:
  ```bash
  docker-compose logs -f
  ```

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and push to your branch:
    ```bash
    git add .
    git commit -m "Add new feature"
    git push origin feature-name
    ```
4. Open a pull request.

## Acknowledgments
- Apache Airflow for orchestrating the ETL pipeline.
- Reddit API for providing data access.
- AWS S3 for cloud storage.

