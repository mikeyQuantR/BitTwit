import requests as rq
import json
import time

'''

Price collector for BitTwit application

This program runs every 24 hrs and collects $BTC price data from the previous day via BitcoinAverage API.
Price data (by minute) is written into a txt file and stored in \prices.

Genesis: 00:00 UTC 00/09/2017 (03:00 am GMT+2)

'''


def pull_price(date):

    file = open('.\prices\{0}_{1}_{2}.txt'.format(date.tm_mday, date.tm_mon, date.tm_year), 'w+')
    r = rq.get('https://apiv2.bitcoinaverage.com/indices/global/history/BTCEUR?period=daily')
    resp_dict = json.loads(r.text)

    i = 0
    pricelist = []
    while True:
        try:
            str_price = str(resp_dict[i]['average']) + ','
            str_datetime = str(resp_dict[i]['time'])
            str_time = str_datetime[11:] + '\n'
            glu = str_price+str_time
            pricelist.append(glu)
            i += 1
        except:
            break

    file.writelines(pricelist)
    file.close()
