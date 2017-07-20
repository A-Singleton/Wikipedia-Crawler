# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:57:20 2016

@author: Alexander Singleton 
"""

def find_Non_Body_Paras(soup, right_table):
    """Finds any <p> tags in the HTML that are not body paragraphs (boxes)"""    
    
    bad_paras = []
     
    #If an info-box is in the page
    info_Box = soup.find_all("table", class_="infobox")
    if(len(info_Box) > 0):
        
        info_Paras = info_Box[0].find_all("p") 
       
        for i in info_Paras:
                bad_paras.append(i)
    
    #If a vertical box is in the page
    vet_Box = soup.find_all("table", class_="vertical-navbox nowraplinks")
    if(len(vet_Box) > 0):
        
        vet_Paras = vet_Box[0].find_all("p") 
        
        for i in vet_Paras:
                bad_paras.append(i)           
                     
     #If an m-box is present        
    m_Box = soup.find_all("td", class_="mbox-text")
    if(len(m_Box ) > 0):
            m_Paras = m_Box[0].find_all("p") 
            
            for i in m_Paras:
                bad_paras.append(i)
                            
    #If a nav-box is present      
    nav_Box = soup.find_all("div", class_="navbox")
    if(len(nav_Box) > 0):
            nav_Paras = nav_Box[0].find_all("p") 
            
            for i in nav_Paras:
                bad_paras.append(i)      
                
    # If a toc-color box is present     class="toccolours"
    to_Box = soup.find_all("table", class_="toccolours")
    if(len(to_Box) > 0):
            to_Paras = to_Box[0].find_all("p") 
            
            for i in to_Paras:
                bad_paras.append(i)            
        
        
    return bad_paras       
           
           
def coor_Para(soup, right_table):            
    """Checks if a coordinate paragraph is the first <p> tag in the article""" 
    
    found_Coor = 0
    first_Box = soup.find("p")            
    coor_Box = soup.find_all("span", style = "font-size: small;") 
    if(len(right_table) > 0):
        coor_First_Para = right_table[0].find_all("span", 
                         style = "font-size: small;") 
        
        
        if(len(first_Box) > 0 and len(coor_Box) > 0 and
                              len(coor_First_Para) > 0):
           found_Coor = 1

    return found_Coor
                
                
    