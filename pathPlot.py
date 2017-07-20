# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:12:43 2016

@author: Alexander Singleton 
"""

import matplotlib.pyplot as plt

def plot(pathlengths):
    """Plots Histogram of path lengths from Random articles to Philosophy""" 
    
    path_length_dict = {}
    
    for pathLen in pathlengths:
        if pathLen not in path_length_dict:
            path_length_dict[pathLen] = 1
        else:
            path_length_dict[pathLen] += 1
    
    # plot the distribution of path lengths
    xaxis = []
    yaxis = []
    
    for path_length in path_length_dict.keys():
        xaxis.append(path_length)
        yaxis.append(path_length_dict[path_length])
    
    plt.bar(xaxis, yaxis, align='center')
    plt.xlabel('Path Length')
    plt.ylabel('Frequency')
    plt.title('Freq of Path Lengths to Philosophy Page')
    plt.savefig('fig.png')      