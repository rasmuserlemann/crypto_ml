# Machine Learning and Regression Library for crypto analysis
# Focus: Regression
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
#skikit Libraries

class Regression:
    def __init__(self, traindata0, valdata0, traintime0, valtime0, method0):
        self.traindata = traindata0
        self.valdata = valdata0
        self.traintime = traintime0
        self.valtime = valtime0
        self.method = method0
        if (self.method == "poly"):
            self.result = self.poly_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+self.method+" Not Available")
    def poly_(self):
        #enumerate hours/days
        xtrain = np.asarray([x for x in range(0,len(self.traindata))])
        ytrain = self.traindata
        xval = np.asarray([x for x in range(max(xtrain),len(self.traindata) + len(self.valdata)-1)])
        yval = np.asarray(self.valdata)

        regression_model = LinearRegression()
        poly = PolynomialFeatures(degree = 5)
        xtrain_transform = poly.fit_transform(xtrain.reshape(-1, 1))
        xval_transform = poly.fit_transform(xval.reshape(-1, 1))
        regression_model.fit(xtrain_transform, np.asarray(ytrain).reshape(-1, 1))

        #Predict the training data prices and the validation data prices
        ytrain_learned = regression_model.predict(xtrain_transform)
        yval_learned = regression_model.predict(xval_transform)

        #list of lists into list of integers
        ytrain_learned = [x[0] for x in ytrain_learned]
        yval_learned = [x[0] for x in yval_learned]

        #Fix the image size
        plt.rcParams["figure.figsize"]=10,10

        plt.plot(xtrain, ytrain_learned, color="blue", label = "Training Prediction Price")
        plt.plot(xval, yval_learned, color="red", label = "Predicted Price")

        plt.plot(xtrain, ytrain, color = "black", label = "Real Price")
        plt.plot(xval, yval, color = "green", label = "Real Price for Validation")

        labels = self.traintime + self.valtime
        plt.xticks([*xtrain, *xval], labels, rotation='vertical')
        plt.locator_params(axis = 'x', nbins=min(len(labels), 20))

        plt.legend()
        plt.show()

'''
#Testing
import dataload as pulldata
test = pulldata.data('X:BTCUSD', 'hour', 1631646542000, 1631738736000, "simpledata")
D = test.data
reg = Regression(D['trainprice'], D['valprice'], D['traintime'], D['valtime'], "poly")

reg.result
'''