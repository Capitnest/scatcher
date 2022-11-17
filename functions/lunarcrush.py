import requests

def get_info(url):
    URL = url
    response = requests.get(URL).json()

    return response

def nft_of_the_day():
    return get_info("https://lunarcrush.com/api3/nftoftheday")

def nft_of_the_day_info():
    return get_info("https://lunarcrush.com/api3/nftoftheday/info")

def coin_of_the_day():
    return get_info("https://lunarcrush.com/api3/coinoftheday")

def coin_of_the_day_info():
    return get_info("https://lunarcrush.com/api3/coinoftheday/info")

def stock_of_the_day():
    return get_info("https://lunarcrush.com/api3/stockoftheday")

def stock_of_the_day_info():
    return get_info("https://lunarcrush.com/api3/stockoftheday/info")