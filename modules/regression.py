# Machine Learning and Regression Library for crypto analysis
# Focus: Regression
# Author: Rasmus Erlemann
# Last Update: _

#Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#skikit Libraries

class Regression:
    def __init__(self, data0, method0):
        self.data = data0
        self.method = method0
        if (self.method == "linear"):
            self.linear = self.linear_()
        #elif (self.method == "hierarchical"):
            #self.cluster = self.hierarchical_()
        else:
            print("Regression method "+self.method+" Not Available")
    #def linear_(self):

