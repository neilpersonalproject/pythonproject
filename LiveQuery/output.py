#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:22:45 2019

@author: neillagundino
"""

class WriteToOutput():
   def __init__(self, output_path, searched_tweets):
            self.output_path = output_path
            self.searched_tweets = searched_tweets
        
   def write_to_output(self):
        with open(self.output_path, 'w') as output:
            for tweet in self.searched_tweets:
                content = []
                created_at = content.append(tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                id = content.append(str(tweet.id))
                text = content.append(tweet.text.strip('\n').strip('\r').replace('\n',' ').replace('\r',' '))
                screen_name = content.append(tweet.user.name)
                output.write('\t'.join(content) + '\n')
