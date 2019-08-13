#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:00:18 2019

@author: neillagundino
"""
import tweepy

class Processor():
    def __init__(self, key_word, max_tweets, api):
        self.query = key_word
        self.max_tweets = max_tweets
        self.api = api
        
    def search_query(self):
        searched_tweets = [status for status in tweepy.Cursor(self.api.search, q=self.query).items(self.max_tweets)]
        return searched_tweets 
    