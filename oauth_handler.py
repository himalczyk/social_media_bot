import tweepy
from config import *
import logging

# Create API object

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
    auth.set_access_token(twitter_access_token, twitter_token_secret)
    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
    except Exception as e:
        logging.logger.error("Error creating API", exc_info=True)
        raise e
    logging.logger.info("API CREATED")
    return api