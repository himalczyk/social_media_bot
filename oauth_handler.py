import tweepy
from config import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
auth.set_access_token(twitter_access_token, twitter_token_secret)

# Create API object
# Setting wait_on_rate_limit and wait_on_rate_limit_notify to True makes the API object print a message and wait if the rate limit is exceeded:
api = tweepy.API(auth)