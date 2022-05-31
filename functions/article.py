from urllib.parse import urlparse
import datetime

# get the name of the website that the article is published on
def article_site_name(soup):
    for tag in soup.find_all('meta'):
        if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['og:site_name', 'keywords']:
            return tag.attrs['content']
    
# get the base domain url of the website
def article_site_name_url(source):
    return (urlparse(source).netloc)

# get the favicon / logo of the website that the article is published on
def article_site_logo_url(soup):
    return soup.find("link", rel="icon")["href"]

# get the link of the website that the article is published on
def article_site_link(source):
    return (urlparse(source).netloc)

# create a basic html post based on the article's title, description & image
def article_post(soup):

    title = ""
    description = ""
    image = ""

    for tag in soup.find_all('meta'):

        # get the title of the article
        if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['og:title', 'keywords']:
            title = tag.attrs['content']

        # get the description of the article
        elif 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['og:description', 'keywords']:
            description = tag.attrs['content']

        # get the image of the article
        elif 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['og:image', 'keywords']:
            image = tag.attrs['content']

    # formulate the basic html for the post
    html = f"""<p>{title}<img src="{image}" alt="article image"/>{description}</p>"""

    return html

# get the date when the article was published
def article_date(soup):
    date = ""
    try:
        for tag in soup.find_all('meta'):
            if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['article:published_time', 'keywords']:
                date = tag.attrs['content']


        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return date.strftime("%m/%d/%Y")
    except:
        return ""