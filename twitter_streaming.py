import json
import tweepy
from oauth_handler import api

class programmingListener(tweepy.SteamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        
    def on_error(self, status):
        print("Error detected")
        
tweets_listener = programmingListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django"], languages=["en"])