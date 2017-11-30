import json
import operator 
from collections import Counter

file = open('Search_glossier.json', 'r')

json_objects = []

for line in file:
	while True:
		try:
			json_obj = json.loads(line)
			break
		except ValueError:
			# Not yet a complete JSON value
			try:
				line += next(file)
			except StopIteration:
				print("reached end of file")
				break
	json_objects.append(json_obj)

# number of tweets
print(str(len(json_objects)))

# number of faves
total_favorite_count = 0
total_number_of_tweets = len(json_objects)

for obj in json_objects:
	if "favorite_count" in obj.keys():
		total_favorite_count += obj["favorite_count"]

print("Total number of favorites for all tweets combined: " + str(total_favorite_count))

avg_favorites = 1.0*total_favorite_count/total_number_of_tweets
print("Average number of favorites that each tweet gets: " + str(avg_favorites))

print("Other dict keys you can use to analytize the data:")
print(json_objects[0].keys())

# max favorite count and tweeter
max_fave_list = []
max_fave_so_far = 0
tweet_with_max_fave = None

for obj in json_objects:
	if "favorite_count" in obj.keys():
		current_tweet_favorite_count = obj["favorite_count"]
		if current_tweet_favorite_count > max_fave_so_far:
			max_fave_so_far = current_tweet_favorite_count
			tweet_with_max_fave = obj

print("Max fave for a tweet: " + str(max_fave_so_far))
print("Tweet with most faves: ")
print(tweet_with_max_fave)

# number of retweets
total_retweet_count = 0

for obj in json_objects:
	if "retweet_count" in obj.keys():
		total_retweet_count += obj["retweet_count"]

print("Total number of retweets combined: " + str(total_retweet_count))

avg_retweets = 1.0*total_retweet_count/total_number_of_tweets
print("Average number of retweets that each tweet gets: " + str(avg_retweets))

# max retweet count and tweeter
max_retweet_list = []
max_retweet_so_far = 0
tweet_with_max_retweet = None

for obj in json_objects:
	if "retweet_count" in obj.keys():
		current_tweet_retweet_count = obj["retweet_count"]
		if current_tweet_retweet_count > max_retweet_so_far:
			max_retweet_so_far = current_tweet_retweet_count
			tweet_with_max_retweet = obj
		

print("Max retweet for a tweet: " + str(max_retweet_so_far))
print("Tweet that got the most retweets: ")
print(tweet_with_max_retweet)

# read text
text_list = []

for obj in json_objects:
	if "text" in obj.keys():
		text = obj["text"]
		text_list.append(text)

print(text_list)

# created at (date)
date_list = []

for obj in json_objects:
	if "created_at" in obj.keys():
		date = obj["created_at"]
		date_list.append(date)

print("Dates :" + str(date_list))







