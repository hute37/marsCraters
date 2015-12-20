# Craters on Mars

## 1. Load packages.
import pandas as pd
import numpy as np


## 2. Import data.
data=pd.read_csv("marscrater_pds.csv", low_memory=False)

### Bug fix for display formats. 
pd.set_option('display.float_format', lambda x:'%f'%x)

### Convert relevant data to numeric values. 
data['DIAM_CIRCLE_IMAGE']=pd.to_numeric(data['DIAM_CIRCLE_IMAGE'])
data['DEPTH_RIMFLOOR_TOPOG']=pd.to_numeric(data['DEPTH_RIMFLOOR_TOPOG'])
data['NUMBER_LAYERS']=pd.to_numeric(data['NUMBER_LAYERS'])

### Force Spyder to display full results.
#pd.set_option('display.max_rows', None)


## 3. Summarize data.

### Basic information.
print('Number of observations: ', len(data)) 
print('Number of variables: ', len(data.columns))

### Handle missing answers.  No used in this code, but kept "just in case.."
#data['MORPHOLOGY_EJECTA_1']=data['MORPHOLOGY_EJECTA_1'].replace(" ", np.nan) 
#data['MORPHOLOGY_EJECTA_2']=data['MORPHOLOGY_EJECTA_2'].replace(" ", np.nan) 
#data['MORPHOLOGY_EJECTA_3']=data['MORPHOLOGY_EJECTA_3'].replace(" ", np.nan) 

### Distributions.

#### Diameter.
#diam_c=data['DIAM_CIRCLE_IMAGE'].value_counts().sort_index()
#print('Crater Diameter, Frequency Count: ')
#print(diam_c)

#diam_p=data['DIAM_CIRCLE_IMAGE'].value_counts(dropna = False, normalize = True).sort_index() 
#print('Crater Diameter, Frequency Percent: ')
#print(diam_p)
#print('Crater Diameter, Number of Unique Values: ', len(diam_c))

#### Depth.
depC=data['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
print('Crater Depth, Frequency Count: ')
print(depC)

depP=data['DEPTH_RIMFLOOR_TOPOG'].value_counts(dropna = False, normalize = True).sort_index()
print('Crater Depth, Frequency Percent: ')
print(depP)
print('Crater Depth, Number of Unique Values: ', len(depC))

#### Ejecta Morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Crater Ejecta Morphology 1 Classification, Frequency Count: ')
print(me1C)

me1P=data.groupby('MORPHOLOGY_EJECTA_1').size()*100/me1C.sum()
print('Crater Ejecta Morphology 1 Classification, Frequency Percent: ')
print(me1P)
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(me1C))

#me2_c=data['MORPHOLOGY_EJECTA_2'].value_counts().sort_index() 
#print('Crater Ejecta Morphology 2 Classification, Frequency Count: ')
#print(me2_c)

#me2_p=data.groupby('MORPHOLOGY_EJECTA_2').size()*100/me2_c.sum()
#print('Crater Ejecta Morphology 2 Classification, Frequency Percent: ')
#print(me2_p)
#print('Ejecta Morphology 2 Classification, Number of Unique Values: ', len(me2_c))

#me3_c=data['MORPHOLOGY_EJECTA_3'].value_counts().sort_index() 
#print('Crater Ejecta Morphology 3 Classification, Frequency Count: ')
#print(me3_c)

#me3_p=data.groupby('MORPHOLOGY_EJECTA_3').size()*100/me3_c.sum()
#print('Crater Ejecta Morphology 3 Classification, Frequency Percent: ')
#print(me3_p)
#print('Ejecta Morphology 3 Classification, Number of Unique Values: ', len(me3_c))

#### Layers, using alternate 'bygroup' call.
#lay_c=data.groupby('NUMBER_LAYERS').size()
#print('Crater Layers, Frequency Count: ')
#print(lay_c)

#lay_p=data.groupby('NUMBER_LAYERS').size()*100/len(data)
#print('Crater Layers, Frequency Percent: ')
#print(lay_p)
#print('Crater Layers, Number of Unique Values: ', len(lay_c))

### Subset data and refine search.

#### Only craters with non-empty MORPHOLOGY_EJECTA_1.
subme1=data[data['MORPHOLOGY_EJECTA_1']!=" "]
print('Number of Observations with non-empty Ejecta Morphology', len(subme1))

subme1_depC=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts(sort=False).sort_index()
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth, Frequency Count: ')
print(subme1_depC)

subme1_depP=subme1['DEPTH_RIMFLOOR_TOPOG'].value_counts(sort=False, normalize=True)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth, Frequency Percent: ')
print(subme1_depP)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Depth, Number of Unique Values: ', len(subme1_depC))

subme1_me1C=subme1['MORPHOLOGY_EJECTA_1'].value_counts()
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Ejecta Morphology 1 Classification, Sorted Frequency Count: ')
print(subme1_me1C)

subme1_me1P=subme1['MORPHOLOGY_EJECTA_1'].value_counts(normalize=True)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Crater Ejecta Morphology 1 Classification, Sorted Frequency Percent: ')
print(subme1_me1P)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme1_me1C))

#### Aggregate along lattitude.
subme1_latC=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=72)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Lattitude, Aggregated Frequency Count: ')
print(subme1_latC)

subme1_lat_p=subme1['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=72)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Lattitude, Aggregated Frequency Percent: ')
print(subme1_lat_p)

#### Aggregate along longitude.
subme1_lon_c=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, bins=72)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Longitude, Aggregated Frequency Count: ')
print(subme1_lon_c)

subme1_lon_p=subme1['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=False, normalize=True, bins=72)
print('Subset, Non-Empty MORPHOLOGY_EJECTA_1')
print('Longitude, Aggregated Frequency Percent: ')
print(subme1_lon_p)
