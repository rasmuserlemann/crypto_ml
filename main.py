import nbformat as nbf
import os
import time
from datetime import datetime

import sys
import uuid
import modules.ConstructJupyterNotebook as Jup
from nbconvert.preprocessors import ExecutePreprocessor
from auth import check

import time
from datetime import datetime

#For testing, use the command: py main.py 'X:BTCUSD' 'day' 1609477200000 123456

#Read in data location as an argument in terminal
crypto, timeint, from_, code= sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

#If the authorization code is not correct, exit the script
if code == False:
    exit()

#Current time in unix timestamp (milliseconds)
now = datetime.now()
unixnow = int(time.mktime(now.timetuple()))*1000

#Text variables
if crypto == "'X:BTCUSD'": cryptoname = "Bitcoin (BTC)"
if crypto == "'X:ETHUSD'": cryptoname = "Ethereum (ETH)"
if crypto == "'X:ADAUSD'": cryptoname = "Cardano (ADA)"
starttime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(from_)/1000))
endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(unixnow)/1000))

#Open a notebook
nb = nbf.v4.new_notebook()

#Combine jupyter notebook text and code cells
nb['cells'] = [
               nbf.v4.new_markdown_cell(Jup.introduction_text(cryptoname, starttime, endtime)), nbf.v4.new_code_cell(Jup.introduction_code(crypto, timeint, from_)),
               nbf.v4.new_markdown_cell(Jup.nn_text), nbf.v4.new_code_cell(Jup.nn_code),
               nbf.v4.new_markdown_cell(Jup.regression_text),
                nbf.v4.new_code_cell(Jup.regression_code),
               nbf.v4.new_markdown_cell(Jup.stat_text), nbf.v4.new_code_cell(Jup.stat_code),
               ]

#New folder with a unique name
folder_name = 'Analysis_' + time.strftime("%Y_%m_%d_%H_%M_%S") + "_" + str(uuid.uuid4())
os.mkdir(folder_name)

#Make src folder and copy the python files
os.mkdir(folder_name + '\\src')
os.mkdir(folder_name + '\\src\\modules')
os.system('copy modules\\introduction.py ' + folder_name + '\\src\\modules')
os.system('copy modules\\parameters.py ' + folder_name + '\\src\\modules')
os.system('copy modules\\regression.py ' + folder_name + '\\src\\modules')
os.system('copy modules\\neural.py ' + folder_name + '\\src\\modules')

#Generate the notebook
with open(folder_name + '\\src\\report.ipynb', 'w') as f:
    nbf.write(nb, f)

#Execute the notebook
with open(folder_name + '\\src\\report.ipynb') as f:
    nb = nbf.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {})
with open(folder_name + '\\src\\report_executed.ipynb', 'wt') as f:
    nbf.write(nb, f)

#Generate html report
os.system('jupyter nbconvert --output-dir=' + folder_name + ' --to HTML --template classic --output report.html --no-input ' + folder_name + '\\src\\report_executed.ipynb' )

#Generate pdf report
#os.system('jupyter nbconvert --output-dir=' + folder_name + ' --to PDF --output report.pdf --no-input ' + folder_name + '\\src\\report_executed.ipynb' )

#Delete the src folder
os.system('rd /s /q ' + folder_name + '\\src')
