# Data loading Library for Cryptocurrency Research
# Focus: Loading data by using Polygon.io API
# Author: Rasmus Erlemann
# Last Update: 2021/09/17

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polygon.rest import RESTClient
import time
from datetime import datetime

class data:
    def __init__(self, crypto0, time_interval0, start0, method0):
        self.method = method0
        self.start = start0
        self.crypto = crypto0
        self.time_interval = time_interval0

        if (self.method == "simpledata"):
            self.data = self.polygonAPI()
    def polygonAPI(self):
        apikey = "lZfT8HmZUt6dTWHbSM44V477wvU7JHCC"

        predlen = 5

        with RESTClient(apikey) as client:
            ticker = self.crypto
            multiplier = 1

            now = datetime.now()
            unixnow = int(time.mktime(now.timetuple()))*1000

            if self.time_interval == "hour":
                valjump = 3600000
                to = unixnow + 18000000 + valjump*predlen
                trainend = unixnow
            if self.time_interval == "day":
                valjump = 86400000
                to = unixnow + valjump*predlen
                trainend = unixnow

            valticks = predlen
            #18000000 is equal to 5 hours and 3600000 1 hour
            #432000000 is equal to 5 days and 86400000 1 day

            resp = client.crypto_aggregates(ticker=ticker, multiplier=1, timespan=self.time_interval, from_=self.start, to=trainend, sort='asc', limit=50000)
            trainclose = []
            traindate = []
            valdate = []

            for d in range(len(resp.results)):
                s = resp.results[d]['t']
                if s < trainend:
                    trainclose.append(resp.results[d]['c'])
                    traindate.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s/1000.0)))
            for el in range(1,valticks+1):
                timemoment = unixnow + valjump*el
                valdate.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timemoment/1000.0)))
                #Divide by 1000 as the function doesn't want milliseconds
            return({"traintime": traindate, "valtime": valdate, "trainprice": trainclose})


'''
test = data('X:BTCUSD', 'hour', 1631646542000, 1632490300000, "simpledata")
T = test.data
'''
