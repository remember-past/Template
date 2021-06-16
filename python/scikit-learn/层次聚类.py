import scipy.spatial as sp, scipy.cluster.hierarchy as hc

linkage = hc.linkage(sp.distance.squareform(cell_cell_distance_df), method='average')
sns.clustermap(cell_cell_distance_df, row_linkage=linkage, col_linkage=linkage)
cluster_result = fcluster(linkage,4,criterion='maxclust')