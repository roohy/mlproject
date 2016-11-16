from crab.models import  MatrixPreferenceDataModel

import parsers
from crab.metrics import pearson_correlation
from crab.similarities import UserSimilarity
from crab.recommenders.knn import UserBasedRecommender
import numpy as np

def crab_main(vectorized_train_data,vectorized_test_data):
    crab_mat = parsers.crab_costum_matrix(vectorized_train_data)

    model = MatrixPreferenceDataModel(crab_mat)
    similarity = UserSimilarity(model, pearson_correlation)
    recommender = UserBasedRecommender(model, similarity, with_preference=True)
    result = []
    for item in vectorized_test_data:
        result.append(recommender.estimate_preference(item[0],item[1]))
    return np.array(result)