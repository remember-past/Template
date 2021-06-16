def decay(network, chromsize, nc, res=1000000, ndim=20):
	matrix = []
	for i, c in enumerate(chromsize):
		ngene = int(chromsize[c] / res)+1
		start_time = time.time()
		dec = np.zeros((len(label), ngene-1)).astype(float)
		j = 0
		for j, cell in enumerate(network):
			D = np.loadtxt(cell+'_chr'+c+'.txt')
			A = csr_matrix((D[:, 2], (D[:, 0], D[:, 1])), shape=(ngene, ngene)).toarray()
			tmp = np.array([np.sum(np.diag(A, k)) for k in range(1,ngene)])
			dec[j] = tmp / np.sum(tmp)
		end_time = time.time()
		print('Load and random walk take', end_time - start_time, 'seconds')
		matrix.append(dec)
		print(c)
	matrix = np.concatenate(matrix, axis = 1)
	pca = PCA(n_components = min(matrix.shape) - 1)
	matrix_reduce = pca.fit_transform(matrix)
	kmeans = KMeans(n_clusters = nc, n_init = 200).fit(matrix_reduce[:, :ndim])
	return kmeans.labels_, matrix_reduce