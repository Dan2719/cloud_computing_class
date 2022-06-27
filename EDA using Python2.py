#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\Learning\Documents\_MZUNI\LEVEL2\SEM1\DATA WRANGLING & EXPLORATORY DATA ANALYSIS-BICT2306\datasets\ChinthecheTXML.csv")


# In[3]:


#1 Understanding the data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.describe()


# In[8]:


data.columns


# In[9]:


data.nunique()


# In[10]:


data['Gender'].unique()


# In[11]:


# Data Cleaning of the file


# In[12]:


data.isnull().sum()


# In[14]:


ChinthecheTXML = data.drop(['#','Refused (Stopped)'], axis=1)


# In[15]:


ChinthecheTXML.head()


# In[33]:


#3 Relationship analysis


# In[16]:


corelation = ChinthecheTXML.corr()


# In[17]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)


# In[18]:


sns.pairplot(ChinthecheTXML)


# In[20]:


sns.relplot(x= 'IIT 6+ mo', y='Age group', hue='Gender', data=ChinthecheTXML)


# In[21]:


sns.relplot(x= 'IIT <3 mo', y='Age group', hue='Gender', data=ChinthecheTXML)


# In[22]:


sns.relplot(x= 'IIT 3-5 mo', y='Age group', hue='Gender', data=ChinthecheTXML)


# In[25]:


sns.relplot(x= 'IIT 3-5 mo', y='IIT 6+ mo', hue='Age group', data=ChinthecheTXML)


# In[28]:


sns.displot(ChinthecheTXML['Transferred out'])


# In[30]:


sns.catplot(x='Transferred out', kind='box', data=ChinthecheTXML)


# In[ ]:




