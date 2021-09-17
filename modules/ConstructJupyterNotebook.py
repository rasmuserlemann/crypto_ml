import nbformat as nbf
import os
import sys

introduction_text = """\
## Introduction
"""

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


"""

regression_code = """\
reg = regression.Regression(data['trainprice'], data['valprice'], data['traintime'], data['valtime'], "poly")
reg.result
"""
