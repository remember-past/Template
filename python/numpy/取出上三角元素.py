masker_ones=np.ones_like(distmap_list_without_NAN[0])
inds=np.where(np.triu(masker_ones,k=1)!=0)

distance_matrix_features_list=[]
cell_name_list=[]
for cell_index,one_cell_distmap in enumerate(distmap_list_without_NAN):
    one_cell_features=one_cell_distmap[inds]
    cell_name='cell_'+str(data['chrom_ids'][cell_index])
    cell_name_list.append(cell_name)

iu2 = np.triu_indices(4, 2)