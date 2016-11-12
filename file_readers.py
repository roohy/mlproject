import numpy as np

def load_data( file_name ):
    result_id = []
    result = []

    with open(file_name,'r') as user_data:
        for line in user_data:
            item = (line[:-1]).split('\t')
            for idx, i in enumerate(item):
                if '/' in i:
                    item[idx] = i.split('/')
            result.append(item[1:])
            result_id.append(item[0])
    return result,result_id

def invited_info_loader(file_name):
    result = []
    with open(file_name,'r') as file:
        for line in file:
            item = (line[:-1]).split('\t')
            result.append(item)
    return result

def test_loader(file_name):
    result = []
    with open(file_name,'r') as file:
        header = file.readline()
        for line in file:
            item = (line[:-2]).split(',')
            print item
            result.append(item)
    return result


def logistic_writer(labels, data):
    with open("logistic_result", 'w') as f:
        f.write("qid,uid,label\n")
        for i in range(data.shape[0]):
            f.write(labels[i][0]+','+labels[i][1]+','+str(data[i])+'\n')