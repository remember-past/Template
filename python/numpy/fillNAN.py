distmap_list = np.array([squareform(pdist(_zxy)) for _zxy in tqdm(data['dna_zxys'])])

mean_distance_array=np.nanmean(distmap_list,axis=0)
var_distance_array=np.nanvar(distmap_list,axis=0)

distmap_list_without_nan=[]
for index,one_distmap in enumerate(distmap_list):
    inds=np.where(np.isnan(one_distmap))
    one_distmap_without_nan=copy.deepcopy(one_distmap)
    one_distmap_without_nan[inds]=mean_distance_array[inds]
    distmap_list_without_nan.append(one_distmap_without_nan)