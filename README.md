# Config kernel

conda install ipykernel

python -m ipykernel install --user --name pytorch1.7.1 --display-name pytorch1.7.1
python -m ipykernel install --user --name pytorch1.10.1 --display-name pytorch1.10.1
python -m ipykernel install --user --name pytorch1.10.1-d2l --display-name pytorch1.10.1-d2l

python -m ipykernel install --user --name umap --display-name umap
python -m ipykernel install --user --name umap_1 --display-name umap_1
python -m ipykernel install --user --name umap_2 --display-name umap_2

# Download with aspera

#!/bin/sh
ascp -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh --overwrite=diff -QTr -l6000m -k 1 anonftp@ftp.ncbi.nlm.nih.gov:/geo/series/GSE164nnn/GSE164203/suppl/GSE164203_processed_data.contacts_pairs.tar.gz /media/fanshichen/Elements\ SE/zhanglab192/data/data/21_cell_brain_xie/GSE164203/suppl/GSE164203_processed_data.contacts_pairs.tar.gz



# Github common usage

git clean  -d  -fx ""
其中 
x  -----删除忽略文件已经对git来说不识别的文件
d  -----删除未被添加到git的路径中的文件
f  -----强制运行


git stash
git stash drop
git pull

#解决 提示文件会被overwrite的问题
git add * 
git stash
git pull



# Linux manager usage

du -sh ./*


watch -n 0.1 gpustat

source /home/scfan/software/anaconda3/bin/activate

nohup jupyter notebook --allow-root --config ~/.jupyter/jupyter_notebook_config-scfan.py >/home/scfan/software/log/jupyter_root.out 2>&1 &


fuser -v /dev/nvidia*


alias activate_base='source /bigdata0/fanshichen/software/anaconda3/bin/activate'

安装时要用bash
alias matlab='/home/zhanglab/software/Matlab2022/bin/matlab -nodesktop -nodisplay'

export PATH="/home/zhanglab/software/Matlab2022/bin/:$PATH"





# Installation of CUDA

ln -sf /home/scfan/software/CUDA/cuda-11.5 /home/scfan/software/CUDA/symbolic_link/cuda



rm /home/scfan/software/CUDA/symbolic_link/cuda



ln -sf /home/scfan/software/CUDA/cuda-10.1 /home/scfan/software/CUDA/symbolic_link/cuda

ln -sf /home/scfan/software/CUDA/cuda-11.2 /home/scfan/software/CUDA/symbolic_link/cuda



ln -sf /home/scfan/software/CUDA/cuda-11.3 /home/scfan/software/CUDA/symbolic_link/cuda





rm -rf ./tem;mkdir tem;tar -xzvf cudnn-8.0-linux-x64-v7.1.tgz -C ./tem/

rm -rf ./tem;mkdir tem;tar -xzvf cudnn-11.3-linux-x64-v8.2.1.32.tgz -C ./tem/

cp /home/scfan/software/cuda_installation_file/tem/cuda/include/cudnn.h  /home/scfan/software/CUDA/cuda-10.1/include/

cp /home/scfan/software/cuda_installation_file/tem/cuda/lib64/libcudnn*  /home/scfan/software/CUDA/cuda-10.1/lib64



cp /home/scfan/software/cuda_installation_file/tem/cuda/include/cudnn.h  /home/scfan/software/CUDA/cuda-11.2/include/

cp /home/scfan/software/cuda_installation_file/tem/cuda/lib64/libcudnn*  /home/scfan/software/CUDA/cuda-11.2/lib64



cp /home/scfan/software/cuda_installation_file/tem/cuda/include/cudnn.h  /home/scfan/software/CUDA/cuda-11.3/include/

cp /home/scfan/software/cuda_installation_file/tem/cuda/lib64/libcudnn*  /home/scfan/software/CUDA/cuda-11.3/lib64



chmod a+r /home/scfan/software/CUDA/cuda-10.1/include/cudnn.h /home/scfan/software/CUDA/cuda-10.1/lib64/libcudnn*



chmod a+r /home/scfan/software/CUDA/cuda-11.2/include/cudnn.h /home/scfan/software/CUDA/cuda-11.2/lib64/libcudnn*

chmod a+r /home/scfan/software/CUDA/cuda-11.3/include/cudnn.h /home/scfan/software/CUDA/cuda-11.2/lib64/libcudnn*





# Common usage of pytorch





# Usage of sc3DVI

python /mnt/disk1/scfan/program/ToolsDemo/scVI-3D/scripts/scVI-3D.py -b 10 -c "whole" -r 1000000 -i /mnt/disk1/scfan/program/ToolsDemo/scVI-3D/demoData -o /mnt/disk1/scfan/program/ToolsDemo/scVI-3D/results -cs /mnt/disk1/scfan/program/ToolsDemo/scVI-3D/supplementaryData/demoData_summary.txt -g /mnt/disk1/scfan/program/ToolsDemo/scVI-3D/supplementaryData/hg19.chrom.sizes -br -n 100 -gpu -p 10 -pca 50 -up -tp -v





