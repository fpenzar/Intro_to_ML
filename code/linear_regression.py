from transform import *
from matplotlib.pylab import figure, subplot, plot, xlabel, ylabel, hist, show, legend
from scipy.linalg import svd
import sklearn.linear_model as lm

# subtract the mean and standardize the data
cols_to_discard = 0
X = X[:, 1:N-cols_to_discard].astype(float)

Y = X - np.ones((N, 1))*X.mean(0)
Y = Y*(1/np.std(Y,0))
X = Y

# Split dataset into features and target vector
tertiary_enrollment_idx = 9 #attribute_names.index('Gross tertiary education(%)')
y = X[:,tertiary_enrollment_idx]

X_cols = list(range(0,tertiary_enrollment_idx)) + list(range(tertiary_enrollment_idx+1,len(attribute_names) - 1))
X = X[:,X_cols]

# Fit ordinary least squares regression model
model = lm.LinearRegression()
model.fit(X,y)

# Predict alcohol content
y_est = model.predict(X)
residual = y_est-y

# Display scatter plot
figure()

Xe =  np.linspace(1,159,159).reshape(-1,1)
plot(Xe, y, '.')
plot(Xe, y_est, '-')
ylabel('Gross tertiary education'); 
legend(['Data X ','Regression fit (model)'])

#plot(y, y_est, '.')
#xlabel('Gross tertiary education(true)'); ylabel('Gross tertiary education(estimated)');

#hist(residual,30)
#ylabel('Residual (y_estimated - y)');

show()