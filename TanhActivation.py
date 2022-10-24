import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the function
def tanhActivation(x):
    #the tanh activation function returns the value between -1 and 1
    return np.tanh(x)

#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,tanhActivation(x))
plt.axis('tight')
plt.title('Tanh Activation Function')
plt.show()