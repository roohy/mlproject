import numpy as np
from sklearn import linear_model
from normalizer import full_normalize,temp_normalize
import matplotlib.pyplot as plt
import PCA
import gc

def prob_plotter(series,series2):
    plt.figure(1, figsize=(4, 3))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    for item in series:
        plt.plot(item, linewidth=2)
    plt.axis('tight')
    plt.xlabel('n_components')
    plt.ylabel('explained_variance_')

    plt.savefig("figure_loglike")

def compiler(user_data,question_data, relation_list):
    result = []#np.zeros((len(relation_list),user_data.shape[1]+question_data.shape[1]))
    print "relation shape ",len(relation_list)
    for item in relation_list:
        result.append(np.concatenate(([user_data[item[0]],question_data[item[1]]])))
    #print result
    print "haaah"
    return np.array(result)


def logistic_main(user_data,question_data, train_data, test_data):
    #preparing the model
    C= 0.4
    model = linear_model.LogisticRegression(penalty='l2',n_jobs='10',C=C)
    question_data = temp_normalize(question_data)
    user_data = temp_normalize(user_data)
    print "prePCAing!!!"
    qMODEL,question_data = PCA.main_plot_pca(question_data,50)
    uMODEL,user_data = PCA.main_plot_pca(user_data,50)
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
    print "fitting started"
    model.fit(X_tr , Y)
    print "fitting ended"
    print model.score(X_tr,Y)
    print "--------"
    res = model.predict_proba(X_test)

    return res[:,1]
