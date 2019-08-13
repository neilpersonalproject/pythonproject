 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:44:35 2019

@author: neillagundino
"""

class TweetConfig():
    def __init__ (self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret