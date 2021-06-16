# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 21:35
# @Author  : scfan
# @FileName: temp.py
# @Software: PyCharm
target_dir=r"D:\Users\scfan\data\CellCycle\experiment\comparision_of_cluster\sim\1\simulation_file_for_scHiCluster\SeqDepthTime_0.1"
result_path=os.path.join(target_dir,"result.pkl")

def get_roc_auc(sim_info,result_dic):

    # result_dic=sim_info.load_variable_from_pikle_file(result_path)
    label=np.array([sim_info.KeyCellName_ValueStage_dic[cell_name] for cell_name in sim_info.cell_phase_list[0]]).astype('U8')

    embedding_array=result_dic['embedding']
    embedding_plot=np.array([one_vector[0:2] for one_vector in embedding_array])

    vector_array=embedding_plot

    mean=vector_array.sum(axis=0)
    normalized_vector=vector_array-mean
    angle_vector=get_angle(normalized_vector)

    roc_auc_result_dic={}
    for one_label in sim_info.cell_stage_name_FACS:
        temp_result_dic={}
        one_label_vector=angle_vector[label==one_label]
        kappa,loc,scale=vonmises.fit(one_label_vector,fscale=1)

        dif_angle_list=[]
        for one_angle in angle_vector:
            first_term=np.abs(one_angle-loc)
            second_term=np.abs(one_angle-2*np.pi-loc)
            dif_angle=np.min([first_term,second_term])
            dif_angle_list.append(dif_angle)
        dif_angle_vector=np.array(dif_angle_list)
        score_vector=2*np.pi-dif_angle_vector
        temp_binary_label=np.array(label==sim_info.cell_stage_name_FACS[0])
        binary_label_list=[]
        for one_value in temp_binary_label:
            if(one_value):
                binary_label_list.append(1)
            else:
                binary_label_list.append(0)
        binary_label_vector=np.array(binary_label_list)
        from sklearn.metrics import roc_auc_score
        fpr, tpr, _ = roc_curve(binary_label_vector, score_vector)
        auc_score=roc_auc_score(binary_label_vector, score_vector)
        temp_result_dic['fpr']=fpr
        temp_result_dic['tpr'] = tpr
        temp_result_dic['auc_score'] = auc_score
        roc_auc_result_dic[one_label]=temp_result_dic
    return roc_auc_result_dic