import numpy as np
import pandas as pd
from math import sqrt


def g(z): 
    return 1/(1+np.exp(-z))

def h(x_i, theta): 
    return g(theta.T @ x_i)

def row_derivative(x_i, theta): 
    return h(x_i, theta)*(1-h(x_i, theta))*np.outer(x_i, x_i.T)

def hessian(x, theta):     
    n = len(x)
    res = np.zeros((n,n))
    for x_i in theta:         
        res += row_derivative(x_i, theta)
    return 1/n*res


