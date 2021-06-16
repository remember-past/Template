## global variables
import numpy as np
# correction_folder
_correction_folder=r'\\10.245.74.116\Chromatin_NAS_0\Corrections\Corrections_202001'
# temp folder
_temp_folder = r'\\10.245.74.116\Chromatin_NAS_6\Pu_Temp'
# distance_zxy
_distance_zxy = np.array([200, 106, 106])
# sigma_zxy
_sigma_zxy = np.array([1.35, 1.9, 1.9])
# image_dim
_image_size = np.array([30,2048,2048])
# allowed_colors
_allowed_colors = ['750', '647', '561', '488', '405']
_corr_channels = ['750', '647', '561']
# number of buffer frames and empty frames
_num_buffer_frames = 10
_num_empty_frames = 0
# image datatype
_image_dtype = np.uint16


# everything about domain analysis
from . import domain_tools
# function to call and evaluate compartments

## import exteral functions
from .External import Fitting_v3
from .External import DomainTools
