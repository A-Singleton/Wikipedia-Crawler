# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:20:20 2016

@author: Alexander Singleton 
"""
import re

# Regex pattern that searches for title in html 
text_Title = re.compile(">.*<")

def get_Title(soup):
    article_Title = soup.find_all("h1", class_="firstHeading")
    string_Title = str(article_Title)
    searched_Title = text_Title.search(string_Title)
    found_Title = searched_Title.group()
    found_Title = found_Title.replace("<i>","")
    found_Title = found_Title.replace("</i>","")
    
    return found_Title[1:-1]