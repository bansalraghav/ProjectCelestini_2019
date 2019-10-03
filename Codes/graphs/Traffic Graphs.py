#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# get_ipython().magic(u'matplotlib inline')
# import mpld3
# mpld3.enable_notebook()


# In[ ]:


traffic_data = pd.read_csv('joined.csv').iloc[3:2595]


# In[ ]:


pollution_15 = pd.read_excel('5-13pollution.xlsx').iloc[0:864]
traffic_15 = traffic_data.iloc[traffic_data.index%3 ==0]


# In[ ]:


pollution_15


# In[ ]:


traffic_15


# In[ ]:


removingNaN = traffic_15.fillna(-1)
removingNone = pollution_15.replace('None', -2, regex= True)


# In[ ]:


removingNaN


# In[ ]:


removingNone


# In[ ]:


traffic_currentTime = removingNaN['Current Time(seconds)']
traffic_timestamp = removingNaN['newtimestamp']
pollution_NOx = removingNone['NOx']
y = pollution_NOx


# In[ ]:


# pd.plot(traffic_timestamp, traffic_currentTime)
x = traffic_timestamp
# pd.to_datetime(pollution_NOx)


# In[ ]:

plt.plot(x, y)
plt.plot(x, traffic_currentTime)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




