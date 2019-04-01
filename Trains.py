#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Trains
# 1.	List all train names which terminates at  “ BANGALORE CANT”
# 2.	List all the Source stations which has train facility to “ BANGALORE CANT”
# 3.	Given a train number, list all the station names that train passes through before reaching destination station.
# 4.	Give the train details (Train number, source and destination station , distance in KMs) which covers longest distance.
# 5.	Give the train details (Train number, source and destination station , distance in KMs) which takes longer time to reach destination.
# 6.	List the station which has more number of train connectivity.
# Visualization:
# Draw bar chart to show the total number of trains starting from Mumbai, Bangalore, Delhi, Chennai and Kolkota. Station codes of Mumbai are ( CSTM, BCT, LTT, BDTS, PNVL), Bangalore (SBC, YPR, BNC), Delhi (DEC, DEE, DLI, DAZ, DSA, NDLS, DSJ, DKJ), Chennai (MPK, MS, MSB, MSC, MAS) and Kolkota is (KOAA, CP, HWH, SDAH)
# Draw pie chart for Delhi and Bangalore showing %age of trains handled ( Originating and Destination) by each stations in the given city.


# In[44]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[192]:


df = pd.read_csv('trains.csv')
df.head(5)


# In[84]:




#List all train names which terminates at  “ BANGALORE CANT”


#bc = bc.loc['BANGALORE CANT ']
#bc = df[df['Destination Station Name'] == 'BANGALORE CANT ']
# bc = bc.groupby('Destination Station Name').agg({'Destination Station Name':'unique'})

bc = df[df['Destination Station Name'] == 'BANGALORE CANT ']
bc = bc['train Name']
bc.unique()


# In[91]:


#List all the Source stations which has train facility to “ BANGALORE CANT”

bs = df['source Station Name'][df['Destination Station Name'] == 'BANGALORE CANT '].unique()

bs


# In[120]:


#Given a train number, list all the station names that train passes through before reaching destination station.

t_no = df.groupby(['Train No.']).agg({'Station Name':'unique'})
t_no = t_no.reset_index()
# t_no['\'00851\'']
t_no = t_no[t_no['Train No.'] == '\'00851\'']
list(t_no['Station Name'])


# In[134]:


#Give the train details (Train number, source and destination station , distance in KMs) which covers longest distance

#MAX
lt =df.groupby(['Train No.','source Station Name','Destination Station Name']).agg({'Distance':'max'})
lt = lt.reset_index()
lt.head(1)

#SUM
# lt =df.groupby(['Train No.','source Station Name','Destination Station Name']).agg({'Distance':'sum'})
# lt = lt.reset_index()
# lt.sort_values('Distance', ascending = False)
# lt.head(1)


# In[135]:


#Give the train details (Train number, source and destination station , distance in KMs) 
#which takes longer time to reach destination.



# In[198]:


#List the station which has more number of train connectivity.
df1 = df['Station Name'].value_counts()
df1 = df1.to_frame(name = 'total')

df1[df1['total']==df1['total'].max()]

# df1 = df['source Station Name  '].groupby('Station Name').agg({'Station Name':'count'})
# #df1 = df1.reset_index()
# #df1.sort_values('Station Name', ascending = False)
# df1


# In[259]:


# Draw bar chart to show the total number of trains starting from Mumbai, Bangalore, Delhi, Chennai and Kolkota. 
# Station codes of Mumbai are ( CSTM, BCT, LTT, BDTS, PNVL), 
# Bangalore (SBC, YPR, BNC), 
# Delhi (DEC, DEE, DLI, DAZ, DSA, NDLS, DSJ, DKJ), 
# Chennai (MPK, MS, MSB, MSC, MAS) and 
# Kolkata is ('KOAA ':'Kolkata', 'CP ':'Kolkata', 'HWH '::'Kolkata', 'SDAH ':'Kolkata')


list_city = {'CSTM ':'Mumbai','BCT ':'Mumbai','LTT ':'Mumbai','BDTS ':'Mumbai','PNVL ':'Mumbai','SBC ':'Bangalore','YPR ':'Bangalore','BNC ':'Bangalore','DEC ':'Delhi', 'DEE ':'Delhi','DLI ':'Delhi', 'DAZ ':'Delhi', 'DSA ':'Delhi', 'NDLS ':'Delhi', 'DSJ ':'Delhi', 'DKJ ':'Delhi','MPK ':'Chennai', 'MS ':'Chennai', 'MSB ':'Chennai', 'MSC ':'Chennai', 'MAS ':'Chennai','KOAA ':'Kolkata', 'CP ':'Kolkata', 'HWH ':'Kolkata', 'SDAH ':'Kolkata'}
df["Train_city"]=df["Source Station Code"].map(list_city)

city = df.dropna()
city5 = city.groupby(['Train_city']).agg({'Train No.':'nunique'})
city5 = city5.reset_index()
#city[city['Train_city']=='Mumbai']
city5


# In[260]:



# names = list(city5.Train_city)
# data = list(city5['Train No.'])
# colors = ['red','blue','green','yellow','orange']
# x_count = np.arange(len(data))

#df.set_index('Train_city')[['Train No.']].plot.bar()


city5.plot.bar(x = 'Train_city', y = ['Train No.'])


# In[ ]:


# Draw pie chart for Delhi and Bangalore showing %age of trains handled ( Originating and Destination) by each stations 
#in the given city.

