'''
Created on Oct 19, 2015

@author: pta
'''
from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

param_theta=0.3
num_flips = 100

print bernoulli.rvs(param_theta, size=num_flips)