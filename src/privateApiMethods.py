import requests

apiKey = ''
secret = ''

def buy():
    response = requests.post("https://poloniex.com/tradingApi?command=returnBalances", auth=(apiKey, secret))
    return response