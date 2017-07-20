# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:31:00 2016

@author: Alexander Singleton 
"""
#Dependencies 
import re        #Package for implementing regular expressions  
import time 
#import importlib  # For updating custom modules after edits
#importlib.reload(makeSoup)

### Custom Modules
import makeSoup
import pathPlot
import titleScrape
import paraQueue
import removeParens

start_time = time.clock() #Begins runtime analysis

# Declare lists of visited links, both successfully finding philosophy and not.
failure_Links_Cycle = []
failure_Links_Dead_End = []
failure_Links_Anomoly = []
success_Links = []
pathlengths = []
start_Article = []

# Helper Strings
prefix = "https://en.wikipedia.org"
philosophy = "https://en.wikipedia.org/wiki/Philosophy"       

searches = 500
####################################  Outer Loop    
for crawls in range(0, searches):
    #URL = "" #For debugging specific links 
    URL = "http://en.wikipedia.org/wiki/Special:Random" 
    
    soup = makeSoup.request_Page(URL) # Sourcecode parsed by Beautiful Soup
                    
    # Get article title
    start_Article.append(titleScrape.get_Title(soup))

    # Reset Boolean logic    
    found_Dead_End = False
    found_Cycle = False
    found_Philo = False
    no_Match = True    
    
    link_Chain = []
    link_Set = set()     #Declares a set, for detecting cycles
                        
    while(not found_Philo and not found_Cycle and not found_Dead_End):
                                         
        found_Link = False
                                
        # Finds all paragraphs in html of wiki article
        right_table = soup.find_all("p")    

        # Fill lists of all body paragraphs with corresponding HTML data.
        if(len(right_table)>0):
            body_Paras = paraQueue.html_Finder(right_table, soup)                       
            full_HTML = body_Paras[0]
            right_table_Vec = body_Paras[1] 
            
        else:
            full_HTML = []
            right_table_Vec = []
             
        for p in range(0, len(full_HTML)):   
            
            end_Check = int(p)+1 
            
            # Escape if found link
            if(found_Link is True):
                break     

            # Turns the Beautiful soup body paragraphs into a string form 
            # so that the paragraph can be searched for valid links
            html_Text = right_table[right_table_Vec[p]]
            html_Str_Text = str(html_Text)            
            para_Text = right_table[right_table_Vec[p]].get_text() 

            # Generates a list of all links present in body paragraph            
            right_Link_Candidates = right_table[right_table_Vec[p]].find_all("a", 
                                              title = re.compile(".*"))
                    
            # Takes a plain-text version of the wiki page and removes
            # anything in parentheses
            found_Links = removeParens.link_Queue(html_Str_Text, para_Text, 
                                                  right_Link_Candidates)                                                
            found_HREF = found_Links[0]  
            found_Text_Links = found_Links[1]                                  
            
            # Number of candidate links                                                                                                                                         
            link_Number = len(found_HREF)
            if(link_Number is 0):
                print("No links, trying next paragraph")
                                                                                          
            # Analyzes links systematically:          
            for i in range(0, link_Number):
                print("looking")    
                arl = found_HREF[i]
                link_Text = found_Text_Links[i] 
                     
                # Add link to set, if not a member. If a member, found cycle. 
                if(arl in link_Set):                     
                    print('Failure, found a Cycle')
                    failure_Links_Cycle.append(start_Article[crawls])                                          
                    found_Link = True
                    found_Cycle = True
                    break
                
                else: 
                    link_Set.add(arl) 
                                                    
                # Found Philosophy Page.      
                if(prefix + arl == philosophy):
                    print('Success, found {}!'.format('Philosophy'))
                    link_Chain.append(URL)
                    success_Links.append(start_Article[crawls])
                    pathlengths.append(len(link_Chain))
                    found_Philo = True
                    found_Link = True                      
                    break                                  
                    
                # Found a valid link that is not Philosophy
                print('Nice, traveling to {}'.format(link_Text))
                link_Chain.append(URL)                       
                URL = prefix + arl
                soup = makeSoup.request_Page(URL)
                found_Link = True
                break
                   
        # Either no body paragraphs in article or all candidate paragraphs have
        # been exhaustively searched with no link or termination event found.                          
        if(len(right_table) == 0 or end_Check == len(full_HTML)
                      and not found_Link and not found_Dead_End 
                      and not found_Cycle and not found_Philo):                             
                print('Failure, Did not Work')                
                failure_Links_Dead_End.append(start_Article[crawls])                
                found_Dead_End = True
                break

##Plot histogram of successes.
pathPlot.plot(pathlengths)
                    
print("--- %s seconds ---" % (time.clock() - start_time))