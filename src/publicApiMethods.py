import requests
import json
import time


apiKey = ''

def createTimeStamp(dateString, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(dateString, format))

# def apiQuery(command):
#     if command == "return24hVolume":
#         response = requests.get("https://poloniex.com/public?command=" + command)
#         data = response.json()
#         return data


def get24hVolume():
    response = requests.get("https://poloniex.com/public?command=return24hVolume")
    data = response.json()
    return data


def getTradeHistory(currencyPair):
    response = requests.get("https://poloniex.com/public?command=returnTradeHistory&currencyPair="
                            + currencyPair)
    return response.content


def getChartData(currencyPair, startTime, endTime, period):
    response = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=" +
                            currencyPair +
                            "&start=" + startTime +
                            "&end=" + endTime + "&period=" + period)
    return response.content


def getOrderBook(currencyPair):
    response = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=" + currencyPair)
    return response.content

# with open('24hVolumeData.txt', 'w') as outfile:
#     get24hVolume().dump(data, outfile)