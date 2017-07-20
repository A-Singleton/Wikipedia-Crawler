# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:56:03 2016

@author: Alexander Singleton 
"""
import re

def link_Test(right_Link_Candidates):
    """ Tests if link is viable, if so adds the link to the queue"""  
    
    # Helper string
    prefix = "https://en.wikipedia.org"

    # This set removes special characters that may interfere with regex search    
    chars_to_remove = set(("^", "$", "+", "?", "(",  ")", "{",
            "}", "|", "[" ,"]", ">", "<", )) 

    # Regex pattern that searches for the plain text title in html            
    text = re.compile(">.*<")
    
    # Declare strings that make a link inviable   
    IPA = ("/wiki/Help:IPA_for")
    wiktionary = "https://en.wiktionary"
    wikimedia = "https://commons.wikimedia.org"
    audio_ext1 = ".ogg"
    audio_ext2 =  ".oga"
    coor = "/wiki/Geographic_coordinate_system"
    attr_Needed = "Wikipedia:Attribution needed"
    image = "image"    
    temp = "/w/index.php?title=Template"
                
    #Lists for the valid links and text form of links             
    all_Right_links = []
    all_Right_Text_links = []            
    
    # This loops through all possible links sequentially. It derives numerous
    # substrings and compares them to all of the given validation exceptions.
    for link in right_Link_Candidates:                          
                                   
            href = link.get('href')       
            title_html = link.get('title')    
            class_html = link.get('class')
            
            link_ext = href[-4:len(href)]
            IPA_Form = href[0:len(IPA)]                
            wiktionary_Form = href[0:len(wiktionary)]
            wikimedia_Form = href[0:len(wikimedia)]
            prefix_Form = href[0:len(prefix)]
            temp_Form = href[0:len(temp)]
            
            # Sets the href to a rejected one if it directs to a non-english
            # wikipedia article                 
            if(prefix_Form[11:20] == 'wikipedia' and 
                         prefix_Form[8:10] != 'en'):  
                             
                href = coor
            #ex. "https://ja.wikipedia.org/" is rejected               
           
            # If the link passes all exceptions, add it to the lists                        
            if(IPA_Form != IPA and href != coor and link_ext != audio_ext1 and
            link_ext != audio_ext2 and wiktionary_Form != wiktionary and 
            title_html != attr_Needed and class_html != image and 
            wikimedia_Form != wikimedia and temp != temp_Form):
            
                  string_Form = str(link)
                  searched_Text = text.search(string_Form)                 
                  found_Text = searched_Text.group()                    
                  found_Text = [c for c in found_Text if c 
                                   not in chars_to_remove]
                  found_Text = ''.join(found_Text)
                  
                  all_Right_links.append(href)
                  all_Right_Text_links.append(found_Text) 
    
    return(all_Right_links, all_Right_Text_links)