# Machine Learning and Regression Library for crypto analysis
# Focus: Parameters
# Author: Rasmus Erlemann
# Last Update: _

#LSTM parameters
epochs = 50
batch_size = 32
sliding_window = 40
dropout = 0
minsize = 100 #Minimum training data size

#Polynomial regression parameters
degree = 10

#Plotting parameters
figsize = 10, 10
plotlen = 100 #How many latest data poins to plot
predlen = 5 #How many time steps predict ahead
trainlen = plotlen-predlen #Number of training data points


