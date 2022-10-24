import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the function
def softmax(x):
    #the softmax activation function turns the last linear layer of a multi-class classification neural network into probabilities
    #I dont know what this means
    return np.exp(x)/np.sum(np.exp(x), axis=0)

#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,softmax(x))
plt.axis('tight')
plt.title('SoftMax Activation Function')
plt.show()