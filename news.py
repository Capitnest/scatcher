# This part of the scraper that scrapes the internet for news from different news websites
# We use the usearch.com api to scrape the internet for news about crypto

#The code was copied from the template that can be found here 
# https://rapidapi.com/contextualwebsearch/api/web-search/tutorials/using-python-to-call-the-search-apis

import requests
import json
from urllib.parse import urlparse
import sys
from typing import List

args : List[str] = sys.argv

# The way we get the first 20 characters of the body to create the description 
# is by taking the first x words and putting them in a array
# This function transforms that array in a readeble sentence
def format_description(desc):
    string = ""
    for i in desc:
        
        string+= i + " "

    l = len(string)

    string = string[:l-1]

    string += "..."

    return string

URL = "https://rapidapi.p.rapidapi.com/api/search/NewsSearchAPI"
HEADERS = {
    "x-rapidapi-host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
    "x-rapidapi-key": "9a98b0c887mshd6519308be9ec06p17460fjsnfef70e98b03b"
}

def news_articles(topic, from_published_date = ""):

    query = str(topic)
    page_number = 1
    page_size = 50
    auto_correct = True
    safe_search = False
    with_thumbnails = True
    to_published_date = ""

    querystring = {"q": query,
                "pageNumber": page_number,
                "pageSize": page_size,
                "autoCorrect": auto_correct,
                "safeSearch": safe_search,
                "withThumbnails": with_thumbnails,
                "fromPublishedDate": from_published_date,
                "toPublishedDate": to_published_date}

    response = requests.get(URL, headers=HEADERS, params=querystring).json()

    total_count = response["totalCount"]

    data = {}
    index = 55

    #loop through the every article
    for web_page in response["value"]:

        #the data that we need from the article
        name = web_page["provider"]["name"]
        username = urlparse(web_page["url"]).netloc
        profile_pic_url = web_page["provider"]["favIcon"]
        author_url = f"https://{urlparse(web_page['url']).netloc}/"
        title = web_page["title"]
        thumbnail = web_page["image"]["thumbnail"]
        description = format_description(web_page['body'].split()[:25])
        date = web_page["datePublished"]
        source = web_page["url"]

        #put all the data in a dictionary
        article = {f"{index}" : {"name": name, "username": username, "profile": profile_pic_url, "user_url": author_url , "title": title, "picture": thumbnail, "description": description, "date": date, "source": source}}
        data.update(article)

        #move the index 
        index += 1
        


    # write the data on the json file
    with open(f'results/news_{topic}.json', "w") as f:
        json.dump(data, f)


if __name__ == "__main__":

    try:
        try:
            news_articles(args[1], args[2])
        except:
            news_articles(args[1])
    except:
        print("Error! Please specify a topic to search about!s")