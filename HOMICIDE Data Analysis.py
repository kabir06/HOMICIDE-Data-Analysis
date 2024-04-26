#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


# In[2]:


df = pd.read_csv('C:/Users/kabir/HOMICIDE/homicide_by_countries.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.isnull().sum()


# In[6]:


df.dtypes


# In[7]:


df['Rate']=df['Rate'].astype(int)


# In[8]:


df.dtypes


# In[9]:


my_list = ['Rate', 'Count','Year']
for i in my_list:
    print(i)
    df[i]=df[i].astype(int)


# In[10]:


df.dtypes


# ### Replace Americas with N/A America. To make it permanent 'inplace = True'

# In[11]:


df['Region'].replace('Americas','N/S America', inplace = True)


# In[12]:


df1 = df.sort_values('Count', ascending = False).reset_index(drop = True)


# In[13]:


df1


# In[14]:


df1 = df[['Location', 'Count']].sort_values(by ='Count', ascending = False).head(5)
df1


# In[15]:


df1.plot(x= 'Location',y= 'Count')


# In[16]:


df1.plot(x= 'Location',y= 'Count',kind = 'pie')


# In[ ]:





# In[17]:


df1.plot(x= 'Location',y= 'Count',kind = 'pie' , labels = df1.Location)


# In[18]:


df1.plot(x= 'Location',y= 'Count',kind = 'pie' , labels = df1.Location)
plt.legend().set_visible(False)


# In[19]:


df1.plot(x= 'Location',y= 'Count',kind = 'pie' , labels = df1.Location, autopct ='%1.2f%%')
plt.legend().set_visible(False)


# We can do this in diffrent way.
# 

# In[20]:


df1 = df[['Location', 'Count']].sort_values(by ='Count', ascending = False).head(5)
df1['Perc']= (df1['Count']*100/df1['Count'].sum()).round(2)
df1


# In[21]:


#df1.plot(x= 'Location',y= 'Count',kind = 'pie' , labels = df1.Location, df1.Perc )
#plt.legend().set_visible(False)


# In[22]:


df


# ### Group by Region

# In[23]:


df2 = df.groupby('Region')['Count'].sum()
df2


# #### Sort Data

# In[24]:


df2 = df.groupby('Region')['Count'].sum().sort_values(ascending = False)
df2


# In[25]:


df2.plot(kind = 'bar')
#plt.show()


# To get ride off <Axes: xlabel='Region'>
# 

# In[26]:


df2.plot(kind = 'bar')
plt.show()


# In[27]:


df


# In[28]:


df3 = df.groupby('Subregion')['Count'].sum().sort_values(ascending = False)
df3


# In[29]:


df3.index


# In[30]:


df3.values


# In[31]:


sns.barplot(x = df3.index, y= df3.values)


# In[32]:


sns.barplot(x = df3.index, y= df3.values)
plt.xticks(rotation = 'vertical')


# In[33]:


sns.barplot(x = df3.index, y= df3.values)
plt.xticks(rotation = 'vertical')
xlabel = None


# In[34]:


df


# In[35]:


df.Year.value_counts()


# In[36]:


df[df['Region'].isin(['Asia','Europe'])]


# ### Or It can be done as follows

# In[37]:


df4 = df[(df['Region']== 'Asia') |(df['Region']== 'Europe')]
df4


# In[38]:


df4 = df4[df4['Year']>2016][['Region','Year','Count']]


# In[39]:


df4


# In[40]:


df4 = df4.groupby(['Region','Year']).sum()
df4


# In[41]:


df4 = df4.groupby(['Region','Year']).sum()['Count']
df4


# In[42]:


df4.plot(kind = 'line', figsize = (10,6))


# ### It could not plot successfully. Inorder to plotting it need to be unstake

# In[43]:


df_unstacked = df4.unstack(level = 0)
df_unstacked


# In[44]:


df_unstacked.plot(kind = 'line', figsize = (10,6))


# ### To remove float number. year need to be converted to string.

# In[45]:


df_unstacked.index = df_unstacked.index.astype(int).astype(str)


# In[46]:


df_unstacked.plot(kind = 'line', figsize = (10,6))
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Asia and Europe over years')
plt.show()


# In[47]:


df


# In[48]:


df5 = df.groupby(['Year'])['Rate'].sum().sort_values(ascending = False )
df5


# In[49]:


df5.plot( kind = 'bar', figsize = (7,5),color = 'skyblue', edgecolor = 'black')
plt.xlabel('Region, Year')
plt.ylabel('Sum of Rate')
plt.title('Sum of Rate by Region and Year')
plt.show()


# In[50]:


df


# In[51]:


df6 = df[['Year', 'Region','Count']]
df6


# In[52]:


df6 = df6.groupby(['Year', 'Region']).sum().sort_values(by = 'Year', ascending = False)
df6


# In[53]:


df6.plot(kind = 'bar', figsize = (12,6))


# In[54]:


df6.plot(kind = 'bar', figsize = (12,6), colormap = 'viridis')
plt.xlabel('Year, Region')
plt.ylabel('Sum of Count')
plt.title('Sum of Count by Year and Region')
plt.show()


# In[55]:


df.head(2)


# In[56]:


df7 = df.groupby('Subregion')['Count'].mean().sort_values(ascending = False)
df7


# In[57]:


df7.index


# In[58]:


df7.values


# In[59]:


data = {
    'Category':df7.index,
    'Value':df7.values,
    'Info':df7.values
}
df = pd.DataFrame(data)
df


# In[69]:


fig = px.treemap(df, path = ['Category'], values = 'Value', title= 'Treemap')
fig.update_traces(hovertemplate = 'Category:%{label}<br>Value:%{value}')
fig.show()


# In[ ]:





# In[ ]:




