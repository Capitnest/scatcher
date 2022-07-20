# import necessary libraries
import twint
from bs4 import BeautifulSoup
import requests
import re
import urllib
import sys
from typing import List
from twitter_scraper import get_tweets
from functions.article import *
from functions.tweet import tweet_post
from data.tweets import usernames
from data.websites import links
import random
import twint
import json
import csv
import time
import datetime
from urllib.parse import urlparse
from data.tweets import usernames
from data.tweets import profile_images

from news import news_articles
from twitter import tweet_post
import datetime

args : List[str] = sys.argv

#the main function will scrape the internet for information, create the posts, 
# shuffle them, and cateogirze them for its own section on the website
def main():

    try:

        date = ""

        if(args[1] == "today"):
            date = time.strftime("%d/%m/%Y", time.localtime()) 
        else:
         
            date = args[1]

        #scrape for news for each specific coin
        news_articles("bitcoin")
        print('bitcoin news ✅ - 10 seconds timeout')
        time.sleep(10)
        news_articles("solana")
        print('solana news ✅ - 10 seconds timeout')
        time.sleep(10)
        news_articles("ethereum")
        print('ethereum news ✅ - 10 seconds timeout')
        time.sleep(10)
        news_articles("cardano")
        
        print('cardano news ✅ - 10 seconds timeout')
        time.sleep(10)

        #general news & tweets about crypto
        news_articles("crypto")
        tweet_post(date)
        print("crypto news & tweets ✅")
        print("writing files...")


        # #shuffle the posts

        #Bitcoin
        bitcoin = open('results/news_bitcoin.json')
        bitcoin_data = json.load(bitcoin)
        
        temp = list(bitcoin_data.values())
        random.shuffle(temp)

        with open('posts/bitcoin.json', 'w') as json_file:
            json.dump(temp, json_file)

        #Ethereum
        ethereum = open('results/news_ethereum.json')
        ethereum_data = json.load(ethereum)
        
        temp = list(ethereum_data.values())
        random.shuffle(temp)

        with open('posts/ethereum.json', 'w') as json_file:
            json.dump(temp, json_file)

        #Solana
        solana = open('results/news_solana.json')
        solana_data = json.load(solana)
        
        temp = list(solana_data.values())
        random.shuffle(temp)

        with open('posts/solana.json', 'w') as json_file:
            json.dump(temp, json_file)

        #Cardano
        cardano = open('results/news_cardano.json')
        cardano_data = json.load(cardano)
        
        temp = list(cardano_data.values())
        random.shuffle(temp)

        with open('posts/cardano.json', 'w') as json_file:
            json.dump(temp, json_file)

        # General Posts

        news = open('results/news_crypto.json')
        news_data = json.load(news)

        

        tweets = open('results/tweets.json')
        tweets_data = json.load(tweets)
        
        

        all = {**tweets_data, **news_data}
        

        temp = list(all.values())
        random.shuffle(temp)

        with open('posts/general.json', 'w') as json_file:
            json.dump(temp, json_file)

        print("Done")

    except:

        print("Error! Please specify a date!")




if __name__ == '__main__':
    main()
