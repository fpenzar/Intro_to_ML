import numpy as np
from scipy.io import loadmat
import sklearn.linear_model as lm
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from toolbox_02450 import rlr_validate, train_neural_net, draw_neural_net
from transform import *
import torch


# DATA PREPROCESSING
# subtract the mean and standardize the data
cols_to_discard = 0
X = X[:, 1:N-cols_to_discard].astype(float)

Y = X - np.ones((N, 1))*X.mean(0)
Y = Y*(1/np.std(Y,0))
X = Y


# X_cols = list([2,3,4,7,11,12,13])
#X_cols = [2,3,4,7,11,12,13]
X_cols = list(range(0,len(attribute_names) - 6))
X = X[:,X_cols]
N, M = X.shape
# END DATA PREPROCESSING


## Crossvalidation
# Create crossvalidation partition for evaluation
K = 10
CV = model_selection.KFold(n_splits=K,shuffle=True)
w_rlr = np.empty((M,K))


error_train_baseline = np.empty((K,1))
error_test_baseline = np.empty((K,1))

error_train_KNN = np.empty((K,1))
error_test_KNN = np.empty((K,1))

error_train_logistic = np.empty((K,1))
error_test_logistic = np.empty((K,1))


#defintion of regularization logistic model
lambdas = np.power(10.,range(-3,6))

#definition of KNN
no_of_different_neighbours = [1,2,3,4,5,6,7,8,9]

#### !!! there needs to be the same no of lambdas and no_of_different_neighbours !!!!
print("-------------------------------------------")
print('Outer fold    KNN      Logistic regression   baseline')

k=0
for train_index, test_index in CV.split(X):
    # print(f"outer fold: {k+1}")
    # extract training and test set for current CV fold
    X_train = X[train_index,:]
    X_train_logistic = np.concatenate((np.ones((X_train.shape[0],1)),X_train),1)
    y_train = y[train_index]
    X_test = X[test_index,:]
    X_test_logistic = np.concatenate((np.ones((X_test.shape[0],1)),X_test),1)
    y_test = y[test_index]
    internal_cross_validation = 10


    # Find the value with the most repetitions
    unique_values, counts = np.unique(y_train, return_counts=True)
    most_common_value = unique_values[np.argmax(counts)]
    print("most common continent", most_common_value)
    print("Count:", np.max(counts))
    print("y_test", y_test)
    #inner loop 
    
    #inner fold for regularization
    best_lambda = None
    best_logistic_error = 10000
    
    #inner fold for KNN
    best_k = 0
    best_knn_error = 10000
    
    for train_index_inner, test_index_inner in CV.split(X_train):
        
        X_train_inner = X_train[train_index_inner,:]
        X_train_inner_logistic = X_train_logistic[train_index_inner,:]
        y_train_inner = y_train[train_index_inner]
        X_test_inner = X_train[test_index_inner,:]
        X_test_inner_logistic = X_train_logistic[test_index_inner,:]
        y_test_inner = y_train[test_index_inner]
        
        
        for i in range(len(lambdas)):
            
            regularization_strength = lambdas[i]
            mdl = lm.LogisticRegression(solver='lbfgs', multi_class='multinomial', 
                                           tol=1e-4, random_state=1, 
                                           penalty='l2', C=1/regularization_strength, max_iter=5000)
            mdl.fit(X_train_inner_logistic,y_train_inner)
            y_test_est = mdl.predict(X_test_inner_logistic)
    
            test_error_rate_logistic = np.sum(y_test_est!=y_test_inner) / len(y_test_inner)
            
            if  test_error_rate_logistic < best_logistic_error:
                best_lambda = regularization_strength
                best_logistic_error = test_error_rate_logistic
                
           
            
            k_neighbours = no_of_different_neighbours[i]
            
            knclassifier = KNeighborsClassifier(n_neighbors=k_neighbours);
            knclassifier.fit(X_train_inner, y_train_inner);
            y_est = knclassifier.predict(X_test_inner);
            test_error_rate_knn = np.sum(y_est!=y_test_inner)/len(y_test_inner)
            
            if  test_error_rate_knn < best_knn_error:
                best_k = k_neighbours
                best_knn_error = test_error_rate_knn
    
    #outer loop
    
    # Baseline model error
    y_est_baseline = np.full(len(y_test),most_common_value).T
    error_test_baseline[k] = np.sum(y_test!=y_est_baseline) / len(y_test)
    
    # Logistic model error
    mdl = lm.LogisticRegression(solver='lbfgs', multi_class='multinomial', 
                                   tol=1e-4, random_state=1, 
                                   penalty='l2', C=1/best_lambda, max_iter=5000)
    mdl.fit(X_train_logistic,y_train)
    y_test_est = mdl.predict(X_test_logistic)
    error_test_logistic[k] = np.sum(y_test_est!=y_test) / len(y_test)

    # KNN error rate
    knclassifier = KNeighborsClassifier(n_neighbors=best_k);
    knclassifier.fit(X_train, y_train);
    y_est = knclassifier.predict(X_test);
    error_test_KNN[k] = np.sum(y_est!=y_test)/len(y_test)
    
        
    
    print('fold: ' + str(k+1))
    print('KNN:')
    print('best k: '+ str(best_k)+" error rate: "+str(error_test_KNN[k]))
    print("Logistic classification: ")
    print("best lambda: "+ str(best_lambda)+" error rate: "+str(error_test_logistic[k]))
    print("Baseline: ")
    print("error rate: "+str(error_test_baseline[k]))

    k+=1
    