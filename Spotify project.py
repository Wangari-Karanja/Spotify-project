#!/usr/bin/env python
# coding: utf-8

# In[5]:


artist_df = pd.read_csv("C:/Users/HP/Documents/Simplilearn projects/artists.csv")
artist_df.head(5)


# In[6]:


artist_df.info()


# In[7]:


artist_df.describe()


# In[8]:


# Check for duplicates
print(artist_df.isnull().sum())


# In[10]:


# Clear duplicates
artist_df = artist_df.dropna()
artist_df.isnull().sum()


# In[11]:


artist_df.head()


# In[13]:


#Remove unnecessary columns
artist_df.drop(["id","genres"], inplace = True, axis=1)
artist_df.head()


# In[53]:


features_df = pd.read_csv("C:/Users/HP/Documents/Simplilearn projects/SpotifyFeatures.csv")
features_df.head(2)


# In[54]:


features_df.info()


# In[33]:





# In[35]:


features_df.head(2)


# In[36]:


#Find null values
print(features_df.isnull().sum())


# In[37]:


# Find duplicates

duplicated_artist_df = artist_df[artist_df.duplicated()]
print("Number of duplicates", duplicated_artist_df)


# In[39]:


artist_df.count()


# In[40]:


artist_df = artist_df.drop_duplicates()
artist_df.count()


# In[45]:


# Artists with the top followers
most_followers = artist_df.groupby(by = 'name').max()[['followers']].sort_values(by = ['followers'], ascending = False).reset_index()
fig = plt.figure(figsize = (15,5))
plt.title("Most followed artists", size = 15)
ax = sns.barplot(data = most_followers.iloc[:10], y= 'followers', x = 'name',linewidth = 2, edgecolor='green')

plt.xlabel("Artist")
plt.ylabel("Followers")
plt.show()


# In[51]:


# Most Popular artists
most_popular_artists = artist_df.groupby(by = 'name').max()[['popularity']].sort_values(by=['popularity'],ascending = False).reset_index()
fig = plt.figure(figsize=(14,5))
plt.title("Most Popular Artists")
ax = sns.barplot(data = most_popular_artists.iloc[:10], y = 'popularity', x = 'name', linewidth=2, edgecolor='pink')

plt.xlabel("Artist")
plt.ylabel("Popularity")
plt.show()


# In[58]:


# Least popular song
sorted_df = features_df.sort_values("popularity", ascending=True).head(10)
sorted_df


# In[60]:


features_df.describe().transpose()


# In[61]:


# Most Popular songs
most_popular_songs = features_df.sort_values("popularity",ascending=False).head(10)
most_popular_songs


# In[62]:


# Songs above 90%

most_popular_songs = features_df.query('popularity > 90', inplace = False).sort_values("popularity", ascending = False)
most_popular_songs[:10]


# In[66]:


features_df["duration"] = features_df["duration_ms"].apply(lambda x: round(x/1000))
features_df.drop("duration_ms", inplace = True, axis =1)


# In[68]:


features_df.duration.head


# In[69]:


corr_df = features_df.drop(["key","mode"], axis=1).corr(method="pearson")
fig = plt.figure(figsize=(14,6))
heatmap = sns.heatmap(corr_df,annot=True,fmt=".1g", vmin=-1,vmax=1,center=0,cmap="inferno",linewidth=2)
heatmap.set_title("Correlation HeatMap Between Variables")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)


# In[70]:


sample_df = features_df.sample(int(0.004 * len(features_df)))


# In[71]:


print(len(sample_df))


# In[72]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_df, y = "loudness", x = "energy",color = "c").set(title= "Loudness Vs Energy Correlation")


# In[76]:


plt.figure(figsize=(9,5))
sns.regplot(data=features_df, x = "acousticness", y = "popularity", color = "c").set(title = "Acoustiness vs Popularity")


# In[77]:


plt.figure(figsize=(9,5))
sns.regplot(data = features_df, x = "danceability", y = "popularity", color = "c").set(title = "Popularity Vs Danceability")


# In[78]:


features_df.head(5)


# In[83]:


sns.color_palette("rocket", as_cmap=True)
ax = sns.barplot(data = features_df, y = "genre", x = "duration")
plt.title("Duration of the Songs in Different Genres")
plt.ylabel("Genre")
plt.xlabel("Duration")
plt.show()


# In[88]:


# Most Popular Genres
most_popular_genres = features_df.groupby("genre")["popularity"].sum().to_frame("popularity")
most_popular_genres = most_popular_genres.sort_values("popularity", ascending = False)
most_popular_genres.iloc[:10]


# In[93]:


fig = plt.figure(figsize=(9,5))
sns.color_palette("rocket", as_cmap=True)
ax = sns.barplot(data = most_popular_genres.iloc[:10], x = most_popular_genres.popularity, y = most_popular_genres.index)
plt.title("Most Popular Genres")
plt.xlabel("Popularity")
plt.ylabel("Genres")


# In[ ]:




