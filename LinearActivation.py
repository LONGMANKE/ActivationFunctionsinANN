import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the function
def linearActivation(x):
    #the linear activation function returns the input as it is
    return x


#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,linearActivation(x))
plt.axis('tight')
plt.title('Linear Activation Function')
plt.show()

