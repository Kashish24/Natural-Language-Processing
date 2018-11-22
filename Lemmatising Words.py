# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:14:48 2018

@author: KING
"""

import nltk 
from nltk.stem import WordNetLemmatizer 
wordnet_lemmatizer = WordNetLemmatizer() 
word_data = "car bus train automobile"
nltk_tokens = nltk.word_tokenize(word_data) 
for w in nltk_tokens: 
       print ("Actual: %s  Lemma: %s"%(w,wordnet_lemmatizer.lemmatize(w)))