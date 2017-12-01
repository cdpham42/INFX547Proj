# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:39:48 2017

@author: Casey
"""

#%%

import tweepy
import json

#%% NOTES

"""

Hashtags

Restricting JSON to:
    Text
    Retweets
    Favorites
    Location
    @ reply
    date
    
    user:
        profile background color

"""

#%% Constants

get_count = 200

maxTweets = 10000
    

#%% Get Tweets

def getTweets(user, filename, api):
    
    max_id = -1
    sinceId = None
    
    tweet_count = 0
    
    print("Downloading at least {} tweets".format(maxTweets))
    
    with open(filename,"w+") as f:
        print("Opened " + filename)
#        
#        data = json.load(f)
#        
#        if len(data) > 0:
#        
#            last_tweet = data[-1]
#            max_id = last_tweet["id"]
        
        while tweet_count <= maxTweets:
            
            try:
                
                if(max_id <= 0):
                    if(not sinceId):
                        new_tweets = api.user_timeline(screen_name = user, 
                                                       count = get_count)
                        print("Got new tweets")
                    else:
                        new_tweets = api.user_timeline(screen_name = user, 
                                                       count = get_count, 
                                                       since_id = sinceId)
                        print("Got new tweets since ", sinceId)
                else:
                    if(not sinceId):
                        new_tweets = api.user_timeline(screen_name = user, 
                                                       count = get_count, 
                                                       max_id = str(max_id-1))
                        print("Got new tweets up to ", max_id)
                    else:
                        new_tweets = api.user_timeline(screen_name = user, 
                                                       count = get_count, 
                                                       max_id = str(max_id-1), 
                                                       since_id = sinceId)
                        print("Got new tweets up to ", max_id, " since ", sinceId)
                
                if not new_tweets:
                    print('no more tweets found')
                    break
                		
                for tweet in new_tweets:
                    json.dump(tweet._json, f, indent = 4, sort_keys = True)
                    f.write('\n')
#                    print("Wrote tweets")
                
                
                tweet_count += len(new_tweets)
                print(tweet_count)
                
                max_id = new_tweets[-1].id
                    
            except tweepy.TweepError as e:
                print('some error : ' + str(e))
                break
            
        print("Reached max tweets")
            
            
#%% Search Tweets

def searchTweets(query, filename, api):
    
    max_id = -1
    sinceId = None
    
    tweet_count = 0
    
    print("Downloading at least {} tweets".format(maxTweets))
    
    with open(filename,"w+") as f:
        
#        data = json.load(f)
#        
#        if len(data) > 0:
#        
#            last_tweet = data[-1]
#            max_id = last_tweet["id"]
        
        print("Opened " + filename)
        
        while tweet_count <= maxTweets:
            
            try:
                
                if(max_id <= 0):
                    if(not sinceId):
                        new_tweets = api.search(q = query, 
                                                       count = get_count)
                        print("Got new tweets")
                    else:
                        new_tweets = api.search(q = query, 
                                                       count = get_count, 
                                                       since_id = sinceId)
                        print("Got new tweets since ", sinceId)
                else:
                    if(not sinceId):
                        new_tweets = api.search(q = query, 
                                                       count = get_count, 
                                                       max_id = str(max_id-1))
                        print("Got new tweets up to ", max_id)
                    else:
                        new_tweets = api.search(q = query, 
                                                       count = get_count, 
                                                       max_id = str(max_id-1), 
                                                       since_id = sinceId)
                        print("Got new tweets up to ", max_id, " since ", sinceId)
                
                if not new_tweets:
                    print('no more tweets found')
                    break
                		
                for tweet in new_tweets:
                    json.dump(tweet._json, f, indent = 4, sort_keys = True)
                    f.write('\n')
#                    print("Wrote tweets")
                
                
                tweet_count += len(new_tweets)
                print(tweet_count)
                
                max_id = new_tweets[-1].id
                    
            except tweepy.TweepError as e:
                print('some error : ' + str(e))
                break
            
        print("Reached max tweets")
