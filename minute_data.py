#!/usr/bin/python

import gdax
import csv
from datetime import datetime
import time

api_key = "2f10e98b932b2a516532602ca2905669"
api_secr = "vSU5bD0QloVJO59mjohtgvAK9yDbNcrNdg7BhhSVSvF4PuhnViuhKe6kA7vJtiHyqjrubu8JIAhwRconfvI8RA=="
api_pass = "b7acvrafset"

auth_client = gdax.AuthenticatedClient(api_key,api_secr,api_pass)

try:

    #Get Product Dicts
    btc = auth_client.get_product_order_book('BTC-USD', level=1)
    bch = auth_client.get_product_order_book('BCH-USD', level=1)
    eth = auth_client.get_product_order_book('ETH-USD', level=1)
    ltc = auth_client.get_product_order_book('LTC-USD', level=1)

    btc = btc["bids"]
    btc = btc[0]
    btc = btc[0]

    bch = bch["bids"]
    bch = bch[0]
    bch = bch[0]

    eth = eth["bids"]
    eth = eth[0]
    eth = eth[0]

    ltc = ltc["bids"]
    ltc = ltc[0]
    ltc = ltc[0]

    stamp = str(datetime.now())

    inputs = [stamp,btc,bch,eth,ltc]
    with open('data.csv', 'a') as d:
        writer = csv.writer(d)
        writer.writerow(inputs)

except:

    
    pass


