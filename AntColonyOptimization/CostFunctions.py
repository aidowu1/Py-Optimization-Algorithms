import numpy as np

"""
Continious domain (constrained) common optimization functions
Reference: https://www.sfu.ca/~ssurjano/optimization.html
"""

def dp(x):
    """
    Diagonal Plane
    Range: l_bound, u_bound = 0.5, 1.5
    n_dims = 10
    Optimal x_hat : [x0, x1, ... xN] =  [0.5, 0.5,... 0.5]
    Optimal f_x_hat = 0.5
    """
    y = np.mean(x)
    return y

def sphere(x):
    """
    Sphere
    Range: l_bound, u_bound = -5.12, 5.12
    n_dims = 10
    Optimal x_hat : [x0, x1, ... xN] =  [0.0, 0.0,... 0.0]
    Optimal f_x_hat = 0.0
    """
    y = np.sum(np.power(x,2))
    return y

def stybtangm(x):
    """
    Styblinski-Tang function
    
    Range: l_bound, u_bound = -5, 5
    n_dims = 10
    Optimal x_hat : [x0, x1, ... xN] =  [-2.903534, -2.903534,...-2.903534]
    Optimal f_x_hat = -39.16599
    """
    y = (np.sum(np.power(x, 4.0) - 16.0*np.square(x) + 5.0*x))/2.0
    return y

def rastrigin(x):
    """
    Rastrigin function
    
    Range: l_bound, u_bound = -5.12, 5.12
    n_dims = 10
    Optimal x_hat : [x0, x1, ... xN] =  [0.0, 0.0,...0.0]
    Optimal f_x_hat = 0.0
    """
    d = x.shape[0]
    y = 10.0*d + np.sum((np.square(x) - 10*np.cos(2*np.pi*x)))
    return y
    
    

    
    