from dotenv import load_dotenv
import os

load_dotenv()
twitter_api_key=os.getenv("twitter_api_key")
twitter_api_key_secret=os.getenv("twitter_api_key_secret")
twitter_bearer_token=os.getenv("twitter_bearer_token")
twitter_access_token=os.getenv("twitter_access_token")
twitter_token_secret=os.getenv("twitter_token_secret")