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
import csv
import datetime
from urllib.parse import urlparse
from data.tweets import usernames
from data.tweets import profile_images

args : List[str] = sys.argv
link = ""

# simulating normal headers from a browser, so it will not to be detected as a bot by some website
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def main():

    if(args[1] == "article"):

        filter_date = ""

        try:
            filter_date = args[2]
        except:
            filter_date = ""

        posts = []

        #clean the results of the last scrape
        with open("articles.txt", "w"):
            pass

        for article in links:


            link = links[links.index(article)]
            r = requests.get(link, headers=headers)
            soup = BeautifulSoup(r.content, features="lxml")

            name = article_site_name(soup)
            username = article_site_name_url(link)
            profilePic = article_site_logo_url(soup)
            author_link = article_site_link(link)
            post = article_post(soup)
            date = article_date(soup)
            text = article_text(soup)

            posts.append((name, username, profilePic, author_link, post, date, link, name + username + text))

            with open("articles.txt", "a") as f:

                f.writelines(['{\n',f'authorName: "{name}",\n',f'authorUsername: "{username}",\n',f'authorProfilePic: "{profilePic}",\n', f'authorLink: "{author_link}",\n', f'tweet: ({post}),\n', f'date: "{date}",\n', f'source: "{link}",\n', f'searchKeywords: "{name} {username} {text}"\n', '},\n'])
            

        for users in usernames:

            # Tweets
            c = twint.Config()
            username = users
            print(users)
            img = profile_images[usernames.index(users)]
            c.Username = username
            c.Limit = 1
            c.Custom["tweet"] = ["name", "username", "tweet", "link", "created_at"]
            c.Output = f"{username}.csv"
            c.Store_csv = True

            # Run
            twint.run.Search(c)

            # make the results
            with open(f'{username}.csv', 'r') as f:
                csv_reader = csv.reader(f)

                results = open(f'tweets.txt', 'a')

                for line in csv_reader:
                    name = line[0]
                    account_name = line[1]
                    tweet = f"<p>{line[2]}</p>"
                    source = line[3]
                    date = line[4]
                    link = "https://" + (urlparse(source).netloc) + "/" + account_name

                    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S UTC')
                    date = date.strftime("%d/%m/%Y")
                    
                    if(img == ""):
                        if(date == filter_date or filter_date == ""):
                            posts.append((name, account_name, "", link, tweet, date, source, name + username + text))
                        else:
                            continue
                    else:
                        if(date == filter_date or filter_date == ""):
                            posts.append((name, account_name, img, link, tweet, date, source, name + username + text))
                        else:
                            continue

        
        random.shuffle(posts)

        for element in posts:

            with open("results.txt", "a") as f:

                f.writelines(['{\n',f'authorName: "{element[0]}",\n',f'authorUsername: "{element[1]}",\n',f'authorProfilePic: "{element[2]}",\n', f'authorLink: "{element[3]}",\n', f'tweet: ({element[4]}),\n', f'date: "{element[5]}",\n', f'source: "{element[6]}",\n', f'searchKeywords: "{element[7]}"\n', '},\n'])

        

    elif(args[1] == "tweet"):

        #clean the results of the last scrape
        for file in usernames:
            with open(f"{file}.csv", "w"):
                pass

        with open("tweets.txt", "w"):
            pass

        #run
        try:
            tweet_post(args[2])
        except:
            tweet_post("")

    elif(args[1] == "clean"):
        #clean the results of the last scrape
        for file in usernames:
            with open(f"{file}.csv", "w"):
                pass

        with open("tweets.txt", "w"):
            pass

        #clean the results of the last scrape
        with open("articles.txt", "w"):
            pass
        


    else:
        print("Incorrect Syntax! \n article | link")


if __name__ == '__main__':

    main()
