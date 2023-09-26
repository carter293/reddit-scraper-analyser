import praw
import json
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Set up your Reddit API credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

subreddit_name = 'excel'

def main():
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def fetch_posts_from_subreddit(subreddit_name, limit=500):
        subreddit = reddit.subreddit(subreddit_name)
        
        # List to store each post and its comments
        data = []

        # Fetching the posts
        for post in subreddit.top(limit=limit,time_filter="year"):
            post_data = {
                'title': post.title,
                'content': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc' : post.created_utc,
            }
            data.append(post_data)
        
        return data

    # Fetch data
    subreddit_data = fetch_posts_from_subreddit(subreddit_name,500)

    # Generate a timestamp in the format YYYYMMDD_HHMMSS
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    # Append the timestamp to the filename
    filename = f'subreddit_data_{subreddit_name}_{timestamp}.json'

    # Save to a JSON file
    with open(filename, 'w') as outfile:
        json.dump(subreddit_data, outfile, indent=4)


if __name__ == "__main__":
    main()