import matplotlib.pylab as plt
import numpy as np
import pickle, os
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, cdist, squareform

####### You will need cv2. If you do not have it, run: pip install opencv-python
import cv2

from matplotlib import cm


def resize(im__, scale_percent=100):
    width = int(im__.shape[1] * scale_percent / 100)
    height = int(im__.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(im__, dim, interpolation=cv2.INTER_NEAREST)
    return resized


def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH), cv2.INTER_NEAREST)


def interp1dnan(A):
    A_ = np.array(A)
    ok = np.isnan(A) == False
    xp = ok.nonzero()[0]
    fp = A[ok]
    x = np.isnan(A).nonzero()[0]
    A_[np.isnan(A)] = np.interp(x, xp, fp)
    return A_


def interpolate_chr(_chr):
    """linear interpolate chromosome coordinates"""
    _new_chr = np.array(_chr)
    for i in range(_new_chr.shape[-1]):
        _new_chr[:, i] = interp1dnan(_new_chr[:, i])
    return _new_chr


from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib import cm

fig = plt.figure(figsize=(20, 20))
grid = ImageGrid(fig, 111, nrows_ncols=(4, 1), axes_pad=0.)

mat_ = np.log(contact_map_combined)
pad = 0
min_val, max_val = -2, None  # the minimum and maximum distance in nanometers. this sets the threshold of the image
if max_val is None: max_val = np.nanmax(mat_)
if min_val is None: min_val = np.nanmin(mat_)
# This colors the image
im_ = (np.clip(mat_, min_val, max_val) - min_val) / (max_val - min_val)
im__ = np.array(cm.seismic(im_)[:, :, :3] * 255, dtype=np.uint8)

# resize image 10x to get good resolution
resc = 10  ############
resized = resize(im__, resc * 100)

# Rotate 45 degs
resized = rotate_bound(resized, -45)
start = int(pad * np.sqrt(2) * resc)
center = int(resized.shape[1] / 2)

# Clip it to the desired size
padup = 25  ##### how much of the matrix to keep in the up direction
resized = resized[center - resc * padup:center + resc * padup]

# create axes
contact_ax = grid[0]

# List of positions of CTCF and rad21 in chr21
# ctcf
ctcf = [9, 21, 33, 67, 73, 78, 139, 226, 231, 235, 242, 253, 256,
        273, 284, 292, 301, 307, 339, 350, 355, 363, 366, 370, 373, 376,
        381, 385, 390, 396, 402, 405, 410, 436, 440, 446, 456, 469, 472,
        476, 482, 485, 488, 492, 500, 505, 508, 512, 520, 540, 543, 550,
        554, 560, 565, 576, 580, 585, 589, 592, 595, 599, 602, 606, 615,
        619, 622, 625, 628, 633, 636, 639]
# rad21
rad21 = [21, 33, 67, 73, 139, 226, 231, 236, 242, 256, 273, 284, 292,
         301, 305, 339, 350, 355, 363, 366, 370, 381, 386, 390, 396, 405,
         410, 415, 436, 440, 446, 456, 469, 472, 482, 485, 492, 500, 505,
         508, 512, 543, 550, 554, 560, 576, 581, 585, 589, 593, 596, 599,
         602, 615, 619, 622, 625, 628, 633, 636]

start = 0
min__ = 0
cts_perc = 1. * cts / len(pts) * 100 * resc
x_vals = (np.arange(len(cts_perc)) - min__) * resc * np.sqrt(2) - start

# grid[1].imshow(A_.T,cmap='bwr')
grid[1].plot(x_vals, cts_perc, 'ko-')
contact_ax.imshow(resized)
grid[2].plot(x_vals[ctcf], [0] * len(ctcf), '^',
             color='orange', mec='k',
             markeredgewidth=1, markersize=10)
grid[3].plot(x_vals[rad21], [0] * len(rad21), '^',
             color='yellow', mec='k',
             markeredgewidth=1, markersize=10)
ypad = 20
grid[2].set_ylim([-ypad, ypad])
grid[3].set_ylim([-ypad, ypad])
grid[2].set_yticks([])
grid[3].set_yticks([])
# grid[1].set_yticks([])
# grid[1].set_ylabel('AB  ',rotation='horizontal')
grid[2].set_ylabel('CTCF        ', rotation='horizontal')
grid[3].set_ylabel('RAD21        ', rotation='horizontal')
min_, max_ = (282, 480)
contact_ax.set_xlim([min_ * resc * np.sqrt(2), max_ * resc * np.sqrt(2)])

plt.savefig(os.path.join(figure_folder,
                         f'Fig1C_chr21_sc-domain_prob_combined.pdf'), transparent=True)
plt.show()