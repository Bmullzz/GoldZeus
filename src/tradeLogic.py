import requests
import publicApiMethods

apiKey = ''
secret = ''


#def main():

    # response = requests.get("https://poloniex.com/public?command=returnOrderBook", auth=(apiKey, secret))

    #print (poloniex.returnOrderBook('BTC_ETH&depth=10'))
    #print get24hVolume()
    # print response._content
    # print response.status_code
    # print response.json()

# if __name__ == "__main__":
#     main()
#     get24hVolume()

#public gets
# def selectUrlCall():
#
#
# def get24hVolume():
#     response = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_ETH", auth=(apiKey, secret))
#     return response._content



if __name__=="__main__":
    #main()

    print "24 hour Volume: \n" + publicApiMethods.get24hVolume() + "\n"

    print "Trade History: \n" + publicApiMethods.getTradeHistory() + "\n"

    print "24 hour chart data: \n" + publicApiMethods.getChartData() + "\n"

    print "Order Book: \n" + publicApiMethods.getOrderBook() + "\n"

#
# def getOrderBook():
#
#
# def getTradeHistory():
#
#
# def getChartData():
#
#
# #Private api calls
# def buy():
#
#
# def sell():
#
#
# def


