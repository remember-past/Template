import matplotlib.pyplot as plt
import numpy as np

dx, dy = 0.05, 0.05

x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)

fig, axes = plt.subplots(nrows=1,ncols=2,frameon=False)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = axes[0].imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)

im1 = axes[1].imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
plt.gcf().subplots_adjust(bottom=0.15 ,
                                  left=0.2 ,
                                  right=1 - 0.15 )
plt.show()