import numpy as np
from file_readers import *
import parsers
import logistic_regression
import deep
import PCA
import collab
USER_DATA_ADDR = "./bytecup2016data/user_info.txt"
QUESTION_DATA_ADDR = "./bytecup2016data/question_info.txt"
INVITED_DATA_ADDR = './bytecup2016data/invited_info_train.txt'
VALIDATION_DATA_ADDR = './bytecup2016data/validate_nolabel.txt'


if __name__ == '__main__':
    print "Reading data..."
    user_data,user_id = load_data(USER_DATA_ADDR)
    question_data,question_id = load_data(QUESTION_DATA_ADDR)
    train_data = invited_info_loader(INVITED_DATA_ADDR)
    test_data = test_loader(VALIDATION_DATA_ADDR)

    user_vector,question_vector = parsers.vectorize(user_data,question_data)


    #------delete part
    del user_data,question_data


    print user_vector.shape,question_vector.shape
    vectorized_train_data = parsers.user_question(user_id,question_id,train_data)
    vectorized_test_data = parsers.user_question_test(user_id,question_id,test_data)

    del question_id,user_id,train_data
    # PCA.main_plot_pca(user_vector)

    #logistic_result = logistic_regression.logistic_main(user_vector,question_vector,vectorized_train_data,vectorized_test_data)
    #logistic_writer(test_data,logistic_result)

    # deepResult = deep.deep_main(user_vector,question_vector,vectorized_train_data,vectorized_test_data)
    deepResult = deep.sigmoid_main(user_vector,question_vector,vectorized_train_data,vectorized_test_data)
    logistic_writer(test_data,deepResult)
    #np.savetxt('user',user_vector,delimiter=',',fmt='%d',newline='\n')
    #np.savetxt('question',question_vector,delimiter=',',fmt='%d',newline='\n')
    #np.savetxt('train',vectorized_train_data,delimiter=',',fmt='%d',newline='\n')

    #vectorized_train_data = parsers.user_question(user_id,question_id,train_data)
    #trainMat = parsers.user_question_matrix(user_id,question_id,vectorized_train_data)
    #ollab.show_similarity_pearson(trainMat)

