import numpy as np
import pandas as pd
from data import *
import matplotlib.pyplot as plt

u = np.floor(np.sqrt(M)); v = np.ceil(float(M-6)/u)

# change variable for the histogram you want
i = 5

plt.hist(X[:,i].astype(float) )
plt.xlabel(attribute_names[i])
plt.ylim(0,N)
    
plt.show()
