from reddit_calls import *
from user_definition import *

def _download_reddit_data():
    """
    Create reddit instance and collect data to write to gcs as two csv's,
    one for posts, and the other for comments on those posts.
    """
    reddit = praw_setup(client_id, client_secret, user_agent, password, username)
    blob_name_posts = f'{yesterday}/posts.csv' # names for the files
    blob_name_comments = f'{yesterday}/comments.csv'
    
    df_posts = get_post_titles_and_features(reddit, post_limit=100, timeframe='day', one_sub=False, sub=None)
    df_comments = get_comments_and_features(reddit, post_limit=100, timeframe='day', one_sub=False, sub=None)