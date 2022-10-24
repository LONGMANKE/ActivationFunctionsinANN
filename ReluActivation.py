import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#defining the function
def reluActivation(x):
    #the relu activation function returns 0 if input x < 0 and returns x if input x > 0
    x1=[]
    for i in x:
        if i<0:
            x1.append(0)
        else:
            x1.append(i)
    return x1

#plotting the values between -10 and 10 ... you can change these values as you want
x = np.linspace(-10, 10)
plt.plot(x,reluActivation(x))
plt.axis('tight')
plt.title('RELU Activation Function')
plt.show()