# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:20:26 2016

@author: Alexander Singleton 
"""
import re
import validLinks 
import removeParens
import urllib.request  
 
# Pathological exceptions: https://en.wikipedia.org/wiki/501(c)(3)_organization 
 
# This string is used to determine if an article link is a dead end
dead_Check = "&redlink=1" 
 
def remove_HTML_Parens(html_Str_Text):  
    """Appends strings before and after any appearence of parens to list"""  
    
    # Refresh variables.
    full_HTML_Para = [] 
    new_html_para = []         
    link_Search_Fail = True
    end_Of_Parentheses = True
    length = len(html_Str_Text)
    i = 0
    
    while(i<length): 
        #print(i)
        a  = html_Str_Text[i]
            
        if(a is not "("):
            new_html_para.append(a)
            i += 1  
        
        # This condition determines if parentheses are part of a link. 
        # Ex./wiki/Identity_(social_science)" title="Identity (social science)" 
        # These parens above must be preserved or else a valid link is lost.
        # If the parens are from a link URL, they are not deleted.
        if(i>0):
            if(a is "(" and new_html_para[i-1] is "_"):
                href_Str = []
                link_Search_Fail = True
                found_Close = False
                found_Link_With_Parens = False
                start_Index = i
                
                for char in range(start_Index+1, len(html_Str_Text)):
                    #print(char)
                    sub_Letter = html_Str_Text[char]  
                    if(sub_Letter is ")"): 
                        found_Close = True
                        href_Str_End = char
#                        print("href_Str_end")
#                        print(href_Str_End)
                        break 
                      
                    href_Str.append(sub_Letter)
                href_Str =  ''.join(href_Str)      
                href_Str = href_Str.replace("_"," ")
                href_Str = urllib.request.unquote(href_Str)
#                print("href")
#                print(href_Str)
                       
                title_Str = []    
                if(found_Close):
                    found_Start = False
                    found_Close = False
                    for char in range(href_Str_End+1, len(html_Str_Text)): 
                        if(html_Str_Text[char] is "("): 
                            title_Str_Start = char
#                            print("title_Str_Start")
#                            print(title_Str_Start)
                            found_Start = True
                            break
                     
                    if(found_Start): 
                        found_Start = False
                        for k in range(title_Str_Start+1, len(html_Str_Text)):
                            sub_Letter = html_Str_Text[k]  
                            if(sub_Letter is ")"): 
                                end_Index = k
#                                print(html_Str_Text[end_Index])
#                                print(end_Index)                                
                                break 
                                          
                            title_Str.append(sub_Letter)   
                        title_Str = ''.join(title_Str)        
#                        print(title_Str)
                
                # If the text of the first set of parentheses matches the
                # second set, then the parentheses are part of a link.                                         
                if(href_Str == title_Str): 
                    found_Link_With_Parens = True
#                    print("found_Link_With_Parens")
#                    print(found_Link_With_Parens)
                    for char in range(start_Index, end_Index):
                        new_html_para.append(html_Str_Text[char])
                    to_Full_HTML = ''.join(new_html_para)
                    full_HTML_Para.append(to_Full_HTML)       
                 
                # If found a link with parens, start search (i) after 
                # the closing parens. 
                if(found_Link_With_Parens):
                    i = end_Index              
                    link_Search_Fail = False
                
                else:
                   break 
        
        # If the parentheses are not part of a link, delete everything up to 
        # and including the associated closing parenthese. 
        if(a is "(" and link_Search_Fail):     
#            print("In here...")
            parentheses = 1
            end_Of_Parentheses = False            
    
            # Appends text before parens to a list 
            to_Full_HTML = ''.join(new_html_para)
            full_HTML_Para.append(to_Full_HTML)
            new_html_para = []
            
            # Iterates though charcters until finds closing parens, and deletes
            # any text in between             
            while(end_Of_Parentheses is False and i < length-1):
                i += 1            
                new_letter = html_Str_Text[i]
                
                if (new_letter is "("): 
                    parentheses = parentheses + 1
                        
                elif(new_letter is ")"): 
                    parentheses = parentheses - 1
                    
                    if(parentheses is 0):                        
                        end_Of_Parentheses = True
                        html_Str_Text = html_Str_Text[i+1:len(html_Str_Text)]
                        length = len(html_Str_Text)
                        
                        new_html_para = []
                        i = 0
    
       # If no closing parens is found, assume typo and refresh para
                elif(i is (length-2)):
                    new_html_para = []
                    
        if(link_Search_Fail is False):     
            link_Search_Fail = True
     
    # Appends any remaining text after last parens to list 
    new_html_para = ''.join(new_html_para)
    full_HTML_Para.append(new_html_para)
        
    return(full_HTML_Para)



def remove_Text_Parens(para_Text):  
    """Appends strings before and after any appearence of parens to list"""  
    
    full_Text_Para = []
    new_Text_Para = []
    end_Of_Parentheses = True
    length = len(para_Text)
    i = 0
    
    while(i<length): 
            
        a  = para_Text[i]
            
        if(a is not "("):
            new_Text_Para.append(a)
            i += 1        
                                           
        elif(a is "("):
            parentheses = 1
            end_Of_Parentheses = False            
    
            # Appends text before parens to a list 
            new_Text_Para = ''.join(new_Text_Para)
#            print(new_Text_Para)
            full_Text_Para.append(new_Text_Para)
            new_Text_Para = []
            
            # Iterates though charcters until finds closing parens, and deletes
            # any text in between             
            while(end_Of_Parentheses is False and i < length-1):
                i += 1            
                new_letter = para_Text[i]
                #print(i)
                #print("Inner i")
                if (new_letter is "("): 
                    parentheses = parentheses + 1
                        
                elif(new_letter is ")"): 
                    parentheses = parentheses - 1
                    
                    if(parentheses is 0):    
                        #print("make it here?")                    
                        end_Of_Parentheses = True
                        para_Text = para_Text[i+1:len(para_Text)]
                        length = len(para_Text)
                        i = 0
                 
                # If no closing parens is found, assume typo and refresh para
                elif(i is (length-1)):
                    new_Text_Para = []
     
    # Appends any remaining text after last parens to list 
    new_Text_Para = ''.join(new_Text_Para)
    full_Text_Para.append(new_Text_Para)
        
    return(full_Text_Para)


def link_Queue(html_Str_Text, para_Text, right_Link_Candidates): 
      
    # Fill lists with links that are valid for crawling purposes. 
    val_links = validLinks.link_Test(right_Link_Candidates)                                                  
    all_Valid_Links = val_links[0]
    all_Valid_Text_Links = val_links[1]   
    
    # Removes parentheses from the html and plain text of wiki article.
    full_Text_Paras = removeParens.remove_Text_Parens(para_Text)     
    full_HTML_Paras = removeParens.remove_HTML_Parens(html_Str_Text)
         
    found_Links = []    
    found_Text_Links = []
    
    # Search paras sequentially for both a text and href match. Text is what 
    # the link looks like on the website (plain text) and href is what the 
    # link looks like in the html. 
    for paras in range(0, min(len(full_Text_Paras), len(full_HTML_Paras))):           
    
        text_Para = full_Text_Paras[paras] 
        href_Para = full_HTML_Paras[paras]
    
        j = 0   
        while (j < len(all_Valid_Text_Links) and 
                                           len(all_Valid_Text_Links) is not 0):
           
            text_Of_Link = all_Valid_Text_Links[j]
            href_Of_Link = all_Valid_Links[j]     
            escaped_text_Of_Link = re.escape(text_Of_Link)
            escaped_href_Of_Link = re.escape(href_Of_Link)
            
            text_Search = re.compile(escaped_text_Of_Link)
            link_Search = re.compile(escaped_href_Of_Link)
            
            text_Result = text_Search.search(text_Para)  
            link_Result = link_Search.search(href_Para)
                 
            # If searches are successful, add found links to lists, and then
            # perform deletion operations in case multiple links/words are 
            # present in the article paragraph     
            if(text_Result is not None and link_Result is not None):
                text_Para = text_Para.replace(text_Of_Link,"",1) 
                href_Para = href_Para.replace(href_Of_Link,"",1) 
                
                found_Links.append(href_Of_Link)
                found_Text_Links.append(text_Of_Link)
                all_Valid_Text_Links.remove(text_Of_Link)                  
                all_Valid_Links.remove(href_Of_Link)
                j = -1                    
            j += 1         
         
    return(found_Links, found_Text_Links)
