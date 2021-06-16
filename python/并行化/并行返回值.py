from multiprocessing import Pool

def run(parameter_list):
    temp_series=parameter_list[0]
    one_df=temp_series['df']
    feature_df_dic=parameter_list[1]
    feature_temp={}
    for feature_name,one_feature_df in feature_df_dic.items():
        print(feature_name)
        geneset_DF, loopset_DF=loop.get_loopsets_overlap_feature(one_df,one_feature_df)
        feature_temp[feature_name]={'geneset':geneset_DF,'loopset':loopset_DF}
    temp_result=temp_series.to_list()[0:3]+[feature_temp]
    return temp_result

if __name__=="__main__":

    pool = Pool(processes=24)
    result = []
    start_time = datetime.datetime.now()
    for count, loop_index in enumerate(loop_set_df.index):
        print("count number", count)
        temp_series = loop_set_df.loc[loop_index]
        parameter_list = [temp_series, feature_df_dic]
        result.append(pool.apply_async(run, args=(parameter_list,)))

    pool.close()
    pool.join()
    result_dic = {}
    feature_loop_result = []
    for i, one_task in enumerate(result):
        temp_result = one_task.get()

        feature_loop_result.append(temp_result)