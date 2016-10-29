import numpy as np
from file_readers import *
from parsers import *
USER_DATA_ADDR = "./bytecup2016data/user_info.txt"
QUESTION_DATA_ADDR = "./bytecup2016data/question_info.txt"
INVITED_DATA_ADDR = './bytecup2016data/invited_info_train.txt'
VALIDATION_DATA_ADDR = './bytecup2016data/validate_nolabel.txt'


if __name__ == '__main__':
    print "Reading data..."
    user_data,user_id = load_data(USER_DATA_ADDR)
    question_data,question_id = load_data(QUESTION_DATA_ADDR)
    train_data = invited_info_loader(INVITED_DATA_ADDR)

    # vectorize(user_data,question_data)
    # print user_data

    