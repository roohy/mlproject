import numpy as np
import graphlab as gl
import graphlab.numpy as gnp


def glraw():
    usf = gl.SFrame(data='./bytecup2016data/sfuser_info.txt', format='tsv')
    qsf = gl.SFrame(data='./bytecup2016data/sfquestion_info.txt', format='tsv')
    tsf = gl.SFrame(data='./bytecup2016data/sfinvited_info_train.txt', format='tsv')
    testsf = gl.SFrame(data='./bytecup2016data/sfvalidate_nolabel.txt', format='csv')
    model = gl.recommender.create(observation_data=tsf, user_id='uid', item_id='qid', target='value', user_data=usf,
                                  item_data=qsf, ranking=False)
    result  = model.predict(dataset=testsf)
    result = gnp.array(result)
    result = result - result.min()
    result = result/result.max()
    return result

