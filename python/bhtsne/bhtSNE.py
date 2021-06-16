# CIRCLET/CIRCLET_DEFINE.py
import bhtsne
def run_tsne(self, n_components=15, perplexity=30, rand_seed=-1):
    """ Run tSNE on the data. tSNE is run on the principal component projections
    for single cell RNA-seq data and on the expression matrix for mass cytometry data
    :param n_components: Number of components to use for running tSNE for single cell
    RNA-seq data. Ignored for mass cytometry
    :return: None
    """

    # Work on PCA projections if data is single cell RNA-seq
    data = deepcopy(self.data)
    if self.data_type == 'sc-seq':
        if self.pca is None:
            raise RuntimeError('Please run PCA using run_pca before running tSNE for single cell RNA-seq')
        data -= np.min(np.ravel(data))
        data /= np.max(np.ravel(data))
        data = pd.DataFrame(np.dot(data, self.pca['loadings'].iloc[:, 0:n_components]),
                            index=self.data.index)

    # Reduce perplexity if necessary
    data = data.astype(np.float64)
    perplexity_limit = 15
    if data.shape[0] < 100 and perplexity > perplexity_limit:
        print('Reducing perplexity to %d since there are <100 cells in the dataset. ' % perplexity_limit)
        perplexity = perplexity_limit
    self.tsne = pd.DataFrame(bhtsne.tsne(data, perplexity=perplexity, rand_seed=rand_seed),
                             index=self.data.index, columns=['x', 'y'])

