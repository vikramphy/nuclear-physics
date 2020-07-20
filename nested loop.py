#!/usr/bin/env python
# coding: utf-8

# In[6]:


D = {}
for i in range(5):
    for j in range(5):
        if i == j:
            D.update({(i,j) : 20*i+j})
        elif i!= j:
            D.update({(i,j) : 200*i+j})
print(D)            


# In[ ]:





# In[ ]:





# 
