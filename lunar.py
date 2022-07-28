#revers engineers the api from lunarcrush.com
#takes all the data from them and puts them into a json file
#then we use that data as ours
import requests
import json

URL = "https://api2.lunarcrush.com/v2?data=global&data_points=7&interval=day&change=1w"

def lunar_global():
 
    response = requests.get(URL).json()

    with open(f'data/social_global.json', "w") as f:
        json.dump(response['data'], f)

if __name__ == "__main__":

   lunar_global()