# Data loading Library for Cryptocurrency Research
# Focus: Loading data by using Polygon.io API
# Author: Rasmus Erlemann
# Last Update: 2021/09/17

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polygon import RESTClient
import time
from datetime import datetime

class data:
    def __init__(self, crypto0, time_interval0, start0, end0, method0):
        self.method = method0
        self.start = start0
        self.end = end0
        self.crypto = crypto0
        self.time_interval = time_interval0

        if (self.method == "simpledata"):
            self.data = self.polygonAPI()
    def polygonAPI(self):
        apikey = "lZfT8HmZUt6dTWHbSM44V477wvU7JHCC"
        with RESTClient(apikey) as client:
            ticker = self.crypto
            multiplier = 1
            timespan = self.time_interval

            #Take the end data and add 1 day or 7 days (depending on the time interval)
            #The extra 1 day or 7 days will be used to validate the results
            now = datetime.now()
            unixnow = int(time.mktime(now.timetuple()))*1000
            if self.time_interval == "hour":
                to = min(self.end + 86400000, unixnow)
                trainend = self.end
            if self.time_interval == "day":
                to = min(self.end + 604800000, unixnow)
                trainend = self.end
            #86400000 is equal to 1 day
            #604800000 is equal to 7 days
            #valvar is the length of the validation period

            from_ = self.start

            resp = client.crypto_aggregates(ticker, 1, timespan, from_, to)
            trainclose = []
            traindate = []
            valclose = []
            valdate = []

            for d in range(len(resp.results)):
                s = resp.results[d]['t']
                if s < trainend:
                    trainclose.append(resp.results[d]['c'])
                    traindate.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s/1000.0)))
                if s >= trainend:
                    valclose.append(resp.results[d]['c'])
                    valdate.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s/1000.0)))
                #Divide by 1000 as the function doesn't want milliseconds
            return({"traintime": traindate, "valtime": valdate, "trainprice": trainclose, "valprice": valclose})




test = data('X:BTCUSD', 'hour', 1631646542000, 1631738736000, "simpledata")
T = test.data

