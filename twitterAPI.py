from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import json
import pandas as pd


import twitter_credentials
# # # # TWITTER AUTHENTICATOR # # # # 
# class TwitterAuthenticator():
# 	def authenticate_twitter_app(self):
# 		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
# 		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
# 		return auth

class TwitterStreamer():
	"""
	Class for streaming and processing live tweets.
	"""
	def __init__(self):
		pass

	def stream_tweets(self, fetched_tweets_filename):
		listener = TwitterListener(fetched_tweets_filename)
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		
		stream = Stream(auth, listener)
		stream.sample()

class TwitterListener(StreamListener):
	"""
	This is a basic listener class that just prints received tweets to stdout
	"""
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename

	def on_data(self, data):
		try:
			tweet = json.loads(data)
			user_ids = tweet["user"]
			if not tweet['retweeted'] and 'RT @' not in tweet['text'] and tweet['lang'] == 'en':
				with open(self.fetched_tweets_filename, 'a') as tf:
					tf.write(data)
				print("Added")
			return True
		except BaseException as e:
			if (str(e) == '\'user\''):
				print("OK")
			else:
				print("Error on data: %s" % str(e))
		return True

	def on_error(self, status):
		if status == 420:
			return False
		print(status)

if __name__ == "__main__":
	fetched_tweets_filename = "tweets.json"
	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename)

