#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np


# In[3]:


url = 'https://www.ufc.com/events#events-list-past'
df = pd.DataFrame()


# In[8]:


arr_links = []
for i in range(0,81):
    url = 'https://www.ufc.com/events?page='+str(i)
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    data = soup.find_all('h3', class_= 'c-card-event--result__headline')
    for item in data:
        url2 = 'https://www.ufc.com'+str(item).split('"',4)[3]
        response = requests.get(url2)
        soup2 = bs(response.text, 'html.parser')
        data_3 = soup2.find_all('div', class_= 'c-listing-fight')
        data_2 = soup2.find_all('div', class_ = 'c-listing-ticker--footer')
        for item2 in data_3:         
            arr_links.append('https://www.ufc.com/matchup/'+str(data_2).split('"')[3]+'/'+str(item2).split('"')[3]+'/post')
            print('https://www.ufc.com/matchup/'+str(data_2).split('"')[3]+'/'+str(item2).split('"')[3]+'/post')


# In[12]:


df2 = pd.DataFrame(arr_links)
df2.to_excel('C:/Users/hites/OneDrive/Desktop/UFCframelinks.xlsx')


# In[13]:


i=0
df = pd.DataFrame(columns=['red_total_strikes', 'red_total_takedowns', 'red_total_sub_attampts', 'red_total_rev', 'red_total_sig_strikes', 'red_total_knockdowns', 'blue_total_strikes', 'blue_total_takedowns', 'blue_total_sub_attampts', 'blue_total_rev', 'blue_total_sig_strikes', 'blue_total_knockdowns','winner'])
for url in arr_links:
    try:
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        temp = soup.find_all('span', class_ = 'c-stat-metric-compare__value c-stat-metric-compare__number')
        temp1 = soup.find_all('span', class_ = 'c-stat-metric-compare__value_2 c-stat-metric-compare__number')
        temp2 = str(soup.find('div', class_ = 'fighter-names__winner fighter-names__winner--show').parent).split('"')[1]
        df.loc[i,'red_total_strikes'] = temp[0].text
        df.loc[i,'red_total_takedowns'] = temp[1].text
        df.loc[i,'red_total_sub_attampts'] = temp[2].text
        df.loc[i,'red_total_rev'] = temp[3].text
        df.loc[i,'red_total_sig_strikes'] = temp[4].text
        df.loc[i,'red_total_knockdowns'] = temp[5].text      
        df.loc[i,'blue_total_strikes'] = temp1[0].text
        df.loc[i,'blue_total_takedowns'] = temp1[1].text
        df.loc[i,'blue_total_sub_attampts'] = temp1[2].text
        df.loc[i,'blue_total_rev'] = temp1[3].text
        df.loc[i,'blue_total_sig_strikes'] = temp1[4].text
        df.loc[i,'blue_total_knockdowns'] = temp1[5].text  
        fighter_name_1 = str(soup.find('a', class_ = 'left')).split('/')[2].split('"')[0]
        fighter_name_2 = str(soup.find('a', class_ = 'right')).split('/')[2].split('"')[0]
        df.loc[i,'red_vs_blue'] = fighter_name_1 + ' vs ' + fighter_name_2
        if temp2 == 'right':
            df.loc[i,'winner'] = 'blue'
        elif temp2 == 'left':
            df.loc[i,'winner'] = 'red'
        print(df)
        i+=1 
    except:
        i+=1
        pass


# In[15]:


df.to_excel('C:/Users/hites/OneDrive/Desktop/UFCData.xlsx')
