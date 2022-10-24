import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the binary step activation function
def binaryStep(x):
    #returns if input is greater than 0 or 1 if input is greater than 0
    return np.heaviside(x,1)

#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,binaryStep(x))
plt.axis('tight')
plt.title('Binary Step Activation Function')
plt.show()
