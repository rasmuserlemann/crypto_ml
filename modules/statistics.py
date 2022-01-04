# Machine Learning and Regression Library for crypto analysis
# Focus: Statistics
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

import modules.parameters as param

#skikit Libraries

class Statistics:
    def __init__(self, traindata0, traintime0, valtime0, method0):
        self.traindata = traindata0
        self.traintime = traintime0
        self.valtime = valtime0
        self.method = method0
        if (self.method == "arima"):
            self.result = self.arima_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+self.method+" Not Available")
    def arima_(self):
        #enumerate hours/days
        xtrain = np.asarray([x for x in range(0,len(self.traindata))])
        ytrain = pd.DataFrame(self.traindata)
        xval = np.asarray([x for x in range(max(xtrain)+1,len(self.traindata) + len(self.valtime))])
        rmean = ytrain.rolling(window=12).mean()
        #Make the time series stationary
        datastationary = ytrain-rmean

        #P-value to check if the time series is stationary
        if adfuller(datastationary.dropna())[1] > 0.05:
            print("Unable to make the time series stationary. Choose different settings.")

        model = ARIMA(datastationary, order=(2,1,2))
        results = model.fit()

        #Generate the predictions
        m = rmean[0].iloc[-1]
        yhat = results.forecast(steps=param.predlen)
        predictions = yhat+m

        #PD dataframe back to a list
        ytrain = ytrain[0].values.tolist()
        ytrain_pred = results.fittedvalues+rmean
        ytrain_pred = ytrain_pred[0].values.tolist()

        #Fix the image size
        plt.rcParams["figure.figsize"]= param.figsize
        plt.plot([*xtrain, *xval][-param.plotlen:], [*ytrain_pred, *predictions][-param.plotlen:], color="red", label = "Predictied Price")

        plt.plot(xtrain[-param.plotlen:], ytrain[-param.plotlen:], color = "black", label = "Real Price")

        labels = self.traintime + self.valtime
        plt.axvline(x=len(xtrain)-1, color="blue", label="Prediction Starts")
        plt.xticks([*xtrain, *xval][-param.plotlen:], labels[-param.plotlen:], rotation='vertical')
        plt.locator_params(axis = 'x', nbins=min(len(labels), 20))
        plt.legend()
        plt.show()

'''
#Testing
import parameters as param

import dataload as pulldata
test = pulldata.data('X:BTCUSD', 'hour', 1631310151000, "simpledata")
D = test.data
reg = Statistics(D['trainprice'], D['traintime'], D['valtime'], "arima")

reg.result
'''