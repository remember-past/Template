def raw_pca(network, chromsize, nc, res=1000000, ndim=20):
	matrix=[]
	for i, c in enumerate(chromsize):
		ngene = int(chromsize[c] / res)+1
		start_time = time.time()
		uptri = np.triu_indices(ngene, 1)
		A_concat = np.zeros((len(label), len(uptri[0]))).astype(float)
		j = 0
		for cell in network:
			D = np.loadtxt(cell + '_chr' + c + '.txt')
			A = csr_matrix((D[:, 2], (D[:, 0], D[:, 1])), shape = (ngene, ngene)).toarray()
			A = np.log2(A + A.T + 1)
			A_concat[j, :] = A[uptri]
			j += 1
		end_time = time.time()
		print('Load and impute chromosome', c, 'take', end_time - start_time, 'seconds')
		pca = PCA(n_components = min(A_concat.shape)-1)
		A_reduce = pca.fit_transform(A_concat)
		matrix.append(A_reduce)
		print(c)
	matrix = np.concatenate(matrix, axis = 1)
	pca = PCA(n_components = min(matrix.shape) - 1)
	matrix_reduce = pca.fit_transform(matrix)
	kmeans = KMeans(n_clusters = nc, n_init = 200).fit(matrix_reduce[:, 1:(ndim + 1)])
	return kmeans.labels_, matrix_reduce