import numpy as np
from file_readers import *
USER_DATA_ADDR = "./bytecup2016data/user_info.txt"




if __name__ == '__main__':
    print "Reading data..."
    user_data = load_user_data(USER_DATA_ADDR)
    print user_data[1]
    