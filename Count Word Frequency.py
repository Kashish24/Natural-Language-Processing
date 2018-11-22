# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:56:13 2018

@author: KING
"""

from bs4 import BeautifulSoup 
import urllib.request 
import nltk  
response = urllib.request.urlopen('http://php.net/')  
html = response.read()  
soup = BeautifulSoup(html,"html5lib")  
text = soup.get_text(strip=True)  
tokens = [t for t in text.split()]  
freq = nltk.FreqDist(tokens)  
for key,val in freq.items():      
    print (str(key) + ':' + str(val)) 