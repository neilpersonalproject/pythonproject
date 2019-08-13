#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:21:46 2019

@author: neillagundino
"""

#Lab: Content Extraction


#Question 1: We are going to exacting all retweets and the user information
filename = '/Users/neillagundino/Lab 1  answers/data/full_text_small.txt'
with open(filename, 'r') as f:      
    lines = f.readlines()

    for line in lines:          
        line_list = line.lower().split('\t')
        tweet = line_list[-1]
        if 'rt ' in tweet:  #if tweet.startwith("rt")
            retweet = tweet[:17]
            print(retweet) 


