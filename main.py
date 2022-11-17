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
from functions.lunarcrush import nft_of_the_day, nft_of_the_day_info, coin_of_the_day, coin_of_the_day_info, stock_of_the_day, stock_of_the_day_info

from news import news_articles
import datetime

args : List[str] = sys.argv

def info_to_file(info, file):

    data = info()

    with open(file, 'w') as f:
        json.dump(data, f)

    print(f'✓ Lunarcrush - {info} to {file} (time sleep 5)')
    time.sleep(5)
    

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



    # getNews("bitcoin")
    # getNews("crypto")
    # getNews("ethereum")
    # getNews("solana")
    # getNews("cardano")

    info_to_file(nft_of_the_day, "data/nft_of_the_day.json")
    info_to_file(nft_of_the_day_info, "data/nft_of_the_day_info.json")
    info_to_file(coin_of_the_day, "data/coin_of_the_day.json")
    info_to_file(coin_of_the_day_info, "data/coin_of_the_day_info.json")
    info_to_file(stock_of_the_day, "data/stock_of_the_day.json")
    info_to_file(stock_of_the_day_info, "data/stock_of_the_day_info.json")
   
    



if __name__ == '__main__':
    main()