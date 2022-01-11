from twitter_bot.oauth_handler import api

#get last 20 entries in my timeline. 20 is default
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
    
#post a tweet saying literally Hello
# tweet = api.update_status("Hello")

#get the user, details and last followers
# user = api.get_user(screen_name="realpython")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

#follow someone
# api.create_friendship(screen_name="ThePSF")

#update profile description
# api.update_profile(description="")

#like the most recent tweet in my home timeline
# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)

#get all blocked users
# for block in api.get_blocks():
#     print(block.name)

#get the 10 most recent tweets that are in english and contain the word "Python"
# for tweet in api.search_tweets(q="Python", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")

#get the world wide trending topics
# trends_result = api.get_place_trends(1)
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])

#get all twwets in which you are mentioned, like the tweet and follow the author
# tweets = api.mentions_timeline()
# for tweet in tweets:
#     tweet.favorite()
#     tweet.user.follow()

#using cursor to get the last 100 tweets from your timeline
# for tweet in tweepy.Cursor(api.home_timeline).items(100):
#     print(f"{tweet.user.name} said: {tweet.text}")