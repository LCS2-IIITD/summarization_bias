import numpy as np
from numpy import * 
from sklearn.decomposition import TruncatedSVD


def get_weighted_average(We, x, w):
    """
    Compute the weighted average vectors
    :param We: We[i,:] is the vector for word i
    :param x: x[i, :] are the indices of the words in sentence i
    :param w: w[i, :] are the weights for the words in sentence i
    :return: emb[i, :] are the weighted average vector for sentence i
    """
    n_samples = x.shape[0]
    emb = np.zeros((n_samples, We.shape[1]))
    for i in range(n_samples):
        emb[i,:] = w[i,:].dot(We[x[i,:],:]) / np.count_nonzero(w[i,:])

    # By Yanjun 
    for i in range(n_samples):
        where_nan = isnan(emb[i,:])
        emb[i,where_nan] = 0 
    return emb

def new_get_weighted_average(We, x, w):
    """
    Compute the weighted average vectors
    :param We: We[i,:] is the vector for word i
    :param x: x[i, :] are the indices of the words in sentence i
    :param w: w[i, :] are the weights for the words in sentence i
    :return: emb[i, :] are the weighted average vector for sentence i
    """
    #n_samples = x.shape[0]
    #emb = np.zeros((1, We.shape[1]))
    if w.shape[0] != We.shape[0]:
        tmp = np.zeros((w.shape[0] - We.shape[0], We.shape[1]))
        #print("Append empty arrays: {}".format(tmp.shape))
        We = np.vstack((We, tmp))
        #print("New We arrays: {}".format(We.shape))
    emb = np.dot(w,We) / np.count_nonzero(w)
    #print("emb shape: {}".format(emb.shape))
    emb = emb.reshape(1,-1) 
    #print("new emb shape: {}".format(emb.shape))
    #emb[i,:] = w[i].dot(We) / np.count_nonzero(w)

    # By Yanjun 
    # for i in range(n_samples):
    #     where_nan = isnan(emb[i,:])
    #     emb[i,where_nan] = 0 
    return emb

def compute_pc(X,npc=1):
    """
    Compute the principal components
    :param X: X[i,:] is a data point
    :param npc: number of principal components to remove
    :return: component_[i,:] is the i-th pc
    """
    svd = TruncatedSVD(n_components=npc, n_iter=7, random_state=0)
    svd.fit(X)
    return svd.components_

def remove_pc(X, npc=1):
    """
    Remove the projection on the principal components
    :param X: X[i,:] is a data point
    :param npc: number of principal components to remove
    :return: XX[i, :] is the data point after removing its projection
    """
    pc = compute_pc(X, npc)
    if npc==1:
        XX = X - X.dot(pc.transpose()) * pc
    else:
        XX = X - X.dot(pc.transpose()).dot(pc)
    return XX


def SIF_embedding(We, x, w, params):
    """
    Compute the scores between pairs of sentences using weighted average + removing the projection on the first principal component
    :param We: We[i,:] is the vector for word i
    :param x: x[i, :] are the indices of the words in the i-th sentence
    :param w: w[i, :] are the weights for the words in the i-th sentence
    :param params.rmpc: if >0, remove the projections of the sentence embeddings to their first principal component
    :return: emb, emb[i, :] is the embedding for sentence i
    """
    emb = new_get_weighted_average(We, x, w)
    if  params.rmpc > 0:
        emb = remove_pc(emb, params.rmpc)
    return emb