#!/usr/bin/env python
##############################################################################
#
# Usage example for the procedure loess_1d
#
# MODIFICATION HISTORY:
#   V1.0.0: Written by Michele Cappellari, Oxford 25 February 2015
#   V1.0.1: Fixed deprecation warning in Numpy 1.11. MC, Oxford, 18 April 2016
#   V1.0.2: Changed imports for loess as a package. MC, Oxford, 17 April 2018
#
##############################################################################

import numpy as np
import matplotlib.pyplot as plt

from loess.loess_1d import loess_1d

def test_loess_1d():
    """
    Usage example for loess_1d

    """
    n = 200
    np.random.seed(123)
    x = np.random.uniform(-1, 1, n)
    x.sort()

    y = np.sin(3*x)
    sigy = 0.4
    yran = np.random.normal(y, sigy)

    nbad = int(n*0.1) # 10% outliers
    w = np.random.randint(0, n, nbad)  # random indices from 0-n
    yran[w] += np.random.normal(0, 5*sigy, nbad)

    xout, yout, weigts = loess_1d(x, yran, frac=0.3)

    w = weigts < 0.34  # identify outliers
    plt.clf()
    plt.plot(x, yran, 'ro', label='Noisy')
    plt.plot(xout, yout, 'b', linewidth=4, label='LOESS')
    plt.plot(x, y, color='limegreen', linewidth=4, label='True')
    plt.plot(x[w], yran[w], '+k', ms=20, label='Outliers')
    plt.legend(loc='lower right')
    plt.pause(1)

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    test_loess_1d()
