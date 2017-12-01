# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:13:51 2017

@author: Casey

Conduct sentiment on tweets using NLTK VADER
"""

#%% Setup

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


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

hashtags = ["balmdotcom",
            "boybrow",
            "glossier",
            "glossiergirl",
            "glossierpink",
            "nofilterjustlgossier"
            ]
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
        
    sentiment[key] = pd.DataFrame.from_dict(result)
    

sentiment["balmdotcom"]["date"] = balmdotcom["date"].values.tolist()
sentiment["boybrow"]["date"] = boybrow["date"].values.tolist()
sentiment["glossier"]["date"] = glossier["date"].values.tolist()
sentiment["glossiergirl"]["date"] = glossiergirl["date"].values.tolist()
sentiment["glossierpink"]["date"] = glossierpink["date"].values.tolist()
sentiment["nofilterjustlgossier"]["date"] = nofilterjustlgossier["date"].values.tolist()

for key in hashtags:
    sentiment[key] = sentiment[key].sort_values(by = ["date"])


#%% Organize. Average polarity scores for basic interpretation.

    
avg_sentiment = {}

for key in sentiment:
    
    result = {}
    
    for col in sentiment[key]:
        
        if col == "date":
            continue
        
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
    if main != "glossier_tweets":
        ax.set_title("#" + main, fontsize = size)
    else:
        ax.set_title(main, fontsize = size)
    ax.set_xlabel("Polarity", fontsize = sub_size)
    ax.set_ylabel("Score", fontsize = sub_size)
    
#    fig.savefig(save_path + main + " average polarity score")
#    plt.close(fig)

#%% One Figure

size = 45
sub_size = 40
subsub_size = 35

X = ["Compound", "Negative", "Neutral", "Positive"]

fig,ax = plt.subplots(3, 2, figsize = (26.67,30))

ax[0,0].bar(X, avg_sentiment["balmdotcom"])
ax[0,0].tick_params(axis='both', labelsize=subsub_size)
ax[0,0].set_ylabel("Score", fontsize = sub_size)
ax[0,0].set_title("#balmdotcom", fontsize = size)

ax[0,1].bar(X, avg_sentiment["boybrow"])
ax[0,1].tick_params(axis='both', labelsize=subsub_size)
ax[0,1].set_title("#boybrow", fontsize = size)

ax[1,0].bar(X, avg_sentiment["glossier"])
ax[1,0].tick_params(axis='both', labelsize=subsub_size)
ax[1,0].set_ylabel("Score", fontsize = sub_size)
ax[1,0].set_title("#glossier", fontsize = size)

ax[1,1].bar(X, avg_sentiment["glossiergirl"])
ax[1,1].tick_params(axis='both', labelsize=subsub_size)
ax[1,1].set_title("#glossiergirl", fontsize = size)

ax[2,0].bar(X, avg_sentiment["glossierpink"])
ax[2,0].tick_params(axis='both', labelsize=subsub_size)
ax[2,0].set_xlabel("Polarity", fontsize = sub_size)
ax[2,0].set_ylabel("Score", fontsize = sub_size)
ax[2,0].set_title("#glossierpink", fontsize = size)

ax[2,1].bar(X, avg_sentiment["nofilterjustlgossier"])
ax[2,1].tick_params(axis='both', labelsize=subsub_size)
ax[2,1].set_xlabel("Polarity", fontsize = sub_size)
ax[2,1].set_title("#nofilterjustlgossier", fontsize = size)
  
plt.tight_layout()
plt.close(fig)

#fig.savefig(save_path + "Average Polarity Scores")

#%% Timeseries Test


fig,ax = plt.subplots()

# Smooth using Savitzky-Golay filter given noisy nature of data

pos = savgol_filter(sentiment["balmdotcom"]["pos"], 51, 3)
neg = savgol_filter(sentiment["balmdotcom"]["neg"], 51, 3)
neu = savgol_filter(sentiment["balmdotcom"]["neu"], 51, 3)
compound = savgol_filter(sentiment["balmdotcom"]["compound"], 51, 3)

ax.plot(sentiment["balmdotcom"]["date"], pos, color = "green")
ax.plot(sentiment["balmdotcom"]["date"], neg, color = "red")
ax.plot(sentiment["balmdotcom"]["date"], neu, color = "blue")
ax.plot(sentiment["balmdotcom"]["date"], compound, color = "black")


#%% Timeseries Subplot

fig,ax = plt.subplots(3, 2, figsize = (26.67,30))

for y in range(3):
    
    for x in range(2):
        
        i = 2*y + x
        
        key = hashtags[i]
        
        print(y)
        print(x)
        print(key)
        
        window = np.int(len(sentiment[key]) / 10)
        
        if window%2 == 0:
            window += 1
            
        pos = savgol_filter(sentiment[key]["pos"], window, 3)
        neg = savgol_filter(sentiment[key]["neg"], window, 3)
        neu = savgol_filter(sentiment[key]["neu"], window, 3)
        compound = savgol_filter(sentiment[key]["compound"], window, 3)
        
        l1 = ax[y,x].plot(sentiment[key]["date"], pos, color = "green")
        l2 = ax[y,x].plot(sentiment[key]["date"], neg, color = "red")
        l3 = ax[y,x].plot(sentiment[key]["date"], neu, color = "blue")
        l4 = ax[y,x].plot(sentiment[key]["date"], compound, color = "black")
        
        ax[y,x].set_title(key, fontsize = size)
        ax[y,x].set_xlabel("Date", fontsize = sub_size)
        ax[y,x].set_ylabel("Score", fontsize = sub_size)
        ax[y,x].tick_params(axis = "both", labelsize = subsub_size)
        ax[y,x].set_xticks([ax[y,x].get_xticks()[1],ax[y,x].get_xticks()[-1]])
        
plt.tight_layout()
        
plt.figlegend((l1, l2, l3, l4), ("Positive", "Negative", "Neutral", "Compound"), "lower right")

fig.savefig(save_path + "Time Series Polarity Scores")
        




