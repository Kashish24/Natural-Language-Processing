# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:11:09 2018

@author: KING
"""

import nltk 
from nltk.stem.porter import PorterStemmer 
porter_stemmer = PorterStemmer() 
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms" 
# First Word tokenization 
nltk_tokens = nltk.word_tokenize(word_data) 
#Next find the roots of the word 
for w in nltk_tokens:
    print "Actual: %s  Stem: %s" %(w,porter_stemmer.stem(w))