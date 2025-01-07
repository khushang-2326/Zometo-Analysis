#!/usr/bin/env python
# coding: utf-8

# # Zometo Data Analysis Project

# # Step 1 Importing Libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Step 2 Create the Data Frame

# In[4]:


dataframe=pd.read_csv('Zomato data .csv')
print(dataframe)


# # Convert The data type of column rate

# In[7]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[8]:


dataframe.info()


# # Type of resturent

# In[9]:


dataframe.head()


# In[10]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Type of Resurent')


# # conclusion - majurity of the restrurant falls in dinning category

# In[11]:


dataframe.head()


# In[17]:


grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'Votes':grouped_data})
plt.plot(result,c='g',marker='o')
plt.xlabel('Type Of restaurant',c='b',size=20)
plt.ylabel('Votes',c='b',size=20)


# # conclusion - Dining restarunts has recived maximum votes

# In[18]:


dataframe.head()


# In[21]:


plt.hist(dataframe['rate'],bins=5)
plt.title('Rating Distribution')
plt.show()


# # conclusion - the majority rasturant recevied ratings from 3.5 to 4

# # Average order spending by couples

# In[23]:


dataframe.head()


# In[24]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # conclusion - tThe majority of couples preferr resturants with an approximate cost of 300rs.

# # Wich mode recevies maximum rating

# In[25]:


plt.figure(figsize =(6,6))
sns.boxplot(x='online_order',y='rate',data =dataframe)


# # conclusion - offline order recevied lower rating in comparison to online order

# In[27]:


dataframe.head()


# In[35]:


pivot_table=dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap='YlGnBu',fmt='d')
plt.title('HeatMap')
plt.xlabel('Online Order')
plt.ylabel('listed_in(type)')
plt.show()


# # conclusion - Dining restaurants primarily accept offline orders,whereas cafes primarily receive offline order.This suggests that clients prefrer to place order in person at restaurants,but prefer online ordering at cafes. 

# In[ ]:




