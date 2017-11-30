import json
import operator 
from collections import Counter

file = open('Glossier_tweets.json', 'r')

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
print("Number of Tweets :" + str(len(json_objects)))

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

# unique lang
lang_list = []

for obj in json_objects:
	if "lang" in obj.keys():
		lang = obj["lang"]
		if lang not in lang_list:
			lang_list.append(lang)

#print("Languages :" + str(lang_list))

# unique geo
place_list = []

for obj in json_objects:
	if "place" in obj.keys():
		place = obj["place"]
		if place not in place_list:
			place_list.append(place)

#print("Location :" + str(place_list))

# unique hashtags
hashtag_list = []

for obj in json_objects:
	if "text" in obj.keys() and "#" in obj["text"]:
		tag = obj["text"]
		hashtag_list.append(tag)

print("Hashtags :" + str(hashtag_list))

#print("Location :" + str(place_list))

# search for first 10 text
text_list = []

for obj in json_objects:
	if "text" in obj.keys():
		text = obj["text"]
		text_list.append(text)

#print("Number of text strings :" + str(len(text_list)))
#print(text_list[1:35])

# boybrow
bbrow_count = 0

for obj in json_objects:
	if "text" in obj.keys() and "boy brow" in obj["text"]:
		bbrow_count += 1

print("Total boy brow count: " + str(bbrow_count))

# balmdotcom
bdc_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("balmdotcom" in obj["text"].lower() or "balm dot com" in obj["text"].lower() or "balm dotcom" in obj["text"].lower()):
		bdc_count += 1

print("Total balm dot com count: " + str(bdc_count))

# milkjelly
mjelly_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("milkjellycleanser" in obj["text"].lower() or "milkjelly cleanser" in obj["text"].lower() or "milk jelly cleanser" in obj["text"].lower() or "milk jelly" in obj["text"].lower()):
		mjelly_count += 1

print("Total milk jelly cleanser count: " + str(mjelly_count))

# megagreensgalaxy
mega_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("mega greens" in obj["text"].lower() or "mega greens galaxy" in obj["text"].lower() or "megagreens" in obj["text"].lower()):
		mega_count += 1

print("Total Mega Greens Galaxy count: " + str(mega_count))

# stretchconcealer
stretch_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("stretchconcealer" in obj["text"].lower() or "stretch concealer" in obj["text"].lower() or "stretch concealers" in obj["text"].lower()):
		stretch_count += 1

print("Total stretch conceler count: " + str(stretch_count))

# cloudpaint
cloud_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("cloudpaint" in obj["text"].lower() or "cloudpaints" in obj["text"].lower() or "cloud paint" in obj["text"].lower() or "cloud paints" in obj["text"].lower()):
		cloud_count += 1

print("Total cloud paint count: " + str(cloud_count))

# primingmoisturiser
prime_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("primingmoisturiser" in obj["text"].lower() or "primingmoisturizer" in obj["text"].lower() or "priming moisturiser" in obj["text"].lower() or "priming moisturizer" in obj["text"].lower()):
		prime_count += 1

print("Total priming moisturiser rich count: " + str(prime_count))

# emilyweiss
weiss_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("emilyweiss" in obj["text"].lower() or "emily weiss" in obj["text"].lower()):
		weiss_count += 1

print("Total emily weiss count: " + str(weiss_count))

# perfume
perf_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("perfume" in obj["text"].lower()):
		perf_count += 1

print("Total perfume count: " + str(perf_count))

# skincare
skin_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("skin care" in obj["text"].lower() or "skincare" in obj["text"].lower()):
		skin_count += 1

print("Total skincare count: " + str(skin_count))

# makeup
makeup_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("makeup" in obj["text"].lower() or "make up" in obj["text"].lower()):
		makeup_count += 1

print("Total makeup count: " + str(makeup_count))

# beauty
beaut_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("beauty" in obj["text"].lower()):
		beaut_count += 1

print("Total beauty count: " + str(beaut_count))

# beautiful
beautiful_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("beautiful" in obj["text"].lower()):
		beautiful_count += 1

print("Total beautiful count: " + str(beautiful_count))

# pink
pink_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("pink" in obj["text"].lower() or "glossierpink" in obj["text"].lower() or "glossier pink" in obj["text"].lower()):
		pink_count += 1

print("Total pink count: " + str(pink_count))

# coolgirl
cool_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("cool" in obj["text"].lower() or "coolgirl" in obj["text"].lower() or "cool girl" in obj["text"].lower()):
		cool_count += 1

print("Total coolgirl count: " + str(cool_count))

# chicgirl
chic_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("chic" in obj["text"].lower() or "chicgirl" in obj["text"].lower() or "chic girl" in obj["text"].lower()):
		chic_count += 1

print("Total chic_girl count: " + str(chic_count))

# naturalgirl
natural_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("natural" in obj["text"].lower() or "naturalgirl" in obj["text"].lower() or "natural girl" in obj["text"].lower()):
		natural_count += 1

print("Total naturalgirl count: " + str(natural_count))

# bff
bff_count = 0

for obj in json_objects:
	if "text" in obj.keys() and ("bff" in obj["text"].lower() or "best friend" in obj["text"].lower() or "best friends" in obj["text"].lower() or "bestfriends" in obj["text"].lower()):
		bff_count += 1

print("Total bff count: " + str(bff_count))
























