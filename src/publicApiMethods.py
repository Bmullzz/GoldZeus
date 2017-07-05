import requests


apiKey = ''


def get24hVolume():
    response = requests.get("https://poloniex.com/public?command=return24hVolume", auth=(apiKey))
    return response._content

def getTradeHistory():
    response = requests.get("https://poloniex.com/public?command=returnTradeHistory&currencyPair=USDT_ETH", auth=(apiKey))
    return response._content

def getChartData():
    response = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1498046400"
                            "&end=1498132800&period=1800", auth=(apiKey))
    return response._content

def getOrderBook():
    response = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_ETH", auth=(apiKey))
    return response._content

