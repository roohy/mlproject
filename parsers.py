
import numpy as np

vector_feature_count = 3 #base_length is the lenght of question vecotr (standard) without is feature counts (three first elements)
def dictionary_generator(data_list):
    tag_dic = {}
    word_dic = {}
    list_ll = []
    letter_dic = {}
    tag_counter = 0
    word_counter = 0 
    letter_counter = 0
    for items in data_list:
        if type(items[0]) == str:
            if items[0] not in tag_dic:
                tag_dic[items[0]] = tag_counter
                tag_counter+=1
        else:
            for item in items[0]:
                list_ll.append(item)
                if item not in tag_dic:
                    tag_dic[item] = tag_counter
                    tag_counter+= 1

        if type(items[1]) == str:
            if item not in word_dic:
                word_dic[items[1]] = word_counter
                word_counter += 1
        else:

            for item in items[1]:
                if item not in word_dic:
                    word_dic[item] = word_counter
                    word_counter += 1
        for item in items[2]:
            if item not in letter_dic:
                letter_dic[item] = letter_counter
                letter_counter += 1
    print tag_counter,word_counter,letter_counter
    print "------"
    list_ll=(list(set(list_ll)))
    list_ll = [int(item) for item in list_ll]
    list_ll.sort()
    print list_ll
    return tag_dic,tag_counter,word_dic,word_counter,letter_dic,letter_counter


def document_vectorize(question_data, tag_dic,word_dic, dim,tag_count):
    result = []
    base_length = len(question_data[0])-vector_feature_count
    for question in question_data:
        temp_vec = np.zeros(dim)
        for item in question[0]:
            if item in tag_dic:
                temp_vec[base_length+tag_dic[item]] +=1
        for item in question[1]:
            if item in word_dic:
                temp_vec[base_length+tag_count+word_dic[item]] +=1
        for i in range(0,base_length):
            temp_vec[i] = question[vector_feature_count+i]
        result.append(temp_vec)
    #return np.array(result)[:,:3+tag_count]
    return np.array(result)
def user_question_test(user_ids,question_ids,test_list):
    result = []
    for item in test_list:
        result.append([user_ids.index(item[1]), question_ids.index(item[0])])
    return result
def user_question(user_ids,question_ids, train_data):
    result = []
    for item in train_data:
        result.append([user_ids.index(item[1]),question_ids.index(item[0]),1 if item[2]=='1' else -1])
    return result

def user_question_matrix(user_ids,question_ids, vectorized_train_data):
    result_mat = np.zeros((len(user_ids),len(question_ids)))
    for item in vectorized_train_data:
        result_mat[item[0],item[1]] = item[2]
    return result_mat


def user_vectorize(user_data,question_data,tag_dic,word_dic, dim,tag_count):
    result = []
    base_length = len(question_data[0]) - vector_feature_count
    for user in user_data:
        temp_vec = np.zeros(dim-base_length)
        for item in user[0]:
            if item in tag_dic:
                temp_vec[ tag_dic[item]] += 1
        for item in user[1]:
            if item in word_dic:
                temp_vec[tag_count + word_dic[item]] += 1
        result.append(temp_vec)
    #return np.array(result)[:,:tag_count]
    return np.array(result)


def user_populate(user_data,question_data, user_id,question_id , answers_vector):
    pass

def vectorize(user_data,question_data):
    tag_dic, tag_counter, word_dic, word_counter, letter_dic, letter_counter = dictionary_generator(user_data+question_data)
    dim = tag_counter+word_counter+len(question_data[0])-vector_feature_count
    user_vector = user_vectorize(user_data,question_data,tag_dic,word_dic,dim,tag_counter)
    question_vector = document_vectorize(question_data,tag_dic,word_dic,dim,tag_counter)
    return user_vector,question_vector


