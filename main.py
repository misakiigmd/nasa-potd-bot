import tweepy

# Import our Twitter credentials from credentials.json
import json
with open("credentials.json", "r") as file:
    creds = json.load(file)

# Authenticate to Twitter 
client = tweepy.Client(creds["BEARER_TOKEN"], creds["API_KEY"], creds["API_SECRET"], creds["ACCESS_TOKEN"], creds["ACCESS_TOKEN_SECRET"])
auth = tweepy.OAuth1UserHandler(creds["API_KEY"], creds["API_SECRET"], creds["ACCESS_TOKEN"], creds["ACCESS_TOKEN_SECRET"])	

# Create API object
api = tweepy.API(auth)

# Create a tweet
client.create_tweet(text="Hello, world!")