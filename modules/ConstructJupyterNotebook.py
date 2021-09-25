import nbformat as nbf
import os
import sys

def introduction_text(crypto, from_, to):
    return(
        """\
## Introduction

This report will analyze {} data from the starting time of {} to the end time of {}. First we will plot the price data from the starting time to the end time.
        """.format(crypto, from_, to)
        )

def introduction_code(crypto, timeint, from_):
    return(
        """\
        import modules.regression as regression
        import modules.neural as neural
        import modules.introduction as introductionA
        import modules.dataload as dataload
        import numpy as np
        import pandas as pd
        import os

        crypto = {}
        timeint = {}
        from_ = {}

        getdata = dataload.data(crypto, timeint, from_, "simpledata")
        data = getdata.data
        test = introductionA.intro(data['traintime'], data['trainprice'], "simpleplot")
        test.plot
        """.format(crypto, timeint, from_)
        )

regression_text = """\
## Polynomial Regression
Polynomial regression is a classical supervised approach for predicting price. It fits a nonlinear line between the relationship of features and price. The type of nonlinear line depends on the data. We generally use a polynomial curve with a degree between $5$ and $10$.

"""

regression_code = """\
reg = regression.Regression(data['trainprice'], data['traintime'], data['valtime'], "poly")
reg.result
"""

nn_text = """\
## Long Short Term Memory (LSTM)
LSTM is one of the most widely used deep learning algorithms for predicting price changes. It's designed to take a sequence of data points as an input and make a prediction from it. The model is trained on a series of sliding windows.

The plot displays only the last $100$ time moments with the real price and the predicted price.

"""

nn_code = """\
neuralnetwork = neural.nn(data['trainprice'], data['traintime'], data['valtime'], "lstm")
neuralnetwork.result
"""
