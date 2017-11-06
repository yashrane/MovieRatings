# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:41:54 2017

@author: yashr
"""

import pandas as pd
#import numpy as np
import seaborn as sns
import pickle
import collections
import json

def jsonToList(json_str):
    json_df = pd.read_json(json_str, orient='records')
    if 'name' in json_df.columns:
        names = json_df['name'].tolist()
        return names
    return None

def jsonToString(json_str):
#    if type(json_str) is str:
    try:
        json_dict = {}
        json_dict = json.loads(json_str)
        if 'name' in json_dict.keys():
            return json_dict['name']
    except Exception: #if there was any error parsing the json
        return None   #there were many different cases that threw errors, so i used a generic catch

def readCSV():
    df = pd.read_csv('./lib/movies_metadata.csv')
    df['genres'] = df['genres'].str.replace("\'",'\"')
    df['belongs_to_collection'] = df['belongs_to_collection'].str.replace("\'",'\"')
    
    df['genres'] = df['genres'].apply(jsonToList)
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(jsonToString)
    return df


def makeGenres(df):
    genre_dict = df['genres'].apply(collections.Counter)
    genres = pd.DataFrame.from_records(genre_dict).fillna(value=0)
    fake_news = ['Aniplex', 'BROSTA TV', 'Carousel Productions', 'GoHands', 'Mardock Scramble Production Committee','Odyssey Media', 'Pulser Productions','Rogue State', 'Sentai Filmworks','Telescene Film Group Productions','The Cartel', 'Vision View Entertainment']
    genres.drop(labels=fake_news,axis=1, inplace=True)
    df = df.merge(genres, left_index=True, right_index=True)#validates='one_to_one'
    return df

df = readCSV()
df = makeGenres(df)
store = pd.HDFStore('lib/movies.h5')
store['movies'] = df


"""Long Term Storage"""
#store = pd.HDFStore('movies.h5')
#store['df'] = df  # save it
#store['df']  # load it

#df.to_pickle('movies.df')
#pd.read_pickle('movies.df')R