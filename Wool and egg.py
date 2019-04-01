#!/usr/bin/env python
# coding: utf-8

# In[152]:


# Wool and egg production:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wools_eggs.csv")
df = df.fillna(0)
df.head(5)


# In[ ]:





# In[155]:


col = ['Category','State','E2009','E2010','E2011','E2012','E2013','E2014','E2015','W2009','W2010','W2011','W2012','W2013','W2014','W2015',]
df.columns = col
df.head()


# In[156]:


# Which state has produced max wool in year 2013-14?

max13 = df[['State','W2013']]
max13 = max13.sort_values('W2013',ascending = False)
max13 = max13.set_index('State')
max13 = max13.drop(['All India'])
max13.head(1)

# List top 5 egg producing states in each year from 2009 to 2015
# Calculate average wool and eggs production in each year for selected state.
# List 5 states (if present) whose total eggs production is increased for last three years.
# Visualizations:
# Draw line graph showing total wool and eggs production for last 5 years of selected state
# Draw stacked bar graph showing total milk production of all states and UT for last 5 years.


# In[163]:


# List top 5 egg producing states in each year from 2009 to 2015

onlyegg = df.set_index('State')
onlyegg = onlyegg.drop(['All India'])
onlyegg = onlyegg.iloc[:,2:8]

t10 = onlyegg[['E2010']].sort_values('E2010',ascending = False).head(5)
t11 = onlyegg[['E2011']].sort_values('E2011',ascending = False).head(5)
t12 = onlyegg[['E2012']].sort_values('E2012',ascending = False).head(5)
t13 = onlyegg[['E2013']].sort_values('E2013',ascending = False).head(5)
t14 = onlyegg[['E2014']].sort_values('E2014',ascending = False).head(5)
t15 = onlyegg[['E2015']].sort_values('E2015',ascending = False).head(5)


# In[ ]:







# In[169]:


# Calculate average wool and eggs production in each year for selected state.

# st = df.set_index('State')
# st = st.loc['Karnataka']
# st = pd.DataFrame({'category':st.index, 'numbers':st.values})
# st = st.drop([0])
# ogg = st.iloc[:7,:]
# owl = st.iloc[7:14,:]

# ogg


# In[164]:


# List 5 states (if present) whose total eggs production is increased for last three years.
ds = onlyegg.reset_index()

State = np.where((ds['E2012'] <= ds['E2013'])&(ds['E2013'] <= ds['E2014'])&(ds['E2014'] <= ds['E2015']) , ds['State'], np.nan)
State
cleanedState = [x for x in State if str(x) != 'nan']
cleanedState[:5]


# In[ ]:





# In[55]:


# Visualizations:
# Draw line graph showing total wool and eggs production for last 5 years of selected state

# def perc(state):
    
#     plt.figure(figsize=(20, 15))
#     st = df.drop(df.columns[[-1]], axis=1) 
#     st = st.set_index('States/Uts (Col. 2)')
#     st = st.loc[state]
#     st = pd.DataFrame({'category':st.index, 'numbers':st.values})
#     st = st.drop([0])
#     st_data = list(st.numbers)
#     st_names = list(st.category)
#     plt.pie(st_data, labels = st_names, autopct= '%1.1f%%')
    
#     plt.show()
    
# s=input("Enter state:")
# perc(s)




# In[167]:


# col = ['Category','State','E2009','E2010','E2011','E2012','E2013','E2014','E2015','W2009','W2010','W2011','W2012','W2013','W2014','W2015',]
# df.columns = col
# df
st = df.set_index('State')
st = st.loc['Karnataka']
st = pd.DataFrame({'category':st.index, 'numbers':st.values})
st = st.drop([0])
ogg = st.iloc[:7,:]
owl = st.iloc[7:14,:]
catw = list(owl.category)
cate = list(ogg.category)


plt.figure(figsize=(15, 12))


#EGGS
plt.subplot(2,1,1)
plt.plot(ogg.numbers)

#WOOL
plt.subplot(2,1,2)
plt.plot(owl.numbers)

#plt.xticks(owl.category)

owl


# In[168]:


# Draw stacked bar graph showing total egg production of all states and UT for last 5 years.
()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[165]:



#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]


#plot data
plt.plot(x, y, linestyle="dashdot", marker="*", color="blue", label = 'Line Example')	

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

# add legend
plt.legend()

#title
plt.title("Simple plot")

#show plot
plt.show()


# In[ ]:




