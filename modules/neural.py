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
import parameters as param

#skikit Libraries

class nn:
    def __init__(self, traindata0, traintime0, valtime0, method0):
        self.traindata = traindata0
        self.traintime = traintime0
        self.valtime = valtime0
        self.method = method0
        if (self.method == "lstm"):
            self.result = self.lstm_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Neural Networks Method "+ self.method +" Not Available")

    def lstm_(self):
        #Abort if the training period is less than 100 units
        if len(self.traintime)<100:
            return("The time period is too short. Training period has to be more than 100 time units")

        #Parameters
        epochs = param.epochs
        batch_size = param.batch_size
        sliding_window = param.sliding_window


        #enumerate hours/days and define data variables
        xtrain = np.asarray([x for x in range(0,len(self.traindata))])
        ytrain = np.asarray(self.traindata)
        xval = np.asarray([x for x in range(max(xtrain)+1,len(self.traindata) + len(self.valtime))])

        #Scale the data
        sc = MinMaxScaler()
        training_set_scaled = sc.fit_transform(ytrain.reshape(-1,1))

        #Create the sliding windows
        X_train = []
        y_train = []
        for i in range(sliding_window, len(training_set_scaled)):
            X_train.append(training_set_scaled[i-sliding_window:i])
            y_train.append(training_set_scaled[i])
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))


        #Model
        regressor = Sequential()

        regressor.add(LSTM(units = 50, return_sequences = True, input_shape =  (X_train.shape[1], 1)))
        regressor.add(Dropout(param.dropout))

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(param.dropout))

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(param.dropout))

        regressor.add(LSTM(units = 50))
        regressor.add(Dropout(param.dropout))

        regressor.add(Dense(units = 1))

        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

        regressor.fit(X_train, y_train, epochs = epochs, batch_size = batch_size, verbose=0)

        #Create the test data set and use the model for predicting 100 hours/days
        inputs_standard = ytrain
        inputs = inputs_standard.reshape(-1,1)
        inputs = sc.transform(inputs)
        X_test = []
        for i in range(sliding_window,len(ytrain)):
            X_test.append(inputs[i-sliding_window:i])

        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        predicted_price_scaled = regressor.predict(X_test)

        #Scale back the training data predicted price
        predicted_price = sc.inverse_transform(predicted_price_scaled)
        nopred = inputs_standard[0:sliding_window]
        predicted_price = np.insert(predicted_price, 0, nopred)

        #Take last sliding window number of elements and do predictions one by one
        lastwindow = X_test[-1:]
        ytemp = inputs[-sliding_window:]
        predictions = []
        for i in range(5):
            pred = regressor.predict(lastwindow)
            predictions.append(float(sc.inverse_transform(pred)[0]))
            ytemp = np.delete(ytemp,0)
            ytemp = np.insert(ytemp, len(ytemp), float(pred))
            ytemp = [ytemp]
            ytemp = np.array(ytemp)
            lastwindow = np.reshape(ytemp, (ytemp.shape[0], ytemp.shape[1], 1))

        #Figure size
        plt.rcParams["figure.figsize"]= param.figsize
        #X-axis for the plot
        xaxis100 = [x for x in range(100)]
        #Plot
        plt.plot(xaxis100, [*predicted_price[-95:], *predictions], color = "red", label = "Predicted Price")
        plt.plot(xaxis100[0:95], ytrain[-95:], color = "black", label = "Real Price")
        plt.axvline(x=94, color="blue", label="Prediction Starts")
        #Change the x axis to time ticks
        labels = self.traintime + self.valtime
        plt.xticks(xaxis100, labels[-100:], rotation='vertical')
        plt.locator_params(axis = 'x', nbins=min(len(labels), 20))

        plt.legend()
        plt.show()




#Testing
import dataload as pulldata
test = pulldata.data('X:BTCUSD', 'day', 1611512638000, "simpledata")
D = test.data
lstm = nn(D['trainprice'], D['traintime'], D['valtime'], "lstm")

#lstm.result
