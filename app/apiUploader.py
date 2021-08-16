
"""
PUT YOUR TWITTER ACCOUNT KEYS HERE
"""
CONSUMER_KEY =""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def uploadTweet(persona, tweet, prompt):
    api.update_status("Prompt: " + prompt + "\n" + persona + ": " + tweet)
