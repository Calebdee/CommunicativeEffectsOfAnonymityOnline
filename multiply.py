from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import json
import pandas as pd
import csv


import twitter_credentials
# # # # TWITTER AUTHENTICATOR # # # # 
# class TwitterAuthenticator():
# 	def authenticate_twitter_app(self):
# 		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
# 		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
# 		return auth

class tweetRow:
	ids = 0
	name = ""
	classification = ""

	def __init__(self, var1, var2, var3):
		self.ids = var1
		self.name = var2
		self.classification = var3

class TwitterStreamer():

	
	"""
	Class for streaming and processing live tweets.
	"""
	def __init__(self):
		pass

	def stream_tweets(self, OUTPUT_FILE):
		listener = TwitterListener(fetched_tweets_filename)
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		
		READ_DATA = "highly_anon.csv"
		inData = []
		with open(READ_DATA, 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				inData.append(tweetRow(row[0], row[1], row[2]))

		print(len(inData))

		# stream = Stream(auth, listener)
		# stream.sample()
		api = tweepy.API(auth, wait_on_rate_limit = True)
		tweet_list = []
		count = 1
		setNum = 685
		for account in inData:
			print(count)
			count += 1

			if (count % 50 == 0):
				with open(OUTPUT_FILE + str(setNum) + ".json", mode='w', encoding='utf-8') as output_file:
					json.dump(tweet_list, output_file, indent=4)
				tweet_list = []
				print(OUTPUT_FILE + str(setNum) + ".json")
				setNum += 1

			try:
				search = api.user_timeline(user_id = account.ids, count = 25, include_rts = False)
				newTweet = dict()
				# for key,value in search[0].__dict__.items():
				# 	print(key)
				for tweet in search:
					newTweet = dict()
					newTweet['id'] = tweet.id
					newTweet['user_id'] = tweet.user.id
					newTweet['text'] = tweet.text
					newTweet['classifier'] = account.name
					newTweet['classification'] = account.classification
					tweet_list.append(newTweet)
			except tweepy.TweepError as e:
					print("Failed to run, skipping...")
					print(e)  # prints 34
		


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
	fetched_tweets_filename = "multiply"
	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename)

