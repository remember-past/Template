import sys
import importlib
src_dir=r"E:\Users\scfan\program"
sys.path.append(src_dir)

import image_project.function_basic as function_basic
importlib.reload(function_basic)
basic=function_basic.basic_function()
from image_project.source.MultiProcessTools import *
if __name__ == '__main__':

    sub_process_number=30
    lock_dir=r"E:\\Users\\scfan\\program\\Template\\python\\并行化\\并行并带锁\\Temp_process_lock_da5e3886014aa8d4"
    sub_lock_index_list=MultiProcess.Lock.create_sub_lock_index_list(sub_process_number)

    axis_lock=0
    MultiProcess.Lock.open_lock(lock_dir,axis_lock,sub_lock_index_list)