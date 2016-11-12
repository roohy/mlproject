import numpy as np

def mean_std_cal(train_data_matrix):
    train_data_mean = data_matrix.mean(0)
    train_data_std = data_matrix.std(0)
    return train_data_mean, train_data_std


def normalizer(data_matrix,train_data_mean,train_data_std):
    normal_data_matrix  = (data_matrix - train_data_mean)/train_data_std
    return normal_data_matrix


def temp_normalize(X_tr):
    ''' Normalize training and test data features
    Args:
        X_tr: Unnormalized training features
        X_te: Unnormalized test features
    Output:
        X_tr: Normalized training features
        X_te: Normalized test features
    '''
    X_mu = np.mean(X_tr, axis=0)
    X_tr = X_tr - X_mu
    X_sig = np.std(X_tr, axis=0)
    X_sig[X_sig == 0] = 0.000001
    X_tr = X_tr/X_sig
    return X_tr



def full_normalize(X_tr,X_test):

    X_mu = np.mean(X_tr, axis=0)
    X_tr = X_tr - X_mu
    X_sig = np.std(X_tr, axis=0)
    X_sig[X_sig==0] = 0.000001
    X_tr = X_tr/X_sig
    X_test = X_test - X_mu
    X_test = X_test/X_sig

    return X_tr,X_test