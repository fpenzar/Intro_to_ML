from matplotlib.pyplot import (figure, subplots, boxplot, title, xticks, ylim, 
                               show, setp, sca)
import numpy as np
import pandas as pd
from transform import *

fig, ax = subplots(1,2, figsize=(20, 10))

class_mask0 = (y==0) # binary mask to extract elements of class c
class_mask1 = (y==1)
class_mask2 = (y==2)
class_mask3 = (y==3)
class_mask4 = (y==4)
class_mask5 = (y==5)

attributes_to_plot = [11, 13] # 3, 5, 11, 13

colors = ['orange', 'red', 'blue', 'cyan', 'green', 'yellow']

for i in range(2):
    temp = [X[(y==0), attributes_to_plot[i]].astype(float),X[(y==1), attributes_to_plot[i]].astype(float),
            X[(y==2), attributes_to_plot[i]].astype(float),X[(y==3), attributes_to_plot[i]].astype(float),
            X[(y==4), attributes_to_plot[i]].astype(float),X[(y==5), attributes_to_plot[i]].astype(float)]
    
    bplot = ax[i].boxplot(temp, patch_artist=True)
    ax[i].set_title(attribute_names[attributes_to_plot[i]], fontsize= 15)
    ax[i].set_xticklabels(list(class_names.keys()), rotation=45, fontsize=15)
    # ax[i].set_yticklabels(fontsize=15)
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    for median in bplot['medians']:
        median.set_color('black')


fig.tight_layout()
show()
