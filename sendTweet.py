# import the tweepy library
import tweepy

# import the config file
from config import *

# create client with tweepy.Client with API key, API secret key, Access token, Access token secret

client = tweepy.Client(
    consumer_key = API_KEY,
    consumer_secret = API_SECRET_KEY,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
)

# create a variable called tweet with a string that says 'I wrote this tweet with Copilot

tweet2 = 'Tweeting from VS Code'

# send tweet with client.create_tweet method and text as argument. Save the result in a variable called response

response = client.create_tweet(text=tweet2)

print(response)
