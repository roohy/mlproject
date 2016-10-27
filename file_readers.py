import numpy as np

def load_data( file_name ):
    result = []
    with open(file_name,'r') as user_data:
        for line in user_data:
            item = (line[:-1]).split('\t')
            for i in item:
                if '/' in i:
                    # print i.split('/')
                    i = 0#i.split('/')
                    print i
            result.append(item)
        print result
    return result