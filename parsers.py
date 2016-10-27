
import numpy as np
def dictionary_generator(data_list):
    tag_dic = {}
    word_dic = {}
    letter_dic = {}
    tag_counter = 0
    word_counter = 0 
    letter_counter = 0
    for items in data_list:
        for item in items[1]:
            if item in tag_dic: 
                


def vectorize_user(user_data):
    print user_data[1]