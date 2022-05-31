# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import urllib
import sys
from typing import List

from functions.article import *
from functions.tweet import *

args : List[str] = sys.argv
link = ""

# simulating normal headers from a browser, so it will not to be detected as a bot by some website
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def main():

    link = args[2]

    if(args[1] == "article"):
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, features="lxml")

        name = article_site_name(soup)
        username = article_site_name_url(link)
        profilePic = article_site_logo_url(soup)
        author_link = article_site_link(link)
        post = article_post(soup)
        date = article_date(soup)

        print('{')
        print(f'authorName: "{name}",')
        print(f'authorUsername: "{username}",')
        print(f'authorProfilePic: "{profilePic}",')
        print(f'authorLink: "{author_link}",')
        print(f'tweet: ({post}),')
        print(f'date: "{date}",')
        print(f'source: "{link}",')
        print('},')

    else:
        print("Incorrect Syntax! \n article | link")


if __name__ == '__main__':

    main()