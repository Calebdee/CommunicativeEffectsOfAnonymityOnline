import tweepy
import twitter_credentials

stream = tweepy.Stream(
  twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET,
  twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET
)

stream.sample()

stream.on_data(data):
    print(data)