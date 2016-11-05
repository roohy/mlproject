import numpy as np

import matplotlib.pyplot as plt
from sklearn import decomposition

def main_plot_pca(data):
    print "training the PCA model"
    pca = decomposition.IncrementalPCA(n_components=30,batch_size=400)
    data_trans = pca.fit_transform(data)
    print "pca model trained, variance:"
    print(pca.explained_variance_ratio_)
    return pca, data
    '''plt.figure(1, figsize=(4, 3))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    plt.plot(pca.explained_variance_, linewidth=2)
    plt.axis('tight')
    plt.xlabel('n_components')
    plt.ylabel('explained_variance_')
    plt.savefig("haha.png")'''

def transform(data,pca):
    return pca.transform(data)