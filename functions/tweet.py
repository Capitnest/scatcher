import twint
import csv
import datetime

# generate the information necessary for a post from the latest 10 tweets of a user
def tweet_post(username):

    # Tweets
    c = twint.Config()
    c.Username = username
    c.Limit = 1
    c.Custom["tweet"] = ["name", "username", "tweet", "link", "created_at"]
    c.Output = "tweets.csv"
    c.Store_csv = True

    # Run
    twint.run.Search(c)

    # make the results
    with open('tweets.csv', 'r') as f:
        csv_reader = csv.reader(f)

        results = open('results.txt', 'a')

        for line in csv_reader:
            name = line[0]
            account_name = line[1]
            tweet = line[2]
            source = line[3]
            date = line[4]

            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S UTC')
            date = date.strftime("%d/%m/%Y")
            

            lines = ["\n{\nauthorName:",f'"{name}",\nauthorUsername: "{account_name}",\ntweet: (<p>{tweet}</p>),\nsource:"{source}",\ndate: "{date}"\n',"},"]
            results.writelines(lines)