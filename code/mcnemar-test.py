from toolbox_02450 import mcnemar
from transform import *
import numpy as np

y_true = np.array([0, 0, 1, 3, 3, 2, 3, 1, 2, 2, 1, 2, 0, 0, 0, 5, 
          0, 1, 0, 5, 3, 2, 0, 0, 0, 1, 4, 2, 5, 1, 3, 0, 
          3, 1, 2, 0, 0, 0, 0, 2, 3, 2, 1, 1, 0, 0, 1, 0, 
          5, 3, 0, 5, 0, 2, 0, 1, 1, 1, 4, 1, 0, 1, 3, 0, 
          3, 5, 2, 2, 0, 1, 2, 0, 1, 0, 5, 5, 0, 1, 2, 4, 
          3, 3, 2, 3, 2, 2, 0, 1, 1, 0, 2, 0, 0, 2, 1, 0, 
          0, 2, 4, 0, 5, 1, 1, 0, 0, 1, 4, 2, 2, 1, 0, 1, 
          2, 2, 1, 5, 1, 0, 1, 0, 2, 2, 3, 1, 3, 1, 1, 1,
          1, 1, 4, 1, 1, 0, 0, 1, 2, 0, 2, 1, 2, 2, 5, 1, 
          2, 0, 0, 1, 3, 2, 1, 1, 0, 2, 1, 2, 3, 2, 2])

baseline_yhats =  np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

knn_yhats = np.array([0, 0, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 0, 0, 
             1, 1, 0, 1, 1, 2, 0, 0, 0, 0, 4, 2, 1, 1, 1, 0,
             3, 1, 2, 0, 3, 0, 0, 2, 1, 2, 1, 1, 0, 0, 1, 0,
             2, 2, 0, 3, 0, 2, 0, 2, 1, 1, 2, 1, 0, 4, 2, 0, 
             1, 2, 2, 2, 1, 0, 2, 0, 1, 0, 1, 3, 0, 1, 2, 4,
             5, 2, 2, 1, 2, 2, 0, 1, 2, 1, 2, 0, 0, 2, 2, 0, 
             0, 2, 1, 0, 1, 2, 1, 0, 0, 3, 1, 2, 2, 3, 0, 1, 
             2, 2, 3, 2, 1, 0, 2, 0, 2, 2, 0, 1, 1, 2, 1, 1,
             0, 2, 2, 1, 3, 0, 0, 0, 2, 2, 2, 1, 2, 2, 2, 0,
             2, 1, 0, 2, 3, 2, 0, 1, 0, 1, 1, 2, 2, 2, 2])

logistic_yhats = np.array([0, 0, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 0, 0, 0, 5,
                  1, 1, 0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 5, 2, 1, 3,
                  1, 1, 2, 0, 3, 0, 0, 2, 0, 2, 1, 1, 0, 0, 1, 0,
                  5, 2, 0, 5, 1, 2, 0, 3, 1, 3, 5, 2, 0, 4, 4, 0,
                  1, 1, 2, 2, 3, 0, 2, 0, 3, 1, 3, 4, 0, 1, 2, 4,
                  4, 5, 2, 1, 2, 2, 5, 1, 1, 1, 2, 0, 0, 5, 3, 0,
                  0, 2, 1, 0, 3, 4, 3, 5, 0, 1, 0, 2, 1, 1, 0, 1,
                  2, 2, 3, 1, 3, 0, 2, 0, 2, 1, 3, 1, 4, 2, 0, 1,
                  0, 3, 2, 1, 3, 0, 0, 0, 2, 1, 5, 1, 2, 2, 2, 0,
                  2, 0, 0, 2, 1, 2, 1, 1, 0, 1, 1, 2, 3, 2, 2])

alpha = 0.05

print("#### ACCURACIES:")
print("Baseline accuracy:",  np.sum(baseline_yhats==y_true) / len(y_true))
print("KNN accuracy:",  np.sum(knn_yhats==y_true) / len(y_true))
print("Logreg accuracy:",  np.sum(logistic_yhats==y_true) / len(y_true))


print("#### COMPARISON:")
print("Comparing KNN and Logistic regression")
[thetahat, CI, p] = mcnemar(y_true, knn_yhats, logistic_yhats, alpha=alpha)
print("theta = theta_KNN-theta_logreg point estimate", thetahat, " CI: ", CI, "p-value", p)


print("Comparing KNN and baseline")
[thetahat, CI, p] = mcnemar(y_true, knn_yhats, baseline_yhats, alpha=alpha)
print("theta = theta_KNN-theta_baseline point estimate", thetahat, " CI: ", CI, "p-value", p)


print("Comparing baseline and Logistic regression")
[thetahat, CI, p] = mcnemar(y_true, baseline_yhats, logistic_yhats, alpha=alpha)
print("theta = theta_baseline-theta_logreg point estimate", thetahat, " CI: ", CI, "p-value", p)