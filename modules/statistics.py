# Machine Learning and Regression Library for crypto analysis
# Focus: Statistics
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

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
        ytrain = self.traindata
        xval = np.asarray([x for x in range(max(xtrain)+1,len(self.traindata) + len(self.valtime))])

        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()


        regression_model = LinearRegression()
        poly = PolynomialFeatures(degree = param.degree)
        xtrain_transform = poly.fit_transform(xtrain.reshape(-1, 1))
        xval_transform = poly.fit_transform(xval.reshape(-1, 1))
        regression_model.fit(xtrain_transform, np.asarray(ytrain).reshape(-1, 1))

        #Predict the training data prices and the validation data prices
        ytrain_learned = regression_model.predict(xtrain_transform)
        yval_learned = regression_model.predict(xval_transform)

        #Time interval for plotting is 100
        plotwin = 100

        #list of lists into list of integers
        ytrain_learned = [x[0] for x in ytrain_learned]
        yval_learned = [x[0] for x in yval_learned]
        #Fix the image size
        plt.rcParams["figure.figsize"]= param.figsize
        plt.plot([*xtrain, *xval][-plotwin:], [*ytrain_learned, *yval_learned][-plotwin:], color="red", label = "Predictied Price")

        plt.plot(xtrain[-plotwin:], ytrain[-plotwin:], color = "black", label = "Real Price")

        labels = self.traintime + self.valtime
        plt.axvline(x=len(xtrain)-1, color="blue", label="Prediction Starts")
        plt.xticks([*xtrain, *xval][-plotwin:], labels[-plotwin:], rotation='vertical')
        plt.locator_params(axis = 'x', nbins=min(len(labels), 20))
        plt.legend()
        plt.show()

'''
#Testing
import dataload as pulldata
test = pulldata.data('X:BTCUSD', 'hour', 1631310151000, "simpledata")
D = test.data
reg = Regression(D['trainprice'], D['traintime'], D['valtime'], "poly")

reg.result
'''