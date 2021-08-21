# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 19:46
# @Author  : scfan
# @FileName: run_multiprocess_script_by_12_stage.py
# @Software: PyCharm
from multiprocessing import Pool, Manager
import multiprocessing
import os,time,random
import datetime
import numpy as np
import sys
python_file=r"E:\Users\scfan\software\Anaconda3\envs\base_191\python.exe"

script_dir=r"E:\Users\scfan\program\Template\python\并行化\并行并带锁"

script_file=os.path.join(script_dir,"generate_filled_data_linearRMSD_reciprocal_linear_Gaussian_adaptive_reciprocal_chr21_chr21_cell_cycle_2021_08_20.py")



src_dir=r"E:\Users\scfan\program"
sys.path.append(src_dir)

import image_project.function_basic as function_basic

basic=function_basic.basic_function()
from image_project.source.MultiProcessTools import *



def run_script(parameter_list):

    #script_parameter=[python_file,script_file,'weighted_sim','0','1']
    print(parameter_list[4].value)

    script_parameter = [python_file, script_file, parameter_list[0],parameter_list[1],parameter_list[2],
                        parameter_list[3],str(parameter_list[4].value)]
    script=' '.join(script_parameter)
    print(script)
    parameter_list[4].value = parameter_list[4].value + 1
    os.system(script)
if __name__ =="__main__":
    print('Parent process %s.' % os.getpid())

    base_lock_dir = r"E:\Users\scfan\program\Template\python\并行化\并行并带锁"
    sub_process_number = 30
    lock_dir = MultiProcess.Lock.create_lock_dir(base_lock_dir)
    sub_lock_index_list = MultiProcess.Lock.create_sub_lock_index_list(sub_process_number)
    MultiProcess.Lock.init_sublock_file(lock_dir, sub_lock_index_list)

    axis_lock = Manager().Value('i', 0)
    p = Pool(24)
    start_time=datetime.datetime.now()
    random_time=5
    random_time_list = np.arange(random_time)
    random_time_index=0
    one_missing_rate_index_list=np.arange(30)
    # one_missing_rate_index_list=[19,79]
    # one_missing_rate_index_list = np.arange(1,3)
    # random_time = 10
    args_list=[]
    for one_missing_rate_index in one_missing_rate_index_list:
        args_list.append([[str(random_time_index),str(one_missing_rate_index),lock_dir,str(sub_process_number),axis_lock]])
    # simSeqTime_list = [1]


    all_parameter_list_list=args_list
    print(all_parameter_list_list)
    # for i,parameter_list in enumerate(all_parameter_list_list):
    #     print(i,parameter_list)
    #     # p.apply_async(run_script, args=(parameter_list,))
    #     p.apply(run_script, args=(parameter_list,))
    p.starmap(run_script, all_parameter_list_list)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    end_time=datetime.datetime.now()
    axis_lock=sub_process_number-1

    MultiProcess.Lock.clear_lock_dir(lock_dir)
    print('All subprocesses done.Using',end_time-start_time)