from etls.reddit_etl import extract_posts, transform_data,load_data_to_csv
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
from etls.reddit_etl import connect_reddit 
import pandas as pd


def reddit_pipeline (file_name: str, subreddit: str, time_filter='day', limit = None):
  #connecting to reddit instance
  instance = connect_reddit(CLIENT_ID, SECRET, 'Red_pipeline')
  #extraction 
  posts = extract_posts(instance, subreddit, time_filter, limit)
  post_df = pd.DataFrame(posts)
  #transformation
  post_df = transform_data(post_df)
  #loadng to csv
  file_path = f'{OUTPUT_PATH}/{file_name}.csv'
  load_data_to_csv(post_df,file_path)

  return file_path