from transform import *
import matplotlib.pyplot as plt
from scipy.linalg import svd

X = X[:, 1:].astype(float)

# subtract the mean and standardize the data
Y = X - np.ones((N, 1))*X.mean(0)
Y = Y*(1/np.std(Y,0))

# svd
U, S, Vh = svd(Y, full_matrices=False)
V = Vh.T

# variance explained
rho = (S*S) / (S*S).sum()

# project the data onto principal component space
Z = Y @ V

# indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA of the data
f = plt.figure()
plt.title('PCA')
#Z = array(Z)
for c in range(C):
    # select indices belonging to class c:
    class_mask = y==c
    plt.plot(Z[class_mask,i], Z[class_mask,j], 'o', alpha=.5)
plt.legend(class_names)
plt.xlabel('PC{0}'.format(i+1))
plt.ylabel('PC{0}'.format(j+1))

# Output result to screen
plt.show()

threshold = 0.9
# plot cumulative variance explained
plt.plot(range(1,len(rho)+1),rho,'x-')
plt.plot(range(1,len(rho)+1),np.cumsum(rho),'o-')
plt.plot([1,len(rho)],[threshold, threshold],'k--')
plt.title('Variance explained by principal components')
plt.xlabel('Principal component')
plt.ylabel('Variance explained')
plt.legend(['Individual','Cumulative','Threshold'])
plt.grid()
plt.title('Variance explained')
plt.show()

# percent of the variance. Let's look at their coefficients:
pcs = [i for i in range(10)]
legendStrs = ['PC'+str(e+1) for e in pcs]
bw = .2
r = np.arange(2,M+1)

fig, ax = plt.subplots()
for i in pcs:
    ax.bar(r+i*bw, V[:,i], width=bw)
ax.set_xticks(r+bw) 
ax.set_xticklabels(attribute_names[1:],rotation=270)
ax.set_xlabel('Attributes')
ax.set_ylabel('Component coefficients')
ax.legend(legendStrs, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid()
plt.title('PCA Component Coefficients')
# plt.xticks(r+bw, attribute_names[1:],rotation=270)
# plt.xlabel('Attributes')
# plt.ylabel('Component coefficients')
# plt.legend(legendStrs)
# plt.grid()
# plt.title('PCA Component Coefficients')
plt.show()