#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
from anonBrowser import *
import json
import re
import mechanize
from bs4 import BeautifulSoup, NavigableString, Tag

USERAGENT =[('User-agent','Googlebot/2.1 (+http://www.google.com/bot.html')]

class TwitPerson:
    def __init__(self, handle):
        self.handle = handle
        self.browser = self.set_browser()
        self.tweets = self.get_init_tweets()

    def get_init_tweets(self ):
        try:
            response = self.browser.open("https://twitter.com/"+self.handle)
            text = response.read()
            soup = BeautifulSoup(text, 'html.parser')
        except:
            print ('No user found with that id.')
            return 1

        tweets = [p.text for p in soup.findAll('p', class_='tweet-text')[0:5]]
        return tweets

    def display_tweets(self):
        for t in self.tweets:
            print ('tweet: ',t)

    def set_browser(self):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = USERAGENT
        browser.cookie_jar = LWPCookieJar()
        return browser

    def new_tweets(self):
        response = self.browser.open("https://twitter.com/" + self.handle)
        text = response.read()
        soup = BeautifulSoup(text, 'html.parser')

        last_collected_tweet_found = False
        start_index = 0
        end_index = 1
        while last_collected_tweet_found == False:
            tweets = [p.text for p in soup.findAll('p', class_='tweet-text')[start_index:end_index]]
            for tw in tweets:
                if tw in self.tweets:
                    last_collected_tweet_found = True
                    return tweets
                else: # add to self.tweets
                    print ('new tweet ', tw)
                    self.tweets.append(tw)

            start_index = start_index + 2
            end_index = end_index + 2



