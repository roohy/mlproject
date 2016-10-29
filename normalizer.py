import numpy as np

def mean_std_cal(train_data_matrix):
    train_data_mean = data_matrix.mean(0) 
    train_data_std = data_matrix.std(0)
    return train_data_mean, train_data_std


def normalizer(data_matrix,train_data_mean,train_data_std):
    normal_data_matrix  = (data_matrix - train_data_mean)/train_data_std
    return normal_data_matrix


