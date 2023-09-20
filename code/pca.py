from transform import *
import matplotlib.pyplot as plt
from scipy.linalg import svd
from mpl_toolkits.mplot3d import Axes3D

cols_to_discard = 0

X = X[:, 1:N-cols_to_discard].astype(float)

# subtract the mean and standardize the data
Y = X - np.ones((N, 1))*X.mean(0)
Y = Y*(1/np.std(Y,0))

# svd
U, S, Vh = svd(Y, full_matrices=False)
V = Vh.T

# variance explained
rho = (S*S) / (S*S).sum()

print(rho)

# project the data onto principal component space
Z = Y @ V

# indices of the principal components to be plotted
i = 1
j = 2

# Plot PCA of the data
f = plt.figure()
plt.title('PCA')
for c in range(C):
    # select indices belonging to class c:
    class_mask = y==c
    plt.plot(Z[class_mask,i], Z[class_mask,j], 'o', alpha=.5)
plt.legend(class_names)
plt.xlabel('PC{0}'.format(i+1))
plt.ylabel('PC{0}'.format(j+1))

# Output result to screen
plt.show()

# threshold = 0.9
# # plot cumulative variance explained
# plt.plot(range(1,len(rho)+1),rho,'x-')
# plt.plot(range(1,len(rho)+1),np.cumsum(rho),'o-')
# plt.plot([1,len(rho)],[threshold, threshold],'k--')
# plt.title('Variance explained by principal components')
# plt.xlabel('Principal component')
# plt.ylabel('Variance explained')
# plt.legend(['Individual','Cumulative','Threshold'])
# plt.grid()
# plt.title('Variance explained')
# plt.show()

# # percent of the variance. Let's look at their coefficients:
# pcs = [i for i in range(8)]
# legendStrs = ['PC'+str(e+1) for e in pcs]
# bw = .1
# r = np.arange(2,M - cols_to_discard + 1)

# fig, ax = plt.subplots()
# for i in pcs:
#     ax.bar(r+i*bw - 4*bw, V[:,i], width=bw)
# ax.set_xticks(r+bw) 
# ax.set_xticklabels(attribute_names[1:N-cols_to_discard],rotation=270)
# ax.set_xlabel('Attributes')
# ax.set_ylabel('Component coefficients')
# ax.legend(legendStrs, loc='upper left', bbox_to_anchor=(1, 1))
# ax.grid()
# plt.title('PCA Component Coefficients')
# plt.show()


# # Create a figure and a 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Create a 3D scatter plot
# for c in range(C):
#     # select indices belonging to class c:
#     class_mask = y==c
#     ax.scatter(Z[class_mask,0], Z[class_mask,1], Z[class_mask,2], marker='o', alpha=.5)

# # Set labels for the axes
# ax.set_xlabel('PC 1')
# ax.set_ylabel('PC 2')
# ax.set_zlabel('PC 3')
# ax.legend(class_names, loc='upper left', bbox_to_anchor=(-0.2, 1))


# # Set the title
# ax.set_title('Projection of data on first 3 PCs')

# # Show the plot
# plt.show()