import numpy as np

def load_user_data( file_name ):
    result = []
    with open(file_name,'r') as user_data:
        for line in user_data:
            result.append((line[:-1]).split('\t'))
    return result