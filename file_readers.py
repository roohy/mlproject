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