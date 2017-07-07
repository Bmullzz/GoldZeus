
import publicApiMethods
import privateApiMethods
import poloniexWrapper




rapper = poloniexWrapper.poloniex(APIKey, Secret)


if __name__=="__main__":



    print rapper.returnTicker()
        # print(keys)
        # print(values)



    print "Trade History: \n" + publicApiMethods.getTradeHistory("USDT_ETH") + "\n"

    print "24 hour chart data: \n" + publicApiMethods.getChartData("USDT_ETH", "1498132800", "1498219200", "1800") + "\n"

    print "Order Book: \n" + publicApiMethods.getOrderBook("USDT_ETH") + "\n"

    print privateApiMethods.buy()




