# Linear Regression Algorithm from scratch

import pandas as pd
import matplotlib.pyplot as plt
from Tools import tools

def LinearRegression(x, y, show_eq=False, show_plot=False):
    xm = tools().mean(x)
    ym = tools().mean(y)
    
    yym = []
    xxm = []
    for i in range(0, len(y)):
        yym.append(y[i]-ym)
        xxm.append(x[i]-xm)
    
    b_l1 = []
    for i in range(0, len(yym)):
        b_l1.append(x[i]*yym[i])

    b_l2 = []
    for i in range(0, len(xxm)):
        b_l2.append(x[i]*xxm[i])
    
    b = sum(b_l1)/sum(b_l2)

    a = ym - b*xm

    prediction = []

    for i in range(0, len(x)):
      prediction.append(a+b*x[i])

    plt.scatter(x, y)
    plt.plot(x, prediction)
    plt.title("Linear Regression Plot")
    plt.xlabel(f"x\nMSE: {tools().mse(y, prediction)}")
    plt.ylabel("y")

    if show_eq == True:
        return print(f"y = {b}x + {a}")
    
    if show_plot == True:
        plt.show()

x = [2,25,58]
y = [3,9,12]

LinearRegression(x,y, show_plot=True)
