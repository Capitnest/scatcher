# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import urllib
import sys
from typing import List
from functions.article import *
from functions.tweet import tweet_post
import random
import json
import csv
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

    #Bitcoin
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

  

    print(f'{topic} news ✅ - 10 seconds timeout')

    


#the main function will scrape the internet for information, create the posts, 
# shuffle them, and cateogirze them for its own section on the website
def main():

    try:

 
        news("crypto", 1)

    except:

        print("Error! Some error occured.")




if __name__ == '__main__':
    main()