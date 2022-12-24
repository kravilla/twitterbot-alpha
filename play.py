import tweepy
import requests

api_key = "to8oubDuLRGEVVqoFrq4eFu6d"
api_secret = "9OIpv8WrDZrNlMgNS1eeSq1rE6F3Fja0P9Ka93mip2BMcI8p6y"
access_token = "1582583112910905345-lqXPBzLZCAWjcRv30LWpsmmP1QaGtW"
access_token_secret = "xJJ7PzL1QfDKmxilI17mDKSJTA9uCdceh18BbViFQnTEx"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM5WiQEAAAAADvI3OTgh5U12QyDt8AAqhQmtFt0%3D2CGlM3beptLGHu5TrkJGDgZzc5gkceeDt5KSHI9WpWVH2ldmdM"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
global last_eth_price 
global last_btc_price

last_btc_price = 1000.0
last_eth_price = 1000.0
prices = [10,10]

def post_tweet(val):
    global last_eth_price
    global last_btc_price
    global eth_price 
    global btc_price
    eth_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').json()['ethereum']['usd']
    btc_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()['bitcoin']['usd']
    eth_change = format(((eth_price - val[0])/val[0]) * 100, ".2f")
    btc_change = format(((btc_price - val[1])/val[1]) * 100, ".2f")
    message = 'The current ETH price is $' + str(eth_price) + ' USD with a ' + str(eth_change) + '%' + ' change in the last 24 hours. The current BTC price is $' + str(btc_price) + ' USD with a ' + str(btc_change) + '%' + ' change in the last 24 hours. Comment thoughts and observations below!'
    val[0] = eth_price
    val[1] = btc_price
    api.update_status(message)
    print('successful')
    return val

prices = post_tweet(prices)
print(prices[0])