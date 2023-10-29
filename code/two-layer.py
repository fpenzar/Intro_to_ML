import numpy as np
from scipy.io import loadmat
import sklearn.linear_model as lm
from sklearn import model_selection
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

tertiary_enrollment_idx = 9 #attribute_names.index('Gross tertiary education(%)')
y = X[:,tertiary_enrollment_idx]

# X_cols = list([2,3,4,7,11,12,13])
X_cols = [2,3,4,7,11,12,13]
# X_cols = list(range(0,tertiary_enrollment_idx)) + list(range(tertiary_enrollment_idx+1,len(attribute_names) - 6))
X = X[:,X_cols]
N, M = X.shape
# END DATA PREPROCESSING


## Crossvalidation
# Create crossvalidation partition for evaluation
K = 10
CV = model_selection.KFold(n_splits=K,shuffle=True)
w_rlr = np.empty((M,K))


# Initialize variables
Features = np.zeros((M,K))
Error_train = np.empty((K,1))
Error_test = np.empty((K,1))
Error_train_fs = np.empty((K,1))
Error_test_fs = np.empty((K,1))

error_train_baseline = np.empty((K,1))
error_test_baseline = np.empty((K,1))

error_train_NN = np.empty((K,1))
error_test_NN = np.empty((K,1))

error_train_regression = np.empty((K,1))
error_test_regression = np.empty((K,1))


#defintion of regularization linear model
lambdas = np.power(10.,range(-3,6))

#definition of neural network
n_hidden_units = [1, 10, 20]
loss_fn = torch.nn.MSELoss() 

print("-------------------------------------------")
print('Outer fold    ANN      Linear regression   baseline')

k=0
for train_index, test_index in CV.split(X):
    print(f"outer fold: {k+1}")
    # extract training and test set for current CV fold
    X_train = X[train_index,:]
    y_train = y[train_index]
    X_test = X[test_index,:]
    y_test = y[test_index]
    internal_cross_validation = 10

    #inner loop 
    
    #inner fold for regularization
    opt_val_err, opt_lambda, mean_w_vs_lambda, train_err_vs_lambda, test_err_vs_lambda = rlr_validate(X_train, y_train, lambdas, internal_cross_validation)
    
    #inner fold for neural network 
    best_final_loss = 10000 #anything large
    best_net = None
    best_learning_curve = None
    best_n = 0
    j = 0
    for train_index_inner, test_index_inner in CV.split(X_train):
        print(f"ANN inner fold: {j+1}")
        j += 1
        # if j == 3: break
        # extract training and test set for current CV fold
        X_train_inner = torch.Tensor(X[train_index_inner,:])
        y_train_inner = y[train_index_inner]
        y_train_inner.resize(len(train_index_inner), 1)
        y_train_inner = torch.Tensor(y_train_inner)
        X_test_inner = torch.Tensor(X[test_index_inner,:])
        y_test_inner = y[test_index_inner]
        y_test_inner.resize(len(test_index_inner), 1)
        y_test_inner = torch.Tensor(y_test_inner)
        
        for n in n_hidden_units:
            model = lambda: torch.nn.Sequential(
                                torch.nn.Linear(M, n), 
                                torch.nn.Tanh(),  
                                torch.nn.Linear(n, 1), 
                                # no final tranfer function, i.e. "linear output"
                                )
            net, final_loss, learning_curve = train_neural_net(model,
                                                               loss_fn,
                                                               X=X_train_inner,
                                                               y=y_train_inner,
                                                               n_replicates=3,
                                                               max_iter=2000)
            if final_loss < best_final_loss:
                best_net = net
                best_learning_curve = learning_curve
                best_final_loss = final_loss
                best_n = n
    
    #outer loop
    
    # Baseline model error
    error_train_baseline[k] = np.square(y_train-y_train.mean()).sum()/y_train.shape[0]
    error_test_baseline[k] = np.square(y_test-y_test.mean()).sum()/y_test.shape[0]
    
    # Regression model error
    # error_train_regression[k] = np.power(y_train-X_train @ mean_w_vs_lambda[:,np.where(lambdas == opt_lambda)[0]],2).mean()
    # error_test_regression[k] = np.power(y_test-X_test @ mean_w_vs_lambda[:,np.where(lambdas == opt_lambda)[0]],2).mean()
    # Estimate weights for the optimal value of lambda, on entire training set
    Xty = X_train.T @ y_train
    XtX = X_train.T @ X_train
    lambdaI = opt_lambda * np.eye(M)
    lambdaI[0,0] = 0 # Do no regularize the bias term
    w_rlr[:,k] = np.linalg.solve(XtX+lambdaI,Xty).squeeze()
    # Compute mean squared error with regularization with optimal lambda
    error_train_baseline[k] = np.square(y_train-X_train @ w_rlr[:,k]).sum()/y_train.shape[0]
    error_test_regression[k] = np.square(y_test-X_test @ w_rlr[:,k]).sum()/y_test.shape[0]

    # Neural network error
    X_train_tensor = torch.Tensor(X_train)
    y_train.resize(X_train.shape[0], 1)
    y_train_tensor = torch.Tensor(y_train)
    y_train_est = best_net(X_train_tensor)
    se = (y_train_est.float()-y_train_tensor.float())**2 # squared error
    mse = (sum(se).type(torch.float)/len(torch.Tensor(y_train))).data.numpy() #mean
    error_train_NN[k] = mse
    
    
    X_test_tensor = torch.Tensor(X_test)
    y_test.resize(X_test.shape[0], 1)
    y_test_tensor = torch.Tensor(y_test)
    y_test_est = best_net(torch.Tensor(X_test))
    se = (y_test_est.float()-torch.Tensor(y_test).float())**2 # squared error
    mse = (sum(se).type(torch.float)/len(torch.Tensor(y_test))).data.numpy() #mean
    error_test_NN[k] = mse
    
    print('fold: ' + str(k+1))
    print('Neural network:')
    print('best n: '+ str(best_n)+" mse: "+str(error_test_NN[k]) + f"  train lost: {best_final_loss}")
    print("Linear regression: ")
    print("best lambda: "+ str(opt_lambda)+" mse: "+str(error_test_regression[k]))
    print("Baseline: ")
    print("mse: "+str(error_test_baseline[k]))

    k+=1
    

# Display results
'''print('\n')
print('Linear regression without feature selection:\n')
print('- Training error: {0}'.format(Error_train.mean()))
print('- Test error:     {0}'.format(Error_test.mean()))
print('- R^2 train:     {0}'.format((error_train_baseline.sum()-Error_train.sum())/error_train_baseline.sum()))
print('- R^2 test:     {0}'.format((error_test_baseline.sum()-Error_test.sum())/error_test_baseline.sum()))
print('Linear regression with feature selection:\n')
print('- Training error: {0}'.format(Error_train_fs.mean()))
print('- Test error:     {0}'.format(Error_test_fs.mean()))
print('- R^2 train:     {0}'.format((error_train_baseline.sum()-Error_train_fs.sum())/error_train_baseline.sum()))
print('- R^2 test:     {0}'.format((error_test_baseline.sum()-Error_test_fs.sum())/error_test_baseline.sum()))'''
