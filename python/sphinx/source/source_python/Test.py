import os
import time
import datetime
from subprocess import  call
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sc
from matplotlib.colors import ListedColormap
import scipy.sparse as sparse
from scipy.stats import zscore
import copy
import pickle
from tqdm import tqdm
import importlib
import sys
from scipy.spatial.distance import pdist, squareform


def mean_subtraction_matrix(A):
    '''
    Compute the centralized matrix of A.
    Parameters
    ----------
    A : array_like
        row, bin of chromosome;
        columns, Z, X, Y positions

    Returns
    -------
    centroid_A: array_like
        shape=(1,3)
    mean_subtracted_A: array_like
        mean_subtracted_A and A have the same shape.
    '''
    centroid_A = np.mean(A, axis=0)
    mean_subtracted_A = A - centroid_A
    return centroid_A, mean_subtracted_A
class Similarity3D(object):
    '''
    calculate the similarities between cells with three-dimensonal positions(Z,X,Y)
    '''
    @staticmethod
    def mean_subtraction_matrix(A):
        '''
        Compute the centralized matrix of A.
        Parameters
        ----------
        A : array_like
            row, bin of chromosome;
            columns, Z, X, Y positions

        Returns
        -------
        centroid_A: array_like
            shape=(1,3)
        mean_subtracted_A: array_like
            mean_subtracted_A and A have the same shape.
        '''
        centroid_A=np.mean(A, axis=0)
        mean_subtracted_A=A-centroid_A
        return centroid_A,mean_subtracted_A


