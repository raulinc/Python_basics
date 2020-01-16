#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("this is spartaaa!!!!!")


# In[ ]:





# In[10]:


a=10
b=20
if a>b:
    print(" A>B TRUE")
elif b>a:
    print("B>A FALSE")


# In[ ]:


#numpyyyy 


# In[11]:


import numpy as np


# In[12]:


arr1=np.array([10,20,30,40])
arr1


# In[15]:


arr2d=np.array([[1,2,3],[10,20,30]])
arr2d


# # zeros array

# In[16]:


a1=np.zeros((5,5))
a1


# In[17]:


n2=np.arange(1,21,5)
n2


# In[22]:


n1=np.array([[1,2,3],[9,8,7]])
n1


# In[33]:


n2=np.array([10,20,30])


# In[34]:


n3=np.array([1,2,3])
n3


# In[36]:



np.sum([n3,n2],axis=0)


# In[37]:


rand_arry = np.random.randint(1,20,5)
rand_arry


# In[40]:


np.vstack((n2,n3))


# In[41]:


np.hstack((n2,n3))


# In[42]:


np.column_stack((n2,n3))


# In[ ]:


#pandas it stands for panel data and is the core library for data manipulation and data analysis


# In[43]:


import pandas as pd


# In[44]:


s1= pd.Series([10,20,30,40])
s1


# In[46]:


s1[0]


# In[47]:


s1[0]=60
s1


# In[48]:


s1= pd.Series([10,20,30,40],index=['a','b','c','d'])
s1


# In[49]:


#dictionary
d1={'a':10,"b":20,'c':30}


# In[50]:


s1=pd.Series(d1)


# In[51]:


s1


# In[54]:


#dataframe
d2={"Students":["bob","julia","ram"],"Students_Marks":[20,30,40]}
pd.DataFrame(d2)


# In[ ]:




