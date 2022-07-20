# This part of the scraper scrapes the latest tweets from a specific date from the users from our list
# We use the twint library to scrape twitter

import twint
import csv
import datetime
from urllib.parse import urlparse
from data.tweets import usernames
from data.tweets import profile_images
import sys
from typing import List
import json

args : List[str] = sys.argv


# takes the information necessary for a post from the latest 10 tweets of a user
# filter_date - choose what date to use to filter through the tweets
def tweet_post(filter_date):

    #clean the results of the last scrape
    for file in usernames:
        with open(f"cache/{file}.csv", "w"):
            pass

    index = 0
    posts = {}
    #go through every username from our list and scrape their tweets
    for users in usernames:

        # Tweets
        c = twint.Config()
        username = users
        print(users)
        img = profile_images[usernames.index(users)]
        print(img)
        c.Username = username
        c.Limit = 1
        c.Custom["tweet"] = ["name", "username", "tweet", "link", "created_at"]
        c.Output = f"cache/{username}.csv"
        c.Store_csv = True

        # Run
        twint.run.Search(c)

        # make the results
        with open(f'cache/{username}.csv', 'r') as f:
            csv_reader = csv.reader(f)

            for line in csv_reader:
                name = line[0]
                account_name = line[1]
                tweet = line[2]
                source = line[3]
                date = line[4]
                link = "https://" + (urlparse(source).netloc) + "/" + account_name

                date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S UTC')
                date = date.strftime("%d/%m/%Y")
                
                if(img == ""):
                    lines = {f"{index}" : {"name": name, "username": f'@{account_name}', "user_url": link ,"profile": "", "title": tweet, "date": date, "source": source}}
                   
                else:
                    
                    lines = {f"{index}" : {"name": name, "username": f'@{account_name}', "user_url": link ,"profile": img, "title": tweet, "date": date, "source": source}}

                posts.update(lines)

                print("=====`")
                print(date)
                print(filter_date)
                if(date == filter_date):

                    posts.update(lines)
                else:
                    continue

                index += 1

    print(posts)
    
    with open(f'results/tweets.json', "w") as f:
        json.dump(posts, f)

# {
#     "name": "benzinga",
#     "username": "www.benzinga.com",
#     "profile": "",
#     "title": "Cryptocurrency EOS's Price Increased More Than 3% Within 24 hours",
#     "picture": "https://rapidapi.usearch.com/api/thumbnail/get?value=1722197388307772900",
#     "description": "July 7, 2022 2:07 PM | Over the past 24 hours, EOS's EOS/USD price has risen 3.74% to $1.02. This continues its positive trend over...",
#     "date": "2022-07-07T18:07:54",
#     "source": "https://www.benzinga.com/markets/cryptocurrency/22/07/27991486/cryptocurrency-eoss-price-increased-more-than-3-within-24-hours"
#   },

if __name__ == "__main__":
    tweet_post(args[1])