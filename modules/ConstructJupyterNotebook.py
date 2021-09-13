import nbformat as nbf
import os
import sys

introduction_text = """\
## blabla
"""

def introduction_code(datafile):
    return(
        """\
        import modules.regression as regression
        import modules.introduction as introduction

        import numpy as np
        import pandas as pd
        import os
        reldir = os.getcwd()
        path_to_data = os.path.join(reldir, 'data', '{}')
        data = pd.read_csv(path_to_data)

        test = introduction.intro(data, "simpleplot")
        test.plot
        """.format(datafile)
        )

regression_text = """\
## test regression predict
"""

regression_code = """\
3+3
"""
