
import numpy as np
def dictionary_generator(data_list):
    tag_dic = {}
    word_dic = {}
    letter_dic = {}
    tag_counter = 0
    word_counter = 0 
    letter_counter = 0
    for items in data_list:
        for item in items[0]:
            if item not in tag_dic: 
                tag_dic[item] = tag_counter
                tag_counter+= 1
        for item in items[1]:
            if item not in word_dic:
                word_dic[item] = word_counter
                word_counter += 1
        for item in items[2]:
            if item not in letter_dic:
                letter_dic[item] = letter_counter
                letter_counter += 1
    return tag_dic,tag_counter,word_dic,word_counter,letter_dic,letter_counter

def 


def vectorize_user(user_data):
    print user_data[1]