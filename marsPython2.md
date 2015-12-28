# Craters on Mars

## 1. Load packages.
import pandas as pd
import numpy as np
import decimal

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

### Distributions.

#### Depth.
depC=data['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
#print('Crater Depth, Frequency Count: ')
#print(depC)

depP=data['DEPTH_RIMFLOOR_TOPOG'].value_counts(dropna = False, normalize = True).sort_index()
#print('Crater Depth, Frequency Percent: ')
#print(depP)
print('Crater Depth, Number of Unique Values: ', len(depC))

#### Ejecta Morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
#print('Crater Ejecta Morphology 1 Classification, Frequency Count: ')
#print(me1C)

me1P=data.groupby('MORPHOLOGY_EJECTA_1').size()*100/me1C.sum()
#print('Crater Ejecta Morphology 1 Classification, Frequency Percent: ')
#print(me1P)
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(me1C))

### Subset data and refine search.

#### Only craters with non-empty MORPHOLOGY_EJECTA_1.
subme1=data[data['MORPHOLOGY_EJECTA_1']!=" "]
print('Number of Observations with non-empty Ejecta Morphology', len(subme1))

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

#### Aggregate along lattitude.
subme1_latC=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Latitude, Aggregated Frequency Count: ')
print(subme1_latC)

subme1_lat_p=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Latitude, Aggregated Frequency Percent: ')
print(subme1_lat_p)

#### Aggregate along longitude.
subme1_lon_c=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Longitude, Aggregated Frequency Count: ')
#print(subme1_lon_c)

subme1_lon_p=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=36)
#print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
#print('Longitude, Aggregated Frequency Percent: ')
#print(subme1_lon_p)


## 4. Data management.

### Group craters by depth, round to nearest 1/10th of kilometer. 
subme1['DEPTH_RIMFLOOR_TOPOG']=np.around(subme1['DEPTH_RIMFLOOR_TOPOG'], decimals=1)

subme1_depC=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth Rounded to Nearest 1/10th')
print('Crater Depth, Frequency Count: ')
print(subme1_depC)

subme1_depP=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts(dropna = False, normalize = True).sort_index()
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth Rounded to Nearest 1/10th')
print('Crater Depth, Frequency Percent: ')
print(subme1_depP)
#print('Crater Depth, Number of Unique Values: ', len(subme1_depC))

### Collapse morphology catagories to first entry before the first '/'.
subme1['MORPHOLOGY_EJECTA_1']=subme1['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)

subme1_me1C=subme1['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Subset, Aggregated Non-Empty MORPHOLOGY_EJECTA_1')
print('Ejecta Morphology 1 Classification, Frequency Count')
print(subme1_me1C)

subme1_me1P=subme1['MORPHOLOGY_EJECTA_1'].value_counts(dropna = False, normalize = True).sort_index()
print('Subset, Aggregated Non-Empty MORPHOLOGY_EJECTA_1')
print('Ejecta Morphology 1 Classification, Frequency Percent')
print(subme1_me1P)
#print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme1_me1C))

#### Summary, subsetted & data managed.
print('Summary, Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth Rounded, Number of Unique Values: ', len(subme1_depC))
print('Ejecta Morphology 1 Classification Aggregated, Number of Unique Values: ', len(subme1_me1C))