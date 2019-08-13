#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:25:21 2019

@author: neillagundino
"""
#Question 3: Find all tweets that contain hashtag. e.g. "#nowplaying"
filename = '/Users/neillagundino/Lab 1  answers/data/full_text_small.txt'
with open(filename, 'r') as f:     # open the file for read
    lines = f.readlines()
    for line in lines:               
        line_list = line.lower().split('\t')
        tweet = line_list[5]    
        for x in tweet.split():
            if x.startswith("#"):
                 print(x[1:])   
