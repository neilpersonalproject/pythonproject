#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:24:14 2019

@author: neillagundino
"""

#Question 2: How to get latitude and longtitude information, separated by comma.
filename = '/Users/neillagundino/Lab 1  answers/data/full_text_small.txt'
with open(filename, 'r') as f:      
    lines = f.readlines()
    for line in lines:               
        line_list = line.lower().split('\t')        
        lat = line_list[3]
        lon = line_list[4]
        #print(lat+ "," +lon)
        print(','.join([lat, lon])) 