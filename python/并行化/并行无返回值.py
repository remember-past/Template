# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 19:46
# @Author  : scfan
# @FileName: run_multiprocess_script_by_12_stage.py
# @Software: PyCharm
from multiprocessing import Pool
import os,time,random
import datetime

python_file=r"E:\Users\scfan\software\anaconda3_new\python.exe"

script_dir=r"E:\Users\scfan\program\simulation_project\experiment\pool_structure_analysis"

script_file=os.path.join(script_dir,"script_create_hic_for_raw_sim_RawAndSim_by_5_region.py")

def run_script(parameter_list):

    #script_parameter=[python_file,script_file,'weighted_sim','0','1']
    script_parameter = [python_file, script_file, parameter_list[0], parameter_list[1], parameter_list[2]]
    script=' '.join(script_parameter)
    os.system(script)
if __name__ =="__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool(24)
    start_time=datetime.datetime.now()
    distance_stratified_parameter_list_list = []
    step=1
    for i in range(0, 5,step):
        parameter_list = ['distance_stratified_sim', str(i), str(i + step)]
        distance_stratified_parameter_list_list.append(parameter_list)


    all_parameter_list_list=distance_stratified_parameter_list_list
    print(all_parameter_list_list)
    for i,parameter_list in enumerate(all_parameter_list_list):
        print(i,parameter_list)
        p.apply_async(run_script, args=(parameter_list,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    end_time=datetime.datetime.now()

    print('All subprocesses done.Using',end_time-start_time)