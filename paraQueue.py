# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:16:02 2016

@author: Alexander Singleton 
"""
import importlib

# Custom helper module, finds if <p> tags are outside of body paragraphs 
import findBoxes
importlib.reload(findBoxes)

def html_Finder(right_table, soup):     
    """Create copy of beautiful soup's html, and create string form of HTML."""
     
    to_Text = []
    full_HTML = []
    right_table_Vec = []             
     
    for para in range(0, len(right_table)):    
        to_Text.append(str(right_table[para]))        
                                     
    # Collect only html and string forms that are in body paragraphs.     
    bad_paras = findBoxes.find_Non_Body_Paras(soup, right_table)  
    coor_Para_Start = findBoxes.coor_Para(soup, right_table)                      
     
    if(coor_Para_Start == len(right_table)):
         full_HTML = to_Text[0]
         right_table_Vec.append(0)
               
    # Deletes paragraphs that are not in the main body of the article.
    for para in range(coor_Para_Start, len(right_table)):      
        
        no_Match = True                          
        for bad_para in bad_paras:
            
            if(right_table[para] == bad_para):                    
                no_Match = False
                bad_paras.remove(bad_para)
                
        if(no_Match):
            full_HTML.append(to_Text[para]) 
            right_table_Vec.append(para)

    return(full_HTML, right_table_Vec)