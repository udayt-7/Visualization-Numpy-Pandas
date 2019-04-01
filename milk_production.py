#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[32]:


data = pd.read_csv('milk_production.csv')
data = data.fillna(0)
data.head()


# In[33]:


col_names = ['Category','State','C2010-11','C2011-12','C2013-14','C2014-15','C2015-16','B2010-11','B2011-12','B2013-14','B2014-15','B2015-16','G2010-11','G2011-12','G2013-14','G2014-15','G2015-16']
data.columns = col_names


# In[34]:


cow_data = data.iloc[:,0:7]
cow_data.head()


# In[35]:


buf_data = data.iloc[:,[0,1,7,8,9,10,11]]
buf_data.head()


# In[36]:


goat_data = data.iloc[:,[0,1,12,13,14,15,16]]
goat_data.head()


# In[37]:


# Which state has produced max milk in year 2013-14?
data['Total-2013-14'] = data['C2013-14'] + data['B2013-14']+ data['G2013-14']
q1 = data[data['Total-2013-14'] == max(data['Total-2013-14'])]['State']
q1


# In[43]:


# List top 5 milk producing states in each year from 2010 to 2015
data['Total-2010-11'] = data['C2010-11'] + data['B2010-11']+ data['G2010-11']
data['Total-2011-12'] = data['C2011-12'] + data['B2011-12']+ data['G2011-12']
data['Total-2014-15'] = data['C2014-15'] + data['B2014-15']+ data['G2014-15']
data['Total-2015-16'] = data['C2015-16'] + data['B2015-16']+ data['G2015-16']
q2_1 = list(data.sort_values('Total-2010-11',ascending = False).head()['State'].values)
q2_2 = list(data.sort_values('Total-2011-12',ascending = False).head()['State'].values)
q2_3 = list(data.sort_values('Total-2013-14',ascending = False).head()['State'].values)
q2_4 = list(data.sort_values('Total-2014-15',ascending = False).head()['State'].values)
q2_5 = list(data.sort_values('Total-2015-16',ascending = False).head()['State'].values)
print(q2_1)


# In[45]:


data.head()


# In[49]:


# List 5 states (if present) whose total milk production is increased for last three years.

#q4 = data[data['Total-2013-14'] <= data['Total-2014-15']]
#q4 = q4[q4['Total-2014-15'] <= q4['Total-2015-16']]
## or
q4 = data[(data['Total-2013-14'] <= data['Total-2014-15']) & (data['Total-2014-15'] <= data['Total-2015-16'])]
q4.head()


# In[63]:


## Draw line graph showing total milk production for last 5 years of selected state

state = 'Karnataka'
lin_data = data[data['State'] == state]
lin_data = lin_data.iloc[:,-5:]
lin_data = lin_data.iloc[0].values
lin_data
#x_ticks = [1,2,3,4,5]
x_ticks = ['2010-11','2011-12','2013-14','2014-15','2015-16']
plt.plot(x_ticks,lin_data, marker = '*',label = state)
plt.legend()
plt.show()


# In[75]:


## Draw subplots of pie charts showing 
## % milk productions by cow, buffalo and goat for last 4 years of selected state.
state = 'Karnataka'
pie1 = data[data['State'] == state]
labels = ['Cow','Buffalo','Goat']
plt.figure(figsize = (20,20))
pie1 = pie1.loc[:,['C2011-12','B2011-12','G2011-12']]
pie1 = pie1.values[0]
plt.subplot(2,2,1)
plt.pie(pie1,labels = labels, autopct= '%1.1f%%' )

##
pie2 = data[data['State'] == state]
pie2 = pie2.loc[:,['C2013-14','B2013-14','G2013-14']]
pie2 = pie2.values[0]

plt.subplot(2,2,2)
plt.pie(pie2,labels = labels, autopct= '%1.1f%%' )
##
pie3 = data[data['State'] == state]
pie3 = pie3.loc[:,['C2014-15','B2014-15','G2014-15']]
pie3 = pie3.values[0]

plt.subplot(2,2,3)
plt.pie(pie3,labels = labels, autopct= '%1.1f%%' )
##
pie4 = data[data['State'] == state]
pie4 = pie4.loc[:,['C2015-16','B2015-16','G2015-16']]
pie4 = pie4.values[0]
plt.subplot(2,2,4)
plt.pie(pie4,labels = labels, autopct= '%1.1f%%' )
plt.show()


# In[142]:


data['Total'] = np.sum(data.loc[:,['Total-2010-2011','Total-2011-12','Total-2013-14','Total-2014-15','Total-2015-16']], axis = 1)


# In[143]:


data = data.sort_values('Total', ascending = False)
data


# In[147]:


## Draw stacked bar graph showing total milk production of all states and UT for last 5 years.
q6 = data.iloc[[0,1,2,10]]
#q6 = q6.iloc[:,-5:]
x_labels = list(q6['State'])
#r = [x for x in range(0,10,1)]
barWidth = 0.75
plt.bar(x_labels,q6['Total-2010-11'],width = barWidth, color = 'Red', label = '2010-11')
plt.bar(x_labels,q6['Total-2011-12'],width = barWidth,bottom = q6['Total-2010-11'], color = 'Blue', label = '2011-12')
plt.bar(x_labels,q6['Total-2013-14'],width = barWidth,bottom = np.sum(q6.loc[:,['Total-2010-2011','Total-2011-12']], axis = 1), color = 'Yellow', label = '2013-14')
plt.bar(x_labels,q6['Total-2014-15'],width = barWidth,bottom = np.sum(q6.loc[:,['Total-2010-2011','Total-2011-12','Total-2013-14']], axis = 1), color = 'Green', label = '2014-15')
plt.bar(x_labels,q6['Total-2015-16'],width = barWidth,bottom = np.sum(q6.loc[:,['Total-2010-2011','Total-2011-12','Total-2013-14','Total-2014-15']], axis = 1), color = 'Orange', label = '2015-16')
plt.legend()
plt.show()


# In[ ]:




