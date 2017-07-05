import requests


apiKey = ''

def apiQuery(command):
    if command == "return24hVolume":
        response = requests.get("https://poloniex.com/public?command=" + command, auth=(apiKey))
        return response._content


def get24hVolume():
    response = requests.get("https://poloniex.com/public?command=return24hVolume", auth=(apiKey))
    return response._content


def getTradeHistory(currencyPair):
    response = requests.get("https://poloniex.com/public?command=returnTradeHistory&currencyPair="
                            + currencyPair, auth=(apiKey))
    return response._content


def getChartData(currencyPair, startTime, endTime, period):
    response = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=" +
                            currencyPair +
                            "&start=" + startTime +
                            "&end=" + endTime + "&period=" + period, auth=(apiKey))
    return response._content


def getOrderBook():
    response = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_ETH", auth=(apiKey))
    return response._content

