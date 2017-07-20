# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:53:48 2016

@author: Alexander Singleton 
"""

import requests   

from bs4 import BeautifulSoup   #Web scraping package

def request_Page(URL):
    """Downloads and parses the html of any Wikipedia page using BeautifulSoup"""
    good_Connection = False
    while(good_Connection is False): 
        
        try:
             page = requests.get(URL) 
             good_Connection = True
             
        except requests.exceptions.ConnectionError:
            print("Connection refused") 
            URL = "http://en.wikipedia.org/wiki/Special:Random"

    return BeautifulSoup(page.content, "lxml")
    