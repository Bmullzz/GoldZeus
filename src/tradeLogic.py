
import publicApiMethods
import privateApiMethods
import poloniexWrapper
import apiKeys
import json

APIKey = apiKeys.APIKey
Secret = apiKeys.Secret

rapper = poloniexWrapper.poloniex(APIKey, Secret)


if __name__=="__main__":


    # with open('tickerData.txt', 'w') as outfile:
    #     json.dumps(rapper.returnTicker(), outfile)
    print "Ticker: \n"
    print rapper.returnTicker()
    print "\n"

    print "24 hr Volume: \n"
    print rapper.return24Volume()
    print "\n"

    print "Trade History: \n" + publicApiMethods.getTradeHistory("USDT_ETH") + "\n"

    print "24 hour chart data: \n" + publicApiMethods.getChartData("USDT_ETH", "1498132800", "1498219200", "1800") + "\n"

    print "Order Book: \n" + publicApiMethods.getOrderBook("USDT_ETH") + "\n"

    print privateApiMethods.buy()




