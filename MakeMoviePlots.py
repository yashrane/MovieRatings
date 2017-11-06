# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:47:26 2017

@author: yashr
"""

import pandas as pd
import numpy as np

store = pd.HDFStore('lib/movies.h5')
movies = store['movies']

#i want to make a plot of genre vs rating