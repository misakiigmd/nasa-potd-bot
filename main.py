import tweepy
import requests
import shutil

# Import our Twitter credentials from credentials.json
import json
with open("credentials.json", "r") as file:
    creds = json.load(file)

# Authenticate to Twitter 
client = tweepy.Client(creds["BEARER_TOKEN"], creds["API_KEY"], creds["API_SECRET"], creds["ACCESS_TOKEN"], creds["ACCESS_TOKEN_SECRET"])
auth = tweepy.OAuth1UserHandler(creds["API_KEY"], creds["API_SECRET"], creds["ACCESS_TOKEN"], creds["ACCESS_TOKEN_SECRET"])	

# Create API object
api = tweepy.API(auth)

# Get NASA Astronomy Picture of the Day from the API
r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={creds['NASA_API_KEY']}")
data = r.json()

img_url = data["hdurl"]
file_name = data["date"] + ".jpg"

res = requests.get(img_url, stream=True)
if res.status_code == 200:
    with open(file_name, "wb") as file:
        shutil.copyfileobj(res.raw, file)
    print("Image downloaded successfully.")
    shutil.move(file_name, "images/")
else:
    print("Image couldn't be retrieved.")