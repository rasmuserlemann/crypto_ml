import nbformat as nbf
import os
import time
import sys
import uuid
import modules.ConstructJupyterNotebook as Jup
from nbconvert.preprocessors import ExecutePreprocessor

#Read in data location as an argument in terminal
datafile = str(sys.argv[1])

nb = nbf.v4.new_notebook()

#Combine jupyter notebook text and code cells
nb['cells'] = [
               nbf.v4.new_markdown_cell(Jup.introduction_text), nbf.v4.new_code_cell(Jup.introduction_code(datafile)),
               nbf.v4.new_markdown_cell(Jup.regression_text), nbf.v4.new_code_cell(Jup.regression_code(datafile)),
               ]

#New folder with a unique name
folder_name = 'Analysis_' + time.strftime("%Y_%m_%d_%H_%M_%S") + "_" + str(uuid.uuid4())
os.mkdir(folder_name)

#Make src folder and copy the python files
os.mkdir(folder_name + '/src')
os.mkdir(folder_name + '/src/modules')
os.system('cp modules/introduction.py ' + folder_name + '/src/modules')
os.system('cp modules/regression.py ' + folder_name + '/src/modules')

os.mkdir(folder_name + '/results')
os.mkdir(folder_name + '/data')


#Copy the data
os.system('cp data ' + folder_name + '/data')
with open(folder_name + '/src/report.ipynb', 'w') as f:
    nbf.write(nb, f)

with open(folder_name + '/src/report.ipynb') as f:
    nb = nbf.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {})
with open(folder_name + '/src/report_executed.ipynb', 'wt') as f:
    nbf.write(nb, f)

os.system('jupyter nbconvert --output-dir=' + folder_name + '/results --to PDF --template=./revtex.tplx --output report.pdf --no-input ' + folder_name + '/src/report_executed.ipynb' )
os.system('jupyter nbconvert --output-dir=' + folder_name + '/results --to PDF --template=./revtex.tplx --output report_code.pdf ' + folder_name + '/src/report_executed.ipynb' )