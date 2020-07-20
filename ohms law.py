#!/usr/bin/env python
# coding: utf-8

# # Ohm's law expt #

# In[ ]:


import matplotlib.pyplot as plt
#import random as random
#import json as json
#import pandas as pd
#import numpy as np


# In[4]:


with open ("exampledata.txt",'r') as f:
    i = 0
    X = []
    Y = []
    for line in f:
        #print(line)
        if line.startswith("#"):
            #print(line)
            continue
        else:
            lineparts = line.split(' ')
            #print(lineparts)
            t = lineparts[0]
            #print(t)
            X = float(lineparts[1])
            #print(X)
            X.append(x)
            #print(X)
            Y = float(lineparts[2])
            #print(y)
            #r = y / x
            #print("resistance = ", r,"ohm")
            Y.append(Y)
            '''print(Y)'''
            #print(Y)
            #print(i,x,y)
            i = i + 1
            #r = y/x
#print(i,x,y)
#print(X,Y)
plt.figure(figsize = [4,4])
plt.scatter(X,Y,color = 'r', marker = 'o')
plt.axis([0, 20, 0, 10])
plt.show()
            
    
    


# In[ ]:




