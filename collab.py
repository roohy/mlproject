import numpy as np


def show_similarity_pearson(user_question_matrix):
    coefs = np.corrcoef(user_question_matrix)
    print coefs