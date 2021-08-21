import os
import time
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
import importlib
import copy
import gc
import datetime
from scipy.stats import zscore
import sys
import scipy.stats as st
import math
from scipy import optimize
from tqdm import tqdm
from scipy.spatial.distance import pdist, squareform

src_dir=r"E:\Users\scfan\program"
sys.path.append(src_dir)

import image_project.function_basic
importlib.reload(image_project.function_basic)
import image_project.function_basic

basic=image_project.function_basic.basic_function()

import image_project.Zhuang_20_Cell_Process.function_image_data_analysis
importlib.reload(image_project.Zhuang_20_Cell_Process.function_image_data_analysis)
import image_project.Zhuang_20_Cell_Process.function_image_data_analysis

Zhuang_20_cell=image_project.Zhuang_20_Cell_Process.function_image_data_analysis.Zhuang_20_cell
temp=Zhuang_20_cell.get_chr_length_info()
bin_process=image_project.Zhuang_20_Cell_Process.function_image_data_analysis.bin_process

import image_project.source.DataPreprocessTools.Cai21BioRxivPreprocess as Cai21BioRxivPreprocess

importlib.reload(Cai21BioRxivPreprocess)

import image_project.Cai_21_bioRxiv_Process.function_Cai_21_bioRxiv_info as function_Cai_21_bioRxiv_info

importlib.reload(function_Cai_21_bioRxiv_info)
Cai_20_bioRxiv_info = function_Cai_21_bioRxiv_info.Cai_20_bioRxiv_info

from image_project.source import *
from image_project.source.DataManipulateTools import *
from image_project.source.DataPreprocessTools import *
from image_project.source.DomainClusterTools import *
from image_project.source.ExtractFeatureTools import *
from image_project.source.FillNANTools import *
from image_project.source.PlotTools import *
from image_project.source.MultiProcessTools import *
if __name__ == '__main__':

    if (len(sys.argv) > 1):
        random_time_index = int(sys.argv[1])
        one_missing_rate_index = int(sys.argv[2])
        lock_dir=sys.argv[3]
        sub_process_number=int(sys.argv[4])
        axis_lock=int(sys.argv[5])
        # top=int(sys.argv[3])
    else:
        random_time_index = 0
        one_missing_rate_index = 9
        # top=100
    sub_lock_index_list=sub_lock_index_list=MultiProcess.Lock.create_sub_lock_index_list(sub_process_number)
    MultiProcess.Lock.open_lock(lock_dir, axis_lock, sub_lock_index_list,sleep_time=0.1)
    time.sleep(1)
    MultiProcess.Lock.transfer_lock_state(lock_dir, axis_lock, sub_lock_index_list)
    import os

    os._exit(0)

    importlib.reload(FillNANBasic)
    start_time = datetime.datetime.now()
    max_similarity =0.8
    self_similarity=0
    basic_self_similarity = 0.2
    data_dir=r"E:\Users\scfan\data\image_project\fill_NAN\without_nan_data\chr21_chr21_cell_cycle"
    output_dir=r"E:\Users\scfan\data\image_project\fill_NAN\without_nan_data\chr21_chr21_cell_cycle\random_probe_missing_data"
    data_dna_zxy_pkl_path = os.path.join(data_dir, "data.pkl")

    data = basic.load_variable_from_pikle_file(data_dna_zxy_pkl_path)

    if(len(sys.argv)>1):
        random_time_index = int(sys.argv[1])
        one_missing_rate_index = int(sys.argv[2])
        # top=int(sys.argv[3])
    else:
        random_time_index = 0
        one_missing_rate_index = 9
        # top=100
    top = 100
    method_name = 'linearRMSD_reciprocal_linear_Gaussian_adaptive_reciprocal'

    current_output_dir = os.path.join(output_dir, 'random_time_index_' + str(random_time_index))
    missing_possition_data = basic.load_variable_from_pikle_file(os.path.join(current_output_dir, 'data.pkl'))

    missing_rate_list = missing_possition_data['missing_rate_list']
    start_list = missing_possition_data['start_list']
    end_list = missing_possition_data['end_list']
    region_length = missing_possition_data['region_length']
    cell_number = missing_possition_data['cell_number']
    missing_possition_index = missing_possition_data['missing_possition_index']

    one_missing_rate = missing_rate_list[one_missing_rate_index]
    filled_dir = r"E:\Users\scfan\data\image_project\fill_NAN\without_nan_data\chr21_chr21_cell_cycle\filled_data\Mean"

    current_output_dir = os.path.join(filled_dir, 'random_time_index_' + str(random_time_index),
                                      'missing_percentage_' + str(int(one_missing_rate * 100)))
    one_missing_rate_data = basic.load_variable_from_pikle_file(os.path.join(current_output_dir, 'data.pkl'))
##Generate one_missing_rate_similarity##########
    print('Generate one_missing_rate_similarity')
    filled_dir = r"E:\Users\scfan\data\image_project\fill_NAN\without_nan_data\chr21_chr21_cell_cycle\filled_data\Mean"

    current_output_dir = os.path.join(filled_dir, 'random_time_index_' + str(random_time_index),
                                      'missing_percentage_' + str(int(one_missing_rate * 100)))

    one_missing_rate_dist = basic.load_variable_from_pikle_file(os.path.join(current_output_dir, 'RMSD_dist.pkl'))
    axis_0_length = len(one_missing_rate_dist) #region number

    one_missing_rate_similarity = []
    for axis_0 in tqdm(range(axis_0_length)):
        one_region_dist = np.array(one_missing_rate_dist[axis_0])
        one_region_similarity = ImageMethods.Similarity3D.dist2similarity_reciprocal_normalize_by_setting_specific_self_similarity(one_region_dist,self_similarity=self_similarity)
        one_missing_rate_similarity.append(one_region_similarity)
    del one_missing_rate_dist
    import gc
    gc.collect()


## generate one_missing_rate_background_distances_array###########################
    print('generate one_missing_rate_background_distances_array')
    one_missing_rate_background_distances_array = []
    axis_0_length = len(one_missing_rate_data) #region number
    axis_1_length = len(one_missing_rate_data[0]) #cell number
    for axis_0 in tqdm(range(axis_0_length)):
        axis_0_array=[]
        for axis_1 in range(axis_1_length):
            dna_zxys=one_missing_rate_data[axis_0][axis_1]
            bin_length = len(dna_zxys)
            ground_truth_dna_zxys_front = copy.deepcopy(dna_zxys[ 0:bin_length - 1, :])
            ground_truth_dna_zxys_back = copy.deepcopy(dna_zxys[1:bin_length, :])
            ground_truth_dna_zxys_distances = ground_truth_dna_zxys_back - ground_truth_dna_zxys_front
            axis_0_array.append(ground_truth_dna_zxys_distances)
        axis_0_array = np.array(axis_0_array)
        one_missing_rate_background_distances_array.append(axis_0_array)

###generate filled dna zxys############

    print('generate filled dna zxys')
    filled_dna_zxys = []
    extreaming_condition_1_list = []

    dna_zxys = copy.deepcopy(data['dna_zxys'])
    axis_2_list = []
    for axis_2, (start, end, one_length) in enumerate(zip(start_list, end_list, region_length)):
        axis_3_list = []
        for axis_3, one_cell_ids in enumerate(range(cell_number)):
            part_dna_zxys = dna_zxys[one_cell_ids, start:end]
            one_missing_possition = missing_possition_index[one_missing_rate_index][axis_2][axis_3]
            part_dna_zxys[one_missing_possition] = np.nan
            nan_ids = one_missing_possition
            probe_number = one_length
            continue_number_list=[]
            continue_start_ids=[]
            if (len(nan_ids) > 0):
                _zxys = part_dna_zxys
                (continue_number_list, continue_start_ids) = FillNANGaussianProcess.FillNANGPBackground.get_NAN_continue_info(nan_ids)

            self_similarity_array = np.ones(probe_number) * basic_self_similarity
            for one_number, one_start_ids in zip(continue_number_list, continue_start_ids):
                self_similarity_array[
                one_start_ids:one_start_ids + one_number] = ImageMethods.Similarity3D.MissingLength2Confidence_reciprocal(
                    one_number, max_similarity=max_similarity)

            background_distances_array=one_missing_rate_background_distances_array[axis_2] # for one region

            part_mu_sigma_array=[]
            for bin_axis in range(one_length - 1):
                similarity_array = copy.deepcopy(one_missing_rate_similarity[axis_2][axis_3].flatten())
                similarity_array=similarity_array*(1-self_similarity_array[bin_axis+1])
                similarity_array[axis_3] =self_similarity_array[bin_axis+1]

                axis_1_mu_sigma_array = []
                one_bin = background_distances_array[:, bin_axis, :]
                one_have_number_position = np.where(~np.isnan(one_bin[:, 0].flatten()))[0]

                filter_similarity_array=similarity_array[one_have_number_position]
                filter_part_dna_zxys = one_bin[one_have_number_position, :]

                ###get top similarity cells
                similarity_array=filter_similarity_array
                similarity_array_top=similarity_array
                top_length = int(len(similarity_array) * top / 100)
                sort_index = np.argsort(similarity_array_top)[::-1] ###descending sort
                sort_index = sort_index[0:top_length]
                similarity_array_top = similarity_array_top[sort_index]
                filter_part_dna_zxys_top = filter_part_dna_zxys[sort_index, :]

                filter_similarity_array=similarity_array_top
                filter_part_dna_zxys=filter_part_dna_zxys_top

                mean = np.average(filter_part_dna_zxys, axis=0,weights=filter_similarity_array)
                cov = np.cov(filter_part_dna_zxys, rowvar=0,ddof=0,aweights=filter_similarity_array)
                # cov=np.zeros((3,3))
                axis_1_mu_sigma_array.append(mean)
                axis_1_mu_sigma_array.append(cov)
                part_mu_sigma_array.append(axis_1_mu_sigma_array)


            if (len(nan_ids) > 0):
                _zxys = part_dna_zxys
                (continue_number_list, continue_start_ids) = FillNANGaussianProcess.FillNANGPBackground.get_NAN_continue_info(nan_ids)
                _zxys_fill_NAN= FillNANGaussianProcess.FillNANGPBackground.fill_NAN_v1(_zxys,
                                                                                              continue_number_list,
                                                                                              continue_start_ids,
                                                                                              probe_number,part_mu_sigma_array)
            else:
                _zxys_fill_NAN = part_dna_zxys
            axis_3_list.append(_zxys_fill_NAN)

        axis_2_list.append(axis_3_list)

    filled_dna_zxys=axis_2_list


    axis_2_filled_dna_zxys = filled_dna_zxys
    current_output_dir = os.path.join(data_dir, 'filled_data', method_name,
                                      'random_time_index_' + str(random_time_index),
                                      'missing_percentage_' + str(int(one_missing_rate * 100)))
    basic.recursive_mkdir(current_output_dir)
    basic.store_variable_from_pikle_file(os.path.join(current_output_dir, 'data.pkl'), axis_2_filled_dna_zxys)


    end_time = datetime.datetime.now()

    fill_data = copy.deepcopy(missing_possition_data)
    del fill_data['missing_possition_index']
    fill_data['extreaming_condition_1_list'] = extreaming_condition_1_list

    current_output_dir = os.path.join(data_dir, 'filled_data', method_name, 'random_time_index_' + str(random_time_index))
    basic.recursive_mkdir(current_output_dir)
    basic.store_variable_from_pikle_file(os.path.join(current_output_dir, 'data.pkl'), fill_data)

    current_output_dir = os.path.join(data_dir, 'filled_data', method_name,
                                      'random_time_index_' + str(random_time_index),
                                      'missing_percentage_' + str(int(one_missing_rate * 100)))

    usingtime_output_file = os.path.join(current_output_dir, 'data.pkl.usingtime')
    basic.log_using_time(usingtime_output_file, end_time - start_time)