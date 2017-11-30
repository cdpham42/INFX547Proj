"""

Author: Tiffany Chiu

Exploratory Analysis

Analyzes tweet data from CSV files, determining number of favorites, tweets, 
retweets, etc.

"""

import csv

rows = []

keys = {}

with open('Glossier_Tweets_All.csv', 'rb') as f:
	reader = csv.reader(f)

	# first row of the csv file is the column names
	column_names = reader.next()
	print("Column names: " + str(column_names))

	# map keys to their indices to make easier to access their values in other rows
	for i in range(0, len(column_names)):
		keys[column_names[i]] = i

	# keys: {'username': 0, 'permalink': 9, 'text': 4, 'hashtags': 7, 
	#        'retweets': 2, 'favorites': 3, 'date': 1, 'mentions': 6, 
	#        'geo': 5, 'id': 8}

	for row in reader:
		# validate all keys exist in the rows
		if len(row) == 10:

			# convert hashtags string into a list of the hashtags without the # sign
			# for example:
			# "#glossier #balance #regram" becomes the list ['glossier', 'balance', 'regram']
			if row[keys['hashtags']] != '':
				hashtags_list = row[keys['hashtags']].split(' ')
				hashtags_list_without_pound_sign = list()
				for hashtag in hashtags_list:
					hashtags_list_without_pound_sign.append(hashtag[1:].lower()) #convert to lower to make analysis easier
				row[keys['hashtags']] = hashtags_list_without_pound_sign
			else:
				row[keys['hashtags']] = list()

			rows.append(row)
	


# number of tweets
print("Number of Tweets :" + str(len(rows)))


# favorites
total_favorite_count = 0
total_number_of_tweets = len(rows)

for row in rows:
	total_favorite_count += int(row[keys["favorites"]])

print("Number of favorites :" + str(total_favorite_count))

avg_favorites = 1.0*total_favorite_count/total_number_of_tweets
print("Average number of favorites that each tweet gets: " + str(avg_favorites))


# max favorite count and tweeter
max_fave_list = []
max_fave_so_far = 0
tweet_with_max_fave = None

for row in rows:
	current_tweet_favorite_count = int(row[keys["favorites"]])
	if current_tweet_favorite_count > max_fave_so_far:
		max_fave_so_far = current_tweet_favorite_count
		tweet_with_max_fave = row

print("Max fave for a tweet: " + str(max_fave_so_far))
print("Tweet with most faves: ")
print(tweet_with_max_fave)


# retweets
total_retweet_count = 0

for row in rows:
	total_retweet_count += int(row[keys["retweets"]])

print("Number of retweets: " + str(total_retweet_count))

avg_retweets = 1.0*total_retweet_count/total_number_of_tweets
print("Average number of retweets that each tweet gets: " + str(avg_retweets))


# max retweet count and tweeter
max_retweet_list = []
max_retweet_so_far = 0
tweet_with_max_retweet = None

for row in rows:
	current_tweet_retweet_count = int(row[keys["retweets"]])
	if current_tweet_retweet_count > max_retweet_so_far:
		max_retweet_so_far = current_tweet_retweet_count
		tweet_with_max_retweet = row

print("Max retweet for a tweet: " + str(max_retweet_so_far))
print("Tweet with most retweets: ")
print(tweet_with_max_retweet)


# print first 5 rows
for i in range(0,5):
	print(rows[i])

# unique hashtags
hashtags_count = {}

for row in rows:
	hashtags = row[keys["hashtags"]]
	for hashtag in hashtags:
		if hashtag in hashtags_count:
			hashtags_count[hashtag] += 1 # already saw this hashtag before, increase the count
		else:
			hashtags_count[hashtag] = 1 # new unique hashtag, add to the dict


print(sorted(hashtags_count.items(), key=lambda x:x[1], reverse=True))



# boybrow
bbrow_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["boybrow", "boy brow"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			bbrow_count += 1

print("Total boybrow count: " + str(bbrow_count))


# balmdotcom
bdc_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["balmdotcom", "balm dot com", "balm dotcom"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			bdc_count += 1

print("Total balm dot com count: " + str(bdc_count))


# milkjelly
mjelly_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["milkjellycleanser", "milkjelly cleanser", "milk jelly cleanser", "milk jelly"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			mjelly_count += 1

print("Total milk jelly cleanser count: " + str(mjelly_count))


# megagreensgalaxy
mega_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["mega greens", "mega green", "megagreens", "megagreen", "mega greens galaxy", "megagreens galaxy", "mega green galaxy", "megagreen galaxy"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			mega_count += 1

print("Total Mega Greens Galaxy count: " + str(mega_count))


# stretchconcealer
stretch_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["stretchconcealer", "stretch concealer", "stretch concealers"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			stretch_count += 1

print("Total stretch conceler count: " + str(stretch_count))


# cloudpaint
cloud_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["cloudpaint", "cloudpaints", "cloud paint", "cloud paints"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			cloud_count += 1

print("Total cloud paint count: " + str(cloud_count))


# primingmoisturiser
prime_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["primingmoisturiser", "primingmoisturizer", "priming moisturiser", "priming moisturizer"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			prime_count += 1

print("Total priming moisturiser rich count: " + str(prime_count))

# emilyweiss
weiss_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["emilyweiss", "emily weiss"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			weiss_count += 1

print("Total emily weiss count: " + str(weiss_count))


# perfume
perf_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["perfume"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			perf_count += 1

print("Total perfume count: " + str(perf_count))


# skincare
skin_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["skin care", "skincare"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			skin_count += 1

print("Total skincare count: " + str(skin_count))


# makeup
makeup_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["makeup", "make up"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			makeup_count += 1

print("Total makeup count: " + str(makeup_count))


# beauty
beaut_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["beauty"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			beaut_count += 1

print("Total beauty count: " + str(beaut_count))


# beautiful
beautiful_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["beautiful"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			beautiful_count += 1

print("Total beautiful count: " + str(beautiful_count))


# pink
pink_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["pink", "glossierpink", "glossier pink"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			pink_count += 1

print("Total pink count: " + str(pink_count))

# coolgirl
cool_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["cool", "coolgirl", "cool girl"]
	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			cool_count += 1

print("Total coolgirl count: " + str(cool_count))


# naturalgirl
natural_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["natural", "naturalgirl", "natural girl"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			natural_count += 1

print("Total naturalgirl count: " + str(natural_count))


# chicgirl
chic_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["chic", "chicgirl", "chic girl"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			chic_count += 1

print("Total chic_girl count: " + str(chic_count))


# realgirl
real_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["realgirl", "real girl"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			real_count += 1
			
print("Total real_girl count: " + str(real_count))


# bff
bff_count = 0

for row in rows:
	tweet_text = row[keys['text']].lower()
	hashtag_list = row[keys['hashtags']]

	strings_to_search_for = ["bff", "bestfriend", "best friend", "bestfriends", "best friends"]

	for string in strings_to_search_for:
		if string in tweet_text or string in hashtag_list:
			bff_count += 1

print("Total bff count: " + str(bff_count))






