# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 19:46
# @Author  : scfan
# @FileName: run_multiprocess_script_by_12_stage.py
# @Software: PyCharm
from multiprocessing import Pool
import os,time,random
import datetime

python_file=r"E:\Users\scfan\software\Anaconda3\envs\base_191\python.exe"

script_dir=r"E:\Users\scfan\program\image_project\Zhuang_20_Cell_Process\chr21_cell_cycle\clustering_quick_start_2021_06_20"


script_file=os.path.join(script_dir,"get_louvain_clustering_result_quick_start_multiprocess_random_control_2021_06_25.py")


def run_script(parameter_list):

    #script_parameter=[python_file,script_file,'weighted_sim','0','1']
    script_parameter = [python_file, script_file, parameter_list[0],parameter_list[1]]
    script=' '.join(script_parameter)
    print(script)
    os.system(script)
if __name__ =="__main__":
    print('Parent process %s.' % os.getpid())


    p = Pool(10)
    start_time=datetime.datetime.now()
    raw_parameter_list_list = []

    length_list = [11, 25, 29, 30, 31, 32, 34, 35, 38, 40, 42, 50, 66, 67, 92]
    length_list = [ 31, 32, 34, 35, 38, 40, 42, 50, 66, 67, 92]
    random_time = 10
    args_list = []
    for length in length_list:
        for i in range(random_time):
            args_list.append([str(length), str(i)])
    # simSeqTime_list = [1]


    all_parameter_list_list=args_list
    print(all_parameter_list_list)
    for i,parameter_list in enumerate(all_parameter_list_list):
        print(i,parameter_list)
        p.apply(run_script, args=(parameter_list,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    end_time=datetime.datetime.now()

    print('All subprocesses done.Using',end_time-start_time)