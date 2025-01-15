import praw
from praw import Reddit
import sys
import pandas as pd
import numpy as np
import logging
import os 

from utils.constants import POST_FIELDS


def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        logging.info('Connected to Reddit')
        return reddit
    except Exception as e:
        logging.error(f"Error connecting to Reddit: {e}")
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit_instance = reddit_instance.subreddit(subreddit)
    posts = subreddit_instance.top(time_filter=time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        # Safely handle missing fields
        post_data = {key: post_dict.get(key, None) for key in POST_FIELDS}
        post_lists.append(post_data)
    
    logging.info(f"Extracted {len(post_lists)} posts from subreddit '{subreddit}'")
    return post_lists


def transform_data(post_df: pd.DataFrame):
    try:
        # Convert 'created_utc' to datetime safely
        post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s', errors='coerce')

        # Handle boolean fields with defaults
        post_df['over_18'] = post_df['over_18'].fillna(False).astype(bool)
        post_df['edited'] = post_df['edited'].apply(lambda x: x if isinstance(x, bool) else False)

        # Handle numeric fields with defaults or remove invalid rows
        post_df['num_comments'] = pd.to_numeric(post_df['num_comments'], errors='coerce').fillna(0).astype(int)
        post_df['score'] = pd.to_numeric(post_df['score'], errors='coerce').fillna(0).astype(int)
        
        # Ensure text fields are strings
        post_df['title'] = post_df['title'].fillna('').astype(str)

        logging.info("Data transformation complete")
        return post_df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise


def load_data_to_csv(data: pd.DataFrame, path: str):
    dir_name = os.path.dirname(path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)  # Create the directory if it doesn't exist
    
    try:
        data.to_csv(path, index=False)
        logging.info(f"Data successfully saved to {path}")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
