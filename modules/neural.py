# Machine Learning Library for Crypto Analysis
# Focus: Neural Networks
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
#skikit Libraries

class nn:
    def __init__(self, traindata0, valdata0, traintime0, valtime0, method0):
        self.traindata = traindata0
        self.valdata = valdata0
        self.traintime = traintime0
        self.valtime = valtime0
        self.method = method0
        if (self.method == "lstm"):
            self.result = self.lstm_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+self.method+" Not Available")
    def lstm_(self):
        #enumerate hours/days
        xtrain = np.asarray([x for x in range(0,len(self.traindata))])
        ytrain = self.traindata
        xval = np.asarray([x for x in range(max(xtrain),len(self.traindata) + len(self.valdata)-1)])
        yval = np.asarray(self.valdata)

        regressor = Sequential()

        regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (xtrain.shape[1], 1)))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units = 50))
        regressor.add(Dropout(0.2))

        regressor.add(Dense(units = 1))

        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

        regressor.fit(xtrain, ytrain, epochs = 100, batch_size = 32)

        sc = MinMaxScaler(feature_range = (0, 1))
        training_set_scaled = sc.fit_transform(training_set)

        #Predict the training data prices and the validation data prices
        ytrain_learned = regression_model.predict(xtrain_transform)
        yval_learned = regressor.predict(X_test)


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