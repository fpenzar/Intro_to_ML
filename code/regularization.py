
from matplotlib.pylab import (figure, semilogx, loglog, xlabel, ylabel, legend, 
                           title, subplot, show, grid)
import numpy as np
from scipy.io import loadmat
import sklearn.linear_model as lm
from sklearn import model_selection
from toolbox_02450 import rlr_validate
from transform import *

# subtract the mean and standardize the data
cols_to_discard = 0
X = X[:, 1:N-cols_to_discard].astype(float)

Y = X - np.ones((N, 1))*X.mean(0)
Y = Y*(1/np.std(Y,0))
X = Y

tertiary_enrollment_idx = 9 #attribute_names.index('Gross tertiary education(%)')
y = X[:,tertiary_enrollment_idx]

X_cols = list([2,3,4,7,11,12,13])
# X_cols = list(range(0,tertiary_enrollment_idx)) + list(range(tertiary_enrollment_idx+1,len(attribute_names) - 6))
X = X[:,X_cols]


# Add offset attribute
X = np.concatenate((np.ones((X.shape[0],1)),X),1)
attribute_names = [u'Offset']+attribute_names[1:]
M = M+1


# Values of lambda
lambdas = np.power(10.,range(-3,6))


internal_cross_validation = 10    

X_train = X
y_train = y

opt_val_err, opt_lambda, mean_w_vs_lambda, train_err_vs_lambda, test_err_vs_lambda = rlr_validate(X_train, y_train, lambdas, internal_cross_validation)


figure(10, figsize=(12,8))
subplot(1,2,1)
semilogx(lambdas,mean_w_vs_lambda.T[:,1:],'.-') # Don't plot the bias term
xlabel('Regularization factor')
ylabel('Mean Coefficient Values')
grid()

subplot(1,2,2)
title('Optimal lambda: 1e{0}'.format(np.log10(opt_lambda)))
loglog(lambdas,train_err_vs_lambda.T,'b.-',lambdas,test_err_vs_lambda.T,'r.-')
xlabel('Regularization factor')
ylabel('Squared error (crossvalidation)')
legend(['Train error','Validation error'])
grid()

show()