#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[105]:


# Transport Vehicles
df = pd.read_csv("vehicles.csv")
df.head(5)


# In[109]:


# Find the total number of non-transport vehicles in Karnataka
n_t = df.loc[df['States/Uts (Col. 2)'] == 'Karnataka']
n_t['non_transport_total'] = n_t['Non-Transport - Two Wheelers (Col. 9)'] + n_t['Non-Transport - Cars (Col. 10)'] + n_t['Non-Transport - Jeeps (Col. 11)'] + n_t['Non-Transport - Omni Buses (Col. 12)'] + n_t['Non-Transport - Tractors (Col. 13)'] + n_t['Non-Transport - Trailers (Col. 14)']+ n_t['Non-Transport - Others (Col. 15)']
n_t[['States/Uts (Col. 2)','non_transport_total']]


# In[99]:


# Find the State / UT which has max number of Buses

t_bus = df[['States/Uts (Col. 2)','Transport - Buses (Col. 5)', 'Non-Transport - Omni Buses (Col. 12)']]
t_bus['total_bus'] = t_bus['Transport - Buses (Col. 5)'] + t_bus['Non-Transport - Omni Buses (Col. 12)']
top_bus =t_bus.sort_values("total_bus", ascending = False)
top_bus = top_bus.set_index('States/Uts (Col. 2)')
top_bus = top_bus.drop(['GRAND TOTAL','TOTAL STATES'])
top_bus.head(1)


# In[100]:


# Find the State / UT which has min number of two wheelers
min_t = df[['States/Uts (Col. 2)','Non-Transport - Two Wheelers (Col. 9)']]
min_t = min_t.set_index('States/Uts (Col. 2)')
min_t = min_t.drop(['GRAND TOTAL','TOTAL STATES','TOTAL Uts'])
min_t = min_t.sort_values('Non-Transport - Two Wheelers (Col. 9)')
min_t.head(1)


# In[111]:


# Find the State / UT which has max number of vehicles (transport + non transport)

gt = df.set_index('States/Uts (Col. 2)')
gt = gt.drop(['GRAND TOTAL','TOTAL STATES','TOTAL Uts'])

gt['grand_total'] = gt['Transport - Multi-Axled/ Articulated Vehicles/ Trucks and Lorries (Col. 3)']+gt['Transport - Light Motor Vehicle (Goods) (Col. 4)']+gt['Transport - Buses (Col. 5)']+ gt['Transport - Taxis (Col. 6)']+gt['Transport - Light Motor Vehicle (Passenger) (Col. 7)']+gt['Non-Transport - Two Wheelers (Col. 9)']+gt['Non-Transport - Cars (Col. 10)']+gt['Non-Transport - Jeeps (Col. 11)']+gt['Non-Transport - Omni Buses (Col. 12)']+gt['Non-Transport - Tractors (Col. 13)']+gt['Non-Transport - Trailers (Col. 14)']+gt['Non-Transport - Others (Col. 15)']
gt = gt.sort_values('grand_total', ascending = False)
gt = gt.reset_index()
#gt = gt[['States/Uts (Col. 2)','grand_total']]
top_state = gt.head(1)[['States/Uts (Col. 2)','grand_total']]
top_state


# In[102]:


# Find the State / UT which has max number of Trucks
truck = df[['States/Uts (Col. 2)','Transport - Multi-Axled/ Articulated Vehicles/ Trucks and Lorries (Col. 3)']]
truck = truck.set_index('States/Uts (Col. 2)')
truck = truck.drop(['GRAND TOTAL','TOTAL STATES','TOTAL Uts'])
truck = truck.sort_values('Transport - Multi-Axled/ Articulated Vehicles/ Trucks and Lorries (Col. 3)', ascending = False)
truck.head(1)


# In[82]:


# Visualizations:
# Draw pie chart to show the percentages and number of different types of vehicles in the given state.

def perc(state):
    
    plt.figure(figsize=(20, 15))
    st = df.drop(df.columns[[-1]], axis=1) 
    st = st.set_index('States/Uts (Col. 2)')
    st = st.loc[state]
    st = pd.DataFrame({'category':st.index, 'numbers':st.values})
    st = st.drop([0])
    st_data = list(st.numbers)
    st_names = list(st.category)
    plt.pie(st_data, labels = st_names, autopct= '%1.1f%%')
    
    plt.show()
    
s=input("Enter state:")
perc(s)
    



# In[129]:


# Draw stacked bar chart for top 5 states which has max number of vehicles.
top_5 = gt.head(5)
top_5.iloc[:,2:7]
top_5['total-transport'] = np.sum(top_5.iloc[:,2:7], axis = 1)
#top_5['total-Non-transport'] = np.sum(top_5.iloc[:,7:15],axis = 1)
top_5 = top_5.iloc[:,[0,-1,-3]]
top_5
data1= list(top_5['total-transport'])
data2 = list(top_5['Non-Transport - Total Non Transport (Col. 16)'])
names = list(top_5['States/Uts (Col. 2)'])
r = [0,1,2,3,4]
barWidth = 0.75
plt.bar(r, data1, color='red', edgecolor='white', width=barWidth, label = 'Total Transport')
plt.bar(r, data2, bottom=data1, color='blue', edgecolor='white', width=barWidth, label = 'Total Non-Transport')

plt.xticks(r, names, fontweight='bold')
plt.xlabel("States")
#???
plt.legend()
plt.show()


# In[97]:


#PIE for top 5 states which has max number of vehicles.
data = list(top_5.grand_total)
labels = list(top_5['States/Uts (Col. 2)'])
colors = ['red','blue','green','yellow','black']
explode = (0.1,0,0,0,0)
plt.pie(data, labels = labels, explode = explode, shadow = True, colors = colors, autopct = '%1.1f%%' )
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




