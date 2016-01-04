# Craters on Mars

## 1. Load packages.
import pandas as pd
import numpy as np
import decimal
import seaborn
import matplotlib.pyplot as plt


## 2. Import and set-up data.
data=pd.read_csv("marscrater_pds.csv", low_memory=False)

### Bug fix for display formats. 
pd.set_option('display.float_format', lambda x:'%f'%x)

### Convert relevant data to numeric values. 
data['DIAM_CIRCLE_IMAGE']=pd.to_numeric(data['DIAM_CIRCLE_IMAGE'])
data['DEPTH_RIMFLOOR_TOPOG']=pd.to_numeric(data['DEPTH_RIMFLOOR_TOPOG'])
data['NUMBER_LAYERS']=pd.to_numeric(data['NUMBER_LAYERS'])

### Force Spyder to display full results.
pd.set_option('display.max_rows', None)


## 3. Summarize data.

### Basic information.
print('Original data set.')
print('Number of observations: ', len(data)) 
print('Number of variables: ', len(data.columns))
print()

### Distributions.

#### Depth.
depC=data['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
#print('Crater Depth, Frequency Count: ')
#print(depC)
depP=data['DEPTH_RIMFLOOR_TOPOG'].value_counts(dropna = False, normalize = True).sort_index()
#print('Crater Depth, Frequency Percent: ')
#print(depP)
print('Crater Depth, Number of Unique Values: ', len(depC))
print()

#### Ejecta Morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
#print('Crater Ejecta Morphology 1 Classification, Frequency Count: ')
#print(me1C)
me1P=data.groupby('MORPHOLOGY_EJECTA_1').size()*100/me1C.sum()
#print('Crater Ejecta Morphology 1 Classification, Frequency Percent: ')
#print(me1P)
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(me1C))
print()

### Subset data and refine search.

#### Only craters with non-empty MORPHOLOGY_EJECTA_1.
subme1=data[data['MORPHOLOGY_EJECTA_1']!=" "]
print('Number of Observations with non-empty Ejecta Morphology', len(subme1))
print()

subme1_depC=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts(sort=False).sort_index()
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Crater Depth, Frequency Count: ')
#print(subme1_depC)
subme1_depP=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts(sort=False, normalize=True)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Crater Depth, Frequency Percent: ')
#print(subme1_depP)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth, Number of Unique Values: ', len(subme1_depC))
print()

subme1_me1C=subme1['MORPHOLOGY_EJECTA_1'].value_counts()
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Crater Ejecta Morphology 1 Classification, Sorted Frequency Count: ')
#print(subme1_me1C)
subme1_me1P=subme1['MORPHOLOGY_EJECTA_1'].value_counts(normalize=True)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Crater Ejecta Morphology 1 Classification, Sorted Frequency Percent: ')
#print(subme1_me1P)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme1_me1C))
print()

#### Aggregate along lattitude.
subme1_latC=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Latitude, Aggregated Frequency Count: ')
#print(subme1_latC)
#subme1_lat_p=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Latitude, Aggregated Frequency Percent: ')
#print(subme1_lat_p)

#### Aggregate along longitude.
#subme1_lon_c=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Longitude, Aggregated Frequency Count: ')
#print(subme1_lon_c)
#subme1_lon_p=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Longitude, Aggregated Frequency Percent: ')
#print(subme1_lon_p)


## 4. Data management.

### Remove MORPHOLOGY_EJECTA_1='Rd' (approximately 60% of the non-empty sample).
subme2=subme1[subme1['MORPHOLOGY_EJECTA_1']!="Rd"]
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Number of Observations: ', len(subme2))
print()

### Collapse morphology catagories to first entry before the first '/'.
subme2['MORPHOLOGY_EJECTA_1']=subme2['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)

subme2_me1C=subme2['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Ejecta Morphology 1 Classification, Frequency Count')
print(subme2_me1C)
print()
subme2_me1P=subme2['MORPHOLOGY_EJECTA_1'].value_counts(dropna = False, normalize = True).sort_index()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Ejecta Morphology 1 Classification, Frequency Percent')
print(subme2_me1P)
#print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme2_me1C))
print()

### Group craters by depth, round to nearest 1/10th of kilometer. 
subme2['DEPTH_RIMFLOOR_TOPOG']=np.around(subme2['DEPTH_RIMFLOOR_TOPOG'], decimals=1)

subme2_depC=subme2['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Crater Depth Rounded to Nearest 1/10th')
print('Crater Depth, Frequency Count: ')
print(subme2_depC)
print()
subme2_depP=subme2['DEPTH_RIMFLOOR_TOPOG'].value_counts(dropna = False, normalize = True).sort_index()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Crater Depth Rounded to Nearest 1/10th')
print('Crater Depth, Frequency Percent: ')
print(subme2_depP)
#print('Crater Depth, Number of Unique Values: ', len(subme2_depC))
print()

#### Aggregate along lattitude.
subme2_latC=subme2['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Latitude, Aggregated Frequency Count: ')
print(subme2_latC)
print()
subme2_lat_p=subme2['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Latitude, Aggregated Frequency Percent: ')
print(subme2_lat_p)
print()

#### Aggregate along longitude.
#subme2_lon_c=subme2['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
#print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
#print('Longitude, Aggregated Frequency Count: ')
#print(subme2_lon_c)
#subme2_lon_p=subme2['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
#print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
#print('Longitude, Aggregated Frequency Percent: ')
#print(subme2_lon_p)

### Summary, subsetted & data managed.
print('Summary, Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Aggregated non-empty Ejecta Morphology != Rd, Number of Unique Values: ', len(subme2_me1C))
print('Crater Depth Rounded, Number of Unique Values: ', len(subme2_depC))
print()


## 5. Graphing data, univariate analysis. 

### Aggregated ejecta morphology.
subme2['MORPHOLOGY_EJECTA_1']=subme2['MORPHOLOGY_EJECTA_1'].astype('category')
seaborn.countplot(y='MORPHOLOGY_EJECTA_1', data=subme2)
plt.xlabel('Count')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Ejecta Morphology Classification')
print()

### Rounded crater depth.
seaborn.distplot(subme2['DEPTH_RIMFLOOR_TOPOG'].dropna(), kde=False)
plt.xlabel('Mars Craters Crater Depth, Rounded to nerest 1/10th')
plt.title('Histogram')
print()

### Latitude.
seaborn.kdeplot(subme2['LATITUDE_CIRCLE_IMAGE'], shade=True)
plt.xlabel('Mars Craters Latitude')
plt.title('Density Plot')
print()


## 6. Graphing data, bivariate analysis.

### Aggregated ejecta morphology and crater depth.
subme2['MORPHOLOGY_EJECTA_1']=subme2['MORPHOLOGY_EJECTA_1'].astype('category')
seaborn.boxplot(x='DEPTH_RIMFLOOR_TOPOG', y='MORPHOLOGY_EJECTA_1', data=subme2)
plt.xlabel('Crater Depth')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Crater Depth by Ejecta Morphology Classification')
print()

### Aggregated ejecta morphologyh and latitude.
seaborn.boxplot(x='LATITUDE_CIRCLE_IMAGE', y='MORPHOLOGY_EJECTA_1', data=subme2)
plt.xlabel('Latitude')
plt.ylabel('Ejecta Morphology')
plt.title('Latitude by Ejecta Morphology Classification')
print()

### Crater depth and latitude.
seaborn.jointplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG', data=subme2)
print()

### Crater depth and latitude.
seaborn.heatmap(x='LONGITUDE_CIRCLE_IMAGE', y='LATITUDE_CIRCLE_IMAGE', data=subme2)
print()