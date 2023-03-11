#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-TheCompleteGuide/main/googleplaystore.csv")


# In[3]:


data.head(2)


# 
# ## CORE ML Steps : 
# 
# 1. Data Ingetion(collection gathering)
#   - Read Data from diff file format(csv,json,xml etc)
#   - cloud
#   - Sql and NoSql (read data)
#   - Scrapping 
#   - robust pipeline make in Big data
#   
# 
# 2. EDA( Data Analysis)
# 
# 3. Preprocessing(Feature Endineering)
# 
# 4. Model Building
# 
# 5. Validate or evaluate the Model
# 
# 

# In[ ]:





# ## EDA :
# 
#      1. Profile of data
#      2. Stats Base Analysis
#      3. Graph base Analysis
#      
#      
# - Collection =>> Analysis(EDA (RAW data))                                                                                    =>> Profile of Data(ROWS,COL,MISSING,OUTLIERS,SIZE,DUPLICATE,DTYPE,NUMERICAL,CATEGORICAL,RAM USED,...)                     =>> Data Cleaning => Statistcs Base Analysis(VAR,STD,COV,CORR,CJI-SQUARE,T-test,Z-test,F-test,skewness,MEAN,MODE,MEDIAN,RANGE,PERCENTILE)                                                                            =>>Graph Base Analaysis (Make Satatical Conclusion) based on variable "BOX,SCATTER,KDE,COUNT PLOT,HISTOGRAM,HEAT MAP,........."

# In[24]:


data.shape


# In[9]:


data.sample(2)


# In[10]:


data.info()


# In[14]:


# Numerical col 
data.describe().T


# In[15]:


# Numerical col 
data.describe(include = 'all').T


# In[19]:


# duplicate rows
data[data.duplicated()]


# In[21]:


data['Reviews'].head(5)


# In[23]:


data['Reviews'].shape


# In[25]:


data['Reviews'].dtype


# In[26]:


# Type cast
data.Reviews.str.isnumeric()


# In[29]:


data.Reviews.str.isnumeric().value_counts()


# In[32]:


data[~data.Reviews.str.isnumeric()]


# In[73]:


df = data.copy()


# In[74]:


df['Reviews'].dtype


# In[81]:


df=df.drop(df.index[10472])


# In[82]:


df['Reviews']


# In[83]:


df['Reviews']=df['Reviews'].astype('int')


# In[ ]:





# In[ ]:





# In[85]:


df['Size'] = df['Size'].str.replace("M","000")


# In[86]:


df['Size'] = df['Size'].str.replace("k","")


# In[ ]:





# In[87]:





# In[89]:


import numpy as np
df["Size"]=df["Size"].str.replace('Varies with device',str(np.nan))


# In[90]:


df["Size"].unique()


# In[62]:


df['Size'].unique() 


# In[63]:


df['Size'][0]


# In[92]:


df["Size"]=df["Size"].astype("float")


# In[93]:


for i in df['Size']:
    if i < 10:
        df["Size"] = df["Size"].replace(i,i*1000)


# In[97]:


data["Size"].unique()


# In[ ]:


def 
    else:
        return str(np.nan)
        


# In[98]:


df.columns


# In[101]:


df['Installs'].str.replace("+","")


# In[102]:


df['Installs'].dtype


# In[103]:


df['Installs'][0]


# In[105]:


df["Price"].unique()


# In[106]:


# Create fun to remove character

char_to_remove = ["+",",","$"]
cols_to_clean = ["Installs","Price"]

for item in char_to_remove:
    for col in cols_to_clean:
        df[col] = df[col].str.replace(item,"")


# In[107]:


df.head(2)


# In[108]:


data.head(2)


# In[109]:


df.info()


# In[112]:


df["Install"] =df["Installs"].astype("int")


# In[113]:


df["Price"]=df["Price"].astype("float")


# In[115]:


df["Last Updated"]


# In[117]:


df["Last Updated"] = pd.to_datetime(df["Last Updated"])


# In[118]:


df.head(2)


# In[121]:


df["day"] = df["Last Updated"].dt.day


# In[122]:


df["month"] = df["Last Updated"].dt.month


# In[123]:


df["year"] = df["Last Updated"].dt.year


# In[124]:


df


# In[129]:


df['Android Ver'] = df['Android Ver'].str.replace("and up","")


# In[130]:


df["Android Ver"]=df["Android Ver"].str.replace('Varies with device',str(np.nan))


# In[131]:


df['Android Ver']


# In[ ]:





# ## 
# 
# ##  EDA
#             - Profile of data
#             - stats base analysis(python)
#             - graph based analysis
#             
# ## Feature Engineering

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




