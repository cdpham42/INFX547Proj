# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:13:51 2017

@author: Casey
"""

#%% Setup

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt
import numpy as np


path = "C:\\Users\Casey\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj\\Full Twitter Search"

os.chdir(path)

filenames = ["Glossier_Tweets_All.csv",
             "Hashtag_balmdotcom.csv",
             "Hashtag_boybrow.csv",
             "Hashtag_glossier.csv",
             "Hashtag_glossiergirl.csv",
             "Hashtag_glossierpink.csv",
             "Hashtag_nofilterjustglossier.csv"
             ]

#%% Load tweets

glossier_tweets = pd.read_csv(filenames[0])
balmdotcom = pd.read_csv(filenames[1])
boybrow = pd.read_csv(filenames[2])
glossier = pd.read_csv(filenames[3])
glossiergirl = pd.read_csv(filenames[4])
glossierpink = pd.read_csv(filenames[5])
nofilterjustlgossier = pd.read_csv(filenames[6])

glossier_tweets_text = pd.read_csv(filenames[0])['text'].dropna()
balmdotcom_text = pd.read_csv(filenames[1])['text'].dropna()
boybrow_text = pd.read_csv(filenames[2])['text'].dropna()
glossier_text = pd.read_csv(filenames[3])['text'].dropna()
glossiergirl_text = pd.read_csv(filenames[4])['text'].dropna()
glossierpink_text = pd.read_csv(filenames[5])['text'].dropna()
nofilterjustlgossier_text = pd.read_csv(filenames[6])['text'].dropna()

tweets = {"glossier_tweets": glossier_tweets_text,
          "balmdotcom": balmdotcom_text,
          "boybrow": boybrow_text,
          "glossier": glossier_text,
          "glossiergirl": glossiergirl_text,
          "glossierpink": glossierpink_text,
          "nofilterjustlgossier": nofilterjustlgossier_text
          }

#%% Get Polarity Scores

sia = SentimentIntensityAnalyzer()

glossier_tweets_sentiment = []

for tweet in glossier_tweets_text:
    ss = sia.polarity_scores(tweet)
    glossier_tweets_sentiment.append(ss)
    
glossier_tweets_sentiment = pd.DataFrame.from_dict(glossier_tweets_sentiment)

sentiment = {}

for key in tweets:
    result = []
    
    for tweet in tweets[key]:
        ss = sia.polarity_scores(tweet)
        result.append(ss)
        
    sentiment[key] = result
    
    
#%% Organize. Average polarity scores for basic interpretation.

for key in sentiment:
    
    sentiment[key] = pd.DataFrame.from_dict(sentiment[key])
    
avg_sentiment = {}

for key in sentiment:
    
    result = {}
    
    for col in sentiment[key]:
        
        avg = np.mean(sentiment[key][col])
        
        result[col] = avg
        
    avg_sentiment[key] = result
        
avg_sentiment = pd.DataFrame.from_dict(avg_sentiment)

print(avg_sentiment)

#%% Plots

size = 30
sub_size = 20
subsub_size = 15

save_path = "C:\\Users\Casey\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj\\Plots\\"

for main in avg_sentiment:
    
    fig,ax = plt.subplots(figsize = (20, 15))
    ax = avg_sentiment[main].plot(kind = "bar", fontsize = subsub_size)
    ax.set_title(main, fontsize = size)
    ax.set_xlabel("Polarity", fontsize = sub_size)
    ax.set_ylabel("Score", fontsize = sub_size)
    
    fig.savefig(save_path + main + " average polarity score")














