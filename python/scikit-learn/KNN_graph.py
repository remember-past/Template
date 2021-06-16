from sklearn.neighbors import kneighbors_graph
X=PCA_distmap_triu_flatten_list_top_10
A = kneighbors_graph(X, 20, mode='connectivity', include_self=True,n_jobs=-1)
graph_matrix=A.toarray()
graph_matrix=graph_matrix+graph_matrix.T