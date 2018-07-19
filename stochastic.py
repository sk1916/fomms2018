"""
This function implements 1d  Monte Carlo integration
"""

import numpy as np

def monte_1d(x, f, trials):
   """ 
    Compute a 1D definite integral 
    Parameters
    ----------
    f : function
        User defined function.
    x : numpy array
        Integration domain.
    trials : integer
        Total number of generated random samples.
    Returns
    -------
    I : float
        Integration result.
   """   
   a = x[0]
   b = x[1]
   d = (b - a) *  np.random.rand(1, trials) + a
   y = f(d)
	return (b-a) * np.sum(y) / trials