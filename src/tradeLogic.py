import requests
import publicApiMethods
import privateApiMethods

apiKey = ''
secret = ''


#def main():

    # response = requests.get("https://poloniex.com/public?command=returnOrderBook", auth=(apiKey, secret))

    #print (poloniex.returnOrderBook('BTC_ETH&depth=10'))
    #print get24hVolume()
    # print response._content
    # print response.status_code
    # print response.json()




if __name__=="__main__":

    print "24 hour Volume: \n" + publicApiMethods.get24hVolume() + "\n"

    print "Trade History: \n" + publicApiMethods.getTradeHistory("USDT_ETH") + "\n"

    print "24 hour chart data: \n" + publicApiMethods.getChartData("USDT_ETH", "1498132800", "1498219200", "1800") + "\n"

    print "Order Book: \n" + publicApiMethods.getOrderBook() + "\n"

    print privateApiMethods.buy()




