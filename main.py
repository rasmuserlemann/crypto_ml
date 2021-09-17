import nbformat as nbf
import os
import time
import sys
import uuid
import modules.ConstructJupyterNotebook as Jup
from nbconvert.preprocessors import ExecutePreprocessor

#For testing, use the command: py main.py 'X:BTCUSD' 'hour' 1630454400000 1631577600000
#Train on 2021 1. Sept to 14. Sept

#Read in data location as an argument in terminal
crypto, timeint, from_, to = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

nb = nbf.v4.new_notebook()

#Combine jupyter notebook text and code cells
nb['cells'] = [
               nbf.v4.new_markdown_cell(Jup.introduction_text), nbf.v4.new_code_cell(Jup.introduction_code(crypto, timeint, from_, to)),
               nbf.v4.new_markdown_cell(Jup.regression_text), nbf.v4.new_code_cell(Jup.regression_code)
               ]

#New folder with a unique name
folder_name = 'Analysis_' + time.strftime("%Y_%m_%d_%H_%M_%S") + "_" + str(uuid.uuid4())
os.mkdir(folder_name)

#Make src folder and copy the python files
os.mkdir(folder_name + '\\src')
os.mkdir(folder_name + '\\src\\modules')
os.system('copy modules\\introduction.py ' + folder_name + '\\src\\modules')
os.system('copy modules\\regression.py ' + folder_name + '\\src\\modules')

os.mkdir(folder_name + '\\results')

#Generate jupyter notebook
with open(folder_name + '\\src\\report.ipynb', 'w') as f:
    nbf.write(nb, f)

with open(folder_name + '\\src\\report.ipynb') as f:
    nb = nbf.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {})
with open(folder_name + '\\src\\report_executed.ipynb', 'wt') as f:
    nbf.write(nb, f)

#Generate html report
os.system('jupyter nbconvert --output-dir=' + folder_name + '\\results --to HTML --output report.html --no-input ' + folder_name + '\\src\\report_executed.ipynb' )
#Generate pdf report
os.system('jupyter nbconvert --output-dir=' + folder_name + '\\results --to PDF --output report.pdf --no-input ' + folder_name + '\\src\\report_executed.ipynb' )
