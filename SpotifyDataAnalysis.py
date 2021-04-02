#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[28]:


songs=pd.read_csv("D:\Data\spotifytoptracks.csv")
songs.head(5)


# In[55]:


#bins used for x axis points  
bins = [80,90,100,110,120,130,140,150]

#creates plots for histogram using the bins assigned above, and rwidth spaces them out to make
#it more visable 
plt.hist(songs.tempo, bins=bins, rwidth=0.9)

#labels for y,x,and title
plt.ylabel('Number of songs')
plt.xlabel('Tempo')
plt.title('Distribution of Tempo in Songs on Spotify')

#shows histogram
plt.show()


# In[26]:


#creates scatter plot for loudness and acousticness
songs.plot.scatter(x = 'loudness', y = 'acousticness')

#labels for y,x,and title
plt.ylabel('Acousticness of the song')
plt.xlabel('Loudness of the song')
plt.title('Loudness compared to Acousticness of Top 50 Spotify song')

#shows scatter plot
plt.show()


# In[ ]:





# In[50]:


#Creates line chart of duration of songs 
plt.plot(songs.duration_ms)

#labels for y,x,and title
plt.ylabel('Duration of Song in Milliseconds')
plt.xlabel('Tracks in Top 50 Order')
plt.title('Song Length Compared to Song Ranking')

#shows line graph
plt.show()


# In[56]:


#plots song energy on a line chart 
plt.plot(songs.energy)

#plots song danceability on a line chart 
plt.plot(songs.danceability)

#labels for y,x,and title
plt.ylabel('Energy and Danceability Score')
plt.xlabel('Tracks in Top 50 Order')
plt.title('Energy vs Danceablitiy of the Top 50 Spotify Songs')

#shows line graph
plt.show()


# In[ ]:




