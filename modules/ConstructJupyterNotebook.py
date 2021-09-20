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

def introduction_code(crypto, timeint, from_, to):
    return(
        """\
        import modules.regression as regression
        import modules.introduction as introductionA
        import modules.dataload as dataload
        import numpy as np
        import pandas as pd
        import os

        crypto = {}
        timeint = {}
        from_ = {}
        to = {}

        getdata = dataload.data(crypto, timeint, from_, to, "simpledata")
        data = getdata.data
        test = introductionA.intro(data['traintime'], data['trainprice'], "simpleplot")
        test.plot
        """.format(crypto, timeint, from_, to)
        )

regression_text = """\
## Polynomial Regression
Polynomial regression is a classical supervised approach for predicting price. It fits a nonlinear line between the relationship of features (time, ...) and price.

"""

regression_code = """\
reg = regression.Regression(data['trainprice'], data['valprice'], data['traintime'], data['valtime'], "poly")
reg.result
"""
