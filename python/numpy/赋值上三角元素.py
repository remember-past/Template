one_distmap=distmap_list_without_nan[0]

triu_ids=np.where(np.triu(np.ones_like(one_distmap),k=1)==1)
triu_ids

test_assign_value=np.ones_like(one_distmap)
test_assign_value[triu_ids]=one_distmap[triu_ids]
one_distmap[triu_ids]
test_assign_value[triu_ids]