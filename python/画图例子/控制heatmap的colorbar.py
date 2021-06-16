import os
import time
from subprocess import  call
import numpy as np
import MSTDlib.MSTD_v2 as MSTD_v2
import pandas as pd
import seaborn as sns
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sc
from matplotlib.colors import ListedColormap
import scipy.sparse as sparse
import importlib
import copy
import gc
import datetime
from scipy.stats import zscore
import sys
import shutil
import scipy.sparse as ss
import random
from scipy.sparse import coo_matrix
from scipy.stats import hypergeom
from tqdm.notebook import tqdm

# f = plt.figure()
# ax = f.add_subplot(1,1,1)
# mat = np.arange(100).reshape((10, 10))
# i = sns.heatmap(mat, cmap= 'viridis')
# cbar = f.colorbar(i)
# cbar.ax.tick_params(size=0)
# plt.show()

import seaborn as sns
import pandas as pd
import numpy as np

import seaborn as sns
import pandas as pd
import numpy as np

arr = np.random.random((3,3))
df = pd.DataFrame(arr)
ax = sns.heatmap(arr)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=1,right=False,labelright=False)

plt.show()