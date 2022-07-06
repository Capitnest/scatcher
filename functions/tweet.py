import twint
import csv
import datetime
from urllib.parse import urlparse
from data.tweets import usernames
from data.tweets import profile_images

# generate the information necessary for a post from the latest 10 tweets of a user
# filter_date - choose what date to use to filter through the tweets
def tweet_post(filter_date):

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
                tweet = line[2]
                source = line[3]
                date = line[4]
                link = "https://" + (urlparse(source).netloc) + "/" + account_name

                date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S UTC')
                date = date.strftime("%d/%m/%Y")
                
                if(img == ""):
                    lines = ["\n{\nauthorName:",f'"{name}",\nauthorUsername: "@{account_name}",\nauthorLink: "{link}",\ntweet: (<p>{tweet}</p>),\nsource:"{source}",\ndate: "{date}",\nsearchKeywords: "{name} {account_name} {tweet}"\n',"},"]
                else:
                    lines = ["\n{\nauthorName:",f'"{name}",\nauthorUsername: "@{account_name}",\nauthorProfilePic: "{img}",\nauthorLink: "{link}",\ntweet: (<p>{tweet}</p>),\nsource:"{source}",\ndate: "{date}",\nsearchKeywords: "{name} {account_name} {tweet}"\n',"},"]

                
                if(date == filter_date or filter_date == ""):
                    results.writelines(lines)
                else:
                    continue