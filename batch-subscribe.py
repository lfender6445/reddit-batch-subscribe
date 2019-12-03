import praw
from os import environ, path
from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

reddit = praw.Reddit(
    user_agent='Python:batch-subscribe-v1:v1',
    client_id=environ.get('CLIENT_ID'),
    client_secret=environ.get('CLIENT_SECRET'),
    username=environ.get('USERNAME'),
    password=environ.get('PASSWORD')
)

with open('list.txt', 'r') as f:
    list = f.readlines()
    for subreddit in list:
        print('subscribing to', subreddit)
        reddit.subreddit(subreddit).subscribe()
