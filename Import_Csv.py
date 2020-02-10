#% matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
    fname = r"C:\Users\kitakaze\Downloads\sample_zukai_NeuralNetwork\sample_zukai_NeuralNetwork\chap02\2_01\sales.csv",
    dtype = 'int', 
    delimiter=',', 
    skiprows=1)

train_x = data[:,0]
train_y = data[:,1]

plt.plot(train_x,train_y,".")
plt.show()
