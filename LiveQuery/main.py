#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# imports
import csv
import json
import time
import tweepy
import datetime 

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from config import TweetConfig
from processor import Processor
from output import WriteToOutput

flood_project = TweetConfig('ARoHNwFjcDC9svG4JTMMMhdYc',
                            'MR7LHqEWspS2Zm7vfCP92bVCkawiiw7WjVn1JW2STyhydYu7tW',
                            '1096330764-8dvEkkK8ncA05WhLq2J7K7vSMASdbiJ5o6XpyGZ',
                            'vBH0ZuSo346VrYSJV8IuBYzpogJZsomyzHbwdxKEsUQ22')



# set twitter keys/tokens
auth = OAuthHandler(flood_project.consumer_key, flood_project.consumer_secret)
auth.set_access_token(flood_project.access_token, flood_project.access_token_secret)

api = tweepy.API(auth)

my_twitter = api.me()

p = Processor('flood',100,api)
searched_list = p.search_query()

WriteToOutput('neilsearch4.txt', searched_list).write_to_output()

