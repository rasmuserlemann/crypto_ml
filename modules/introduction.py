# Machine Learning and Regression Library for crypto analysis
# Focus: Introduction
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
#skikit Libraries

class intro:
    def __init__(self, timevar0, data0, method0):
        self.data = data0
        self.method = method0
        self.timevar = timevar0

        if (self.method == "simpleplot"):
            self.plot = self.splot_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+ self.method +" Not Available")
    def splot_(self):
        xaxis = [x for x in range(len(self.data))]
        labels = self.timevar

        plt.rcParams["figure.figsize"]=10,10

        plt.plot(xaxis, self.data, color = "black", label = "Real Price")
        plt.xticks(xaxis, labels, rotation='vertical')
        plt.locator_params(axis = 'x', nbins=min(len(labels), 20))
        plt.legend()


