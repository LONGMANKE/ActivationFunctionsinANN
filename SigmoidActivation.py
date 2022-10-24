import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the function
def sigmoidActivation(x):
    #the sigmoid activation function returns the value between 0 and 1
    return 1/(1+np.exp(-x))

#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,sigmoidActivation(x))
plt.axis('tight')
plt.title('Sigmoid Activation Function')
plt.show()