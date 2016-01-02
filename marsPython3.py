# Craters on Mars

## 1. Set-up. 

### Load packages. 
import pandas as pd
import numpy as np
import decimal
import seaborn as sb
import matplotlib.pyplot as plt

### Import data.
data=pd.read_csv("marscrater_pds.csv", low_memory=False)

### Bug fix for display formats. 
pd.set_option('display.float_format', lambda x:'%f'%x)

### Force Spyder to display full results.
pd.set_option('display.max_rows', None)

### Ensure relevant data is in numeric format. 
data['DIAM_CIRCLE_IMAGE']=pd.to_numeric(data['DIAM_CIRCLE_IMAGE'])
data['DEPTH_RIMFLOOR_TOPOG']=pd.to_numeric(data['DEPTH_RIMFLOOR_TOPOG'])
data['LATITUDE_CIRCLE_IMAGE']=pd.to_numeric(data['LATITUDE_CIRCLE_IMAGE'])
data['LONGITUDE_CIRCLE_IMAGE']=pd.to_numeric(data['LONGITUDE_CIRCLE_IMAGE'])
data['NUMBER_LAYERS']=pd.to_numeric(data['NUMBER_LAYERS'])


## 2. Summarize original data.
print('Summary, Original Data.')

### Basic information.
print('Number of observations: ', len(data)) 
print('Number of variables: ', len(data.columns))
#### Depth.
depC=data['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
print('Crater Depth, Number of Unique Values: ', len(depC))
#### Ejecta morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(me1C))
#### Latitiude.
latC=data['LATITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Latitude, Number of Unique Values: ', len(latC))
#### Longitude.
lonC=data['LONGITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Longitude, Number of Unique Values: ', len(lonC))
print()


## 3. Data management.

### Ejecta morphology.
print('Subset, non-empty MORPHOLOGY_EJECTA_1 != Rd')
#### Exlude craters with non-empty MORPHOLOGY_EJECTA_1.
subme=data[data['MORPHOLOGY_EJECTA_1']!=" "]
#### Exlude MORPHOLOGY_EJECTA_1='Rd' (approximately 60% of the non-empty sample).
subme=subme[subme['MORPHOLOGY_EJECTA_1']!="Rd"]
print('Number of observations: ', len(subme))
subme_me1C1=subme['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme_me1C1))
print()
#### Collapse morphology catagories to first entry before the first '/'.
subme['MORPHOLOGY_EJECTA_1']=subme['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)
##### Count. 
subme_me1C2=subme['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Ejecta Morphology 1 Classification, Frequency Count')
print(subme_me1C2)
print()
##### Percent.
subme_me1P2=subme['MORPHOLOGY_EJECTA_1'].value_counts(dropna = False, normalize = True).sort_index()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Ejecta Morphology 1 Classification, Frequency Percent')
print(subme_me1P2)
print()
print('Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Ejecta Morphology 1 Classification, Number of Unique Values: ', len(subme_me1C2))
print()

### Summary, subsetted & data managed.
print('Summary, Subset, Aggregated non-empty Ejecta Morphology != Rd')
print('Number of observations: ', len(subme))
print('Aggregated non-empty Ejecta Morphology != Rd, Number of Unique Values: ', len(subme_me1C2))


## 4. Graphing data, univariate analysis. 

### Aggregated ejecta morphology.
subme['MORPHOLOGY_EJECTA_1']=subme['MORPHOLOGY_EJECTA_1'].astype('category')
sb.countplot(y='MORPHOLOGY_EJECTA_1', data=subme)
plt.xlabel('Count')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Ejecta Morphology Classification')
print()

### Crater depth.
sb.distplot(subme['DEPTH_RIMFLOOR_TOPOG'].dropna(), kde=False)
plt.xlabel('Mars Craters Crater Depth, Rounded to nerest 1/10th')
plt.title('Histogram')
print()

### Latitude.
sb.kdeplot(subme['LATITUDE_CIRCLE_IMAGE'], shade=True)
plt.xlabel('Mars Craters Latitude')
plt.title('Density Plot')
print()


## 5. Graphing data, bivariate analysis.

### Aggregated ejecta morphology and crater depth.
subme['MORPHOLOGY_EJECTA_1']=subme['MORPHOLOGY_EJECTA_1'].astype('category')
sb.boxplot(x='DEPTH_RIMFLOOR_TOPOG', y='MORPHOLOGY_EJECTA_1', data=subme)
plt.xlabel('Crater Depth')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Crater Depth by Ejecta Morphology Classification')
print()

### Aggregated ejecta morphologyh and latitude.
sb.boxplot(x='LATITUDE_CIRCLE_IMAGE', y='MORPHOLOGY_EJECTA_1', data=subme)
plt.xlabel('Latitude')
plt.ylabel('Ejecta Morphology')
plt.title('Latitude by Ejecta Morphology Classification')
print()

### Crater depth and latitude.
sb.jointplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG',kind='hex', data=subme)
print()

### Longitude and latitude.
sb.jointplot(x='LONGITUDE_CIRCLE_IMAGE', y='LATITUDE_CIRCLE_IMAGE', kind='kde', data=subme)
print()