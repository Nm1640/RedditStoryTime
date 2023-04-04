import praw
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config.get('default', 'client_id')
client_secret = config.get('default', 'client_secret')
user_agent = config.get('default', 'user_agent')

# Initialize the Reddit API
reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent,
                    config_interpolation=None)


subreddit_name = random.choice(['2007scape'])

subreddit = reddit.subreddit(subreddit_name)
random_post = random.choice(list(subreddit.hot()))

print(f'SubReddit: {subreddit_name}')
print("Title: ", random_post.title)
print("Body: ", random_post.selftext)
print(f'Score {random_post.score}')
print(random_post.url)

comment_forest = random_post.comments

count = 0
for comment in comment_forest:
    print()
    print(f'[{comment.score}] {comment.body}')
    count += 1
    if count > 10:
        break
