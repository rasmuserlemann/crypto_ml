# Machine Learning and Regression Library for crypto analysis
# Focus: Introduction
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#skikit Libraries

class intro:
    def __init__(self, data0, method0):
        self.data = data0
        self.method = method0

        if (self.method == "simpleplot"):
            self.plot = self.splot_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+self.method+" Not Available")
    def splot_(self):
        price = self.data.loc[:, "PriceUSD"]
        dates = self.data.loc[:, "date"]
        plt.plot(dates, price)

