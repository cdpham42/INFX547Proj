# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:29:57 2017

@author: Casey
"""

#%%

from nltk.corpus import stopwords
import pandas as pd
import os
import codecs

os.chdir("C:\\Users\\Casey\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj")

#%%

word_list = pd.read_csv("d3viz_words.csv")["Words"].values.tolist()

filtered_words = [word for word in word_list if word not in stopwords.words("english")]

#%%

with codecs.open("filtered_words.csv", "w+", "utf-8") as out:
    for word in filtered_words:
        out.write(word + ",")
        
#%%
        
filtered_words_df = pd.DataFrame()

filtered_words_df["Words"] = filtered_words

filtered_words_df.to_csv("filtered_words_df.csv")
