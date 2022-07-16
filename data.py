import requests
import datetime

root_url = "https://api.binance.com/api/v3/klines"


def get_data(coinSymbol, timeInterval, quantity):
    r = requests.get(root_url + "/api/v3/klines", params=({"symbol":coinSymbol, "interval":timeInterval, "limit":quantity}))
    data = r.json()

    mydict = {}
    counter = len(data)
    for i in data:
        temp = {}
        temp["open time"] = datetime.datetime.fromtimestamp(int(i[0]) // 1000)
        temp["open"] =i[1]
        temp["high"] =i[2]
        temp["low"] =i[3]
        temp["close"] =i[4]
        temp["volume"] =i[5]
        temp["close time"] =datetime.datetime.fromtimestamp(int(i[6]) // 1000)
        temp["quote asset volume"] =i[7]
        temp["number of trades"] =i[8]
        temp["taker buy base asset volume"] =i[9]
        temp["taker buy quote asset volume"] =i[10]
        temp["ignore"] =i[11]
        mydict[counter] = temp
        counter -= 1

    return mydict




