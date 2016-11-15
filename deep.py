
import numpy as np

from keras.layers import Input, Dense
from keras.models import Sequential
import keras.regularizers as Reg
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from keras.utils.np_utils import to_categorical


from normalizer import full_normalize,temp_normalize
import matplotlib.pyplot as plt
import PCA
import gc

def compiler(user_data,question_data, relation_list):
    result = []#np.zeros((len(relation_list),user_data.shape[1]+question_data.shape[1]))
    print "relation shape ",len(relation_list)
    for item in relation_list:
        result.append(np.concatenate(([user_data[item[0]],question_data[item[1]]])))
    #print result
    print "haaah"
    return np.array(result)


def datafer(tX,tY):
    pass

def genmodel(num_units, actfn='relu', reg_coeff=0.0, last_act='softmax'):
	''' Generate a neural network model of approporiate architecture
	Args:
		num_units: architecture of network in the format [n1, n2, ... , nL]
		actfn: activation function for hidden layers ('relu'/'sigmoid'/'linear'/'softmax')
		reg_coeff: L2-regularization coefficient
		last_act: activation function for final layer ('relu'/'sigmoid'/'linear'/'softmax')
	Output:
		model: Keras sequential model with appropriate fully-connected architecture
	'''

	model = Sequential()
	for i in range(1, len(num_units)):
		if i == 1 and i < len(num_units) - 1:
			model.add(Dense(input_dim=num_units[0], output_dim=num_units[i], activation=actfn,
				W_regularizer=Reg.l2(l=reg_coeff), init='glorot_normal'))
		elif i == 1 and i == len(num_units) - 1:
			model.add(Dense(input_dim=num_units[0], output_dim=num_units[i], activation=last_act,
				W_regularizer=Reg.l2(l=reg_coeff), init='glorot_normal'))
		elif i < len(num_units) - 1:
			model.add(Dense(output_dim=num_units[i], activation=actfn,
				W_regularizer=Reg.l2(l=reg_coeff), init='glorot_normal'))
		elif i == len(num_units) - 1:
			model.add(Dense(output_dim=num_units[i], activation=last_act,
				W_regularizer=Reg.l2(l=reg_coeff), init='glorot_normal'))
	return model










def deep_main(user_data,question_data, train_data, test_data):
    #preparing the model
    C= 0.4
    model = 0




    #question_data = temp_normalize(question_data)
    #user_data = temp_normalize(user_data)
    print "prePCAing!!!"
    qMODEL,question_data = PCA.main_plot_pca(question_data,100)
    uMODEL,user_data = PCA.main_plot_pca(user_data,100)
    del qMODEL,uMODEL
    #preparing data
    gc.collect()
    print "compiling training data"
    X_tr = compiler(user_data,question_data,train_data)

    print "compiling test data"
    X_test = compiler(user_data,question_data,test_data)

    #del user_data,question_data
    print "normalizing"
    #X_tr,X_test = full_normalize(X_tr,X_test)
    print "training PCA"
    #pca_model, X_tr = PCA.main_plot_pca(X_tr,90)
    print "testing PCA"
    #X_test = PCA.transform(X_test,pca_model)

    print "transformed"
    #train model
    train_data = np.array(train_data)
    Y = train_data[:,2]
    Y[Y==-1] = 0
    arch = [X_tr.shape[1],450,500,500,800,800,800,2]
    actfn = 'linear'
    last_act = 'softmax'
    sgd_lr = 0.00001
    sgd_decay = 0.000001
    sgd_mom = 0.0
    sgd_Nesterov = False
    reg_coeff = 0.000001

    # model = linear_model.LogisticRegression(penalty='l2',n_jobs='10',C=C)
    call_ES = EarlyStopping(monitor='val_acc', patience=6, verbose=1, mode='auto')

    model = genmodel(num_units=arch, actfn=actfn, reg_coeff=reg_coeff,
                     last_act=last_act)
    # Compile Model
    sgd = SGD(lr=sgd_lr, decay=sgd_decay, momentum=sgd_mom,
              nesterov=sgd_Nesterov)
    model.compile(loss='categorical_crossentropy', optimizer=sgd,
                  metrics=['accuracy'])
    num_epoch = 100
    batch_size = 1000
    verbose = False

    new_Y = to_categorical(Y)
    #print new_Y.shape,X_tr,X_test
    X_tr,X_test = full_normalize(X_tr,X_test)
    print "fitting started"
    model.fit(X_tr, new_Y, nb_epoch=num_epoch, batch_size=batch_size,
              verbose=verbose)
    print "fitting ended"
    print model.evaluate(X_tr, new_Y, batch_size=batch_size, verbose=verbose)
    print "--------"
    res = model.predict_proba(X_test, batch_size=batch_size, verbose=verbose)
    #print res
    print res.shape
    return res[:,1]



def sigmoid_main(user_data,question_data, train_data, test_data):
    #preparing the model
    C= 0.4
    model = 0




    #question_data = temp_normalize(question_data)
    #user_data = temp_normalize(user_data)
    print "prePCAing!!!"
    qMODEL,question_data = PCA.main_plot_pca(question_data,100)
    uMODEL,user_data = PCA.main_plot_pca(user_data,100)
    del qMODEL,uMODEL
    #preparing data
    gc.collect()
    print "compiling training data"
    X_tr = compiler(user_data,question_data,train_data)

    print "compiling test data"
    X_test = compiler(user_data,question_data,test_data)

    #del user_data,question_data
    print "normalizing"
    #X_tr,X_test = full_normalize(X_tr,X_test)
    print "training PCA"
    #pca_model, X_tr = PCA.main_plot_pca(X_tr,90)
    print "testing PCA"
    #X_test = PCA.transform(X_test,pca_model)

    print "transformed"
    #train model
    train_data = np.array(train_data)
    Y = train_data[:,2]
    Y[Y==-1] = 0
    arch = [X_tr.shape[1],200,300,500,500,800,800,1]
    actfn = 'relu'
    last_act = 'sigmoid'
    sgd_lr = 0.00001
    sgd_decay = 0.000001
    sgd_mom = 0.0
    sgd_Nesterov = False
    reg_coeff = 0.000001

    # model = linear_model.LogisticRegression(penalty='l2',n_jobs='10',C=C)
    call_ES = EarlyStopping(monitor='val_acc', patience=6, verbose=1, mode='auto')

    model = genmodel(num_units=arch, actfn=actfn, reg_coeff=reg_coeff,
                     last_act=last_act)
    # Compile Model
    sgd = SGD(lr=sgd_lr, decay=sgd_decay, momentum=sgd_mom,
              nesterov=sgd_Nesterov)
    model.compile(loss='categorical_crossentropy', optimizer=sgd,
                  metrics=['accuracy'])
    num_epoch = 100
    batch_size = 1000
    verbose = False

    #new_Y = to_categorical(Y)
    #print new_Y.shape,X_tr,X_test
    X_tr,X_test = full_normalize(X_tr,X_test)
    print "fitting started"
    model.fit(X_tr, Y, nb_epoch=num_epoch, batch_size=batch_size,
              verbose=verbose)
    print "fitting ended"
    print model.evaluate(X_tr, Y, batch_size=batch_size, verbose=verbose)
    print "--------"
    res = model.predict_proba(X_test, batch_size=batch_size, verbose=verbose)
    res2 = model.predict(X_test,batch_size=batch_size,verbose=verbose)
    #print res
    print res.shape
    print "now res2",res2.shape
    print res2
    return res2