row_idx=np.array([0,1,3])
col_idx=np.array([2,4])
a=np.arange(36).reshape((6,6))
b=np.ones((3,2))
a[row_idx[:,None],col_idx]=b
a

row_idx=np.array([0,1,3])
col_idx=np.array([2,4])
a=np.arange(36).reshape((6,6))
b=np.ones((3,2))
a[np.ix_(row_idx,col_idx)]=b
a

