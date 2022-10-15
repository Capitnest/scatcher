# import necessary libraries

import re
import urllib
import sys
from typing import List

import random
import json
import time
import datetime
from urllib.parse import urlparse

from news import news_articles
from twitter import tweet_post
import datetime

args : List[str] = sys.argv

def news(topic, date=None):
    
    if(date == None):
        news_articles(topic)
    else:
        news_articles(topic, date)

    
    if(date == None):
        results = open(f'results/news_{topic}.json')
        results_data = json.load(results)
        
        temp = list(results_data.values())
        random.shuffle(temp)

        with open(f'posts/{topic}.json', 'w') as json_file:
            json.dump(temp, json_file)

    else:
        results = open(f'results/news_{topic}_{date}.json')
        results_data = json.load(results)
        
        temp = list(results_data.values())
        random.shuffle(temp)

        with open(f'posts/{topic}_{date}.json', 'w') as json_file:
            json.dump(temp, json_file)

  

    if(date == None):

        print(f'{topic} news✅ - 5 seconds timeout')

    else:
        print(f'{topic} news with date {date}✅ - 5 seconds timeout')

    time.sleep(5)
    

# get all the news from multiple time steps
def getNews(topic):

    news(topic)
    news(topic, 1)
    news(topic, 7)
    news(topic, 32)
    news(topic, 90)
    news(topic, 180)
    news(topic, 360)
    

def main():

    try:


        getNews("bitcoin")
        getNews("crypto")
        getNews("ethereum")
        getNews("solana")
        getNews("cardano")
        

    except:

        print("Error! Some error occured.")


if __name__ == '__main__':
    main()