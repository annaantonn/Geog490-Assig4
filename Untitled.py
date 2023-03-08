#!/usr/bin/env python
# coding: utf-8

# In[84]:


# Import libraries
import numpy as np
import rasterio
import pandas as pd
import matplotlib.pyplot as plt


# In[85]:


src = rasterio.open('data/nlcd_2001_phoenix.tif')
src


# In[86]:


print(f"Number of bands: {src.count}")
print(f"Width: {src.width}")
print(f"Height: {src.height}")
print(f"Data type: {src.dtypes}")


# In[87]:


src.transform


# In[88]:


src.bounds


# In[89]:


nlcd_2001_phoenix= src.read(1)
nlcd_2001_phoenix


# In[90]:


fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(nlcd_2001_phoenix, cmap='tab20b')
ax.set_title("Title", fontsize=14)


# In[91]:


unique, counts = np.unique(nlcd_2001_phoenix, return_counts=True)
dict(zip(unique, counts))


# In[92]:


# Count number of land pixels
land_pixels = nlcd_2001_phoenix.size

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# In[93]:


open_water = df_2001[df_2001['lc'] == 11]


# In[94]:


open_water


# In[95]:


open_water['count_2001'][0]


# In[96]:


developed_openspace = df_2001[df_2001['lc'] == 21]
developed_openspace


# In[97]:


developed_openspace


# In[98]:


open_space_value = developed_openspace['count_2001'][1]
open_space_value


# In[99]:


developed_low = df_2001[df_2001['lc'] == 22]
developed_low


# In[100]:


low_value = developed_low['count_2001'][2]
low_value


# In[101]:


developed_med_intensity = df_2001[df_2001['lc'] == 23]
developed_med_intensity


# In[102]:


med_value = developed_med_intensity['count_2001'][3]
med_value


# In[103]:


developed_high_intensity = df_2001[df_2001['lc'] == 24]
developed_high_intensity


# In[104]:


high_value = developed_high_intensity['count_2001'][4]
high_value


# In[105]:


developed_grid_cells = open_space_value + low_value + med_value + high_value
developed_grid_cells


# In[106]:


cultivated_crop = df_2001[df_2001['lc'] == 82]
cultivated_crop


# In[107]:


cultivated_crop['count_2001']


# In[108]:


df_2001


# In[109]:


df_2001['count_2001'].sum()


# In[110]:


nlcd_2001_phoenix[nlcd_2001_phoenix == 21] = 22


# In[111]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2001_phoenix, return_counts=True)

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# In[112]:


nlcd_2001_phoenix[nlcd_2001_phoenix == 22] = 23


# In[113]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2001_phoenix, return_counts=True)

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# In[114]:


nlcd_2001_phoenix[nlcd_2001_phoenix == 23] = 24


# In[115]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2001_phoenix, return_counts=True)

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# In[116]:


developed_perc = df_2001[df_2001['lc'] == 24]


# In[117]:


developed_perc['fraction_2001'][1]


# In[118]:


openwater_perc = df_2001[df_2001['lc'] == 11]


# In[119]:


openwater_perc


# In[120]:


openwater_perc['fraction_2001'][0]


# In[121]:


most_common_perc = df_2001['fraction_2001'].max()
most_common_perc


# In[122]:


most_com_class = df_2001[df_2001['fraction_2001'] == most_common_perc]


# In[123]:


most_com_class


# In[124]:


most_com_class['lc'][5]


# In[125]:


abc = rasterio.open('data/nlcd_2019_phoenix.tif')
abc


# In[126]:


print(f"Number of bands: {abc.count}")
print(f"Width: {abc.width}")
print(f"Height: {abc.height}")
print(f"Data type: {abc.dtypes}")


# In[127]:


nlcd_2019 = abc.read(1)
nlcd_2019


# In[128]:


unique, counts = np.unique(nlcd_2019, return_counts=True)
dict(zip(unique, counts))


# In[129]:


# Count number of land pixels
land_pixels = nlcd_2019.size

# Convert to DataFrame
df_2019 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2019', 'fraction_2019'])
df_2019


# In[130]:


df_2019['count_2019'].sum()


# In[131]:


nlcd_2019[nlcd_2019 == 21] = 22


# In[132]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2019, return_counts=True)

# Convert to DataFrame
df_2019 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2019', 'fraction_2019'])
df_2019


# In[133]:


nlcd_2019[nlcd_2019 == 22] = 23


# In[134]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2019, return_counts=True)

# Convert to DataFrame
df_2019 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2019', 'fraction_2019'])
df_2019


# In[164]:


nlcd_2019[nlcd_2019 == 23] = 24


# In[165]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2019, return_counts=True)

# Convert to DataFrame
df_2019 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2019', 'fraction_2019'])
df_2019


# In[166]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2001_phoenix, return_counts=True)

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# In[167]:


df_2001


# In[168]:


df = pd.merge(df_2001, df_2019, on=['lc'])
df


# In[169]:


df['change'] = (df['count_2019'] - df['count_2001'])
df['change_percent'] = (((df['count_2019'] - df['count_2001']) / df['count_2001']) * 100)
df


# In[170]:


dev_land_change = (df[df['lc'] == 24])


# In[171]:


dev_land_change


# In[172]:


dev_land_change['change_percent']


# In[173]:


cult_crop_change = (df[df['lc'] == 82])


# In[174]:


cult_crop_change


# In[175]:


cult_crop_change['change_percent']


# In[186]:


mask = nlcd_2019[nlcd_2001 == 24]
unique, counts = np.unique(mask, return_counts=True)
change_df = pd.DataFrame(list(zip(unique, counts, (counts/mask.shape[0])*100)),
                 columns=['lc', 'count', 'fraction'])
change_df


# In[188]:


fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(df.astype(int), cmap='Blues')
ax.set_title("Landcover Change between 2001 and 2016", fontsize=14)


# In[ ]:




