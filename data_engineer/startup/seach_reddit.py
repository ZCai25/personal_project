import praw
import re

# Authenticate with Reddit API
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent',
                     username='your_username',
                     password='your_password')

# Specify the subreddit
subreddit = reddit.subreddit('your_subreddit')

# Compile the regex pattern
pattern = re.compile(r'\b\d+d\d+\b')

# Search for comments containing the regex pattern
comments = subreddit.search(pattern, sort='new', limit=1000)

# Loop through each comment and extract the regex match
for comment in comments:
    matches = re.findall(pattern, comment.body)
    if matches:
        print(matches)
