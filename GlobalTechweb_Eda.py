#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv("new.csv")


# In[2]:


df = data.copy()


# In[3]:


df = df.drop('Unnamed: 0',axis = 1)


# In[4]:


df.head(2)


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df['Valuation']= df['Valuation'].str.replace("$","")


# In[8]:


df['Valuation']= df['Valuation'].str.replace("B","")


# In[9]:


data.head(2)


# In[10]:


df.tail(2)


# In[11]:


df['Type']= df['Type'].str.replace("$","")


# In[12]:


df['Type']= df['Type'].str.replace("M","")


# In[13]:


li = []
li1 = []
for i in range(30):
    li.append(df['Type'][i].split(" ",1)[0])
    li1.append(df['Type'][i].split(" ",1)[1])


# In[14]:


df["Type_Amount"] = li


# In[15]:


df["Type_series"] = li1


# In[16]:


df.describe()


# In[17]:


df.info()


# In[18]:



for i in range(30):
    x = df['Type'][i].split(" ")


# In[19]:


x


# In[20]:


df['Type'][0].split(" ",1)


# In[21]:


df["Type_Amount"] = df["Type_Amount"].str.replace("B","000")


# In[22]:


df['Type_Amount']=df['Type_Amount'].astype('float')


# In[27]:


df['Type_Amount'][3] = 1500


# In[30]:


df = df.drop('Type',axis = 1)


# In[38]:


df.to_csv("TCS_PROJ.csv",header = False,index = False)


# In[35]:


pip install cufflinks


# In[36]:


import cufflinks as cf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[37]:


df.iplot()


# In[ ]:





# In[33]:


df['Company']


# In[ ]:




