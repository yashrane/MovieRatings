# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:05:49 2017

@author: yashr
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
np.random.seed(0)


store = pd.HDFStore('lib/movies.h5')
movies = store['movies']


movies['is_train'] = np.random.uniform(0, 1, len(movies)) <= .6

# Creates 3 dataframes: train, validation, and test
#   train is the training data for the Random Forest
#   test is used to create a list of predictions
#   validation is also used to create a list of predictions and is cross referenced with test
train, temp = movies[movies['is_train']==True], movies[movies['is_train']==False]
temp['is_validation'] = np.random.uniform(0, 1, len(temp)) <= .5 #may give a setting with copy warning. this is not an issue and can be ignored
validation, test = temp[temp['is_validation']==True], temp[temp['is_validation']==False]

# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the validation data:',len(validation))
print('Number of observations in the test data:',len(test))

feature_columns = movies.columns[24:44] #all the genres
#add more here
