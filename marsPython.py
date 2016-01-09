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

#### Exlude craters with non-empty MORPHOLOGY_EJECTA_1.
print('Subset, non-empty Ejecta Morphology')
subme=data[data['MORPHOLOGY_EJECTA_1']!=" "]
print('Number of observations: ', len(subme))
subme_me1C=subme['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Number of Unique Values: ', len(subme_me1C))
print()
print(subme_me1C)
print()

#### Collapse morphology catagories to first entry before the first '/'.
subme2=subme.copy()
print('Subset, Aggregated non-empty Ejecta Morphology')
subme2['MORPHOLOGY_EJECTA_1']=subme2['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)
print('Number of observations: ', len(subme2))
subme2_me1C=subme2['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Number of Unique Values: ', len(subme2_me1C))
print()
print(subme2_me1C)
print()

#### Exlude MORPHOLOGY_EJECTA_1='Rd' (approximately 60% of the non-empty sample).
subme3=subme2.copy()
print('Subset, Selected, Aggregated non-empty Ejecta Morphology 1 Classification')
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="Rd"]
#### Exclude classifications with frequencies < 10.
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="DLEPSPd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="DLEPd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="DLERCPd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="DLERSRd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="DLSPC"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="MLERSRd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="Pd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="RD"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="SLEPCRd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="SLEPSRd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="SLERSRd"]
subme3=subme3[subme3['MORPHOLOGY_EJECTA_1']!="SLErS"]
print('Number of observations: ', len(subme3))
subme3_me1C=subme3['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
subme3_me1P=subme3['MORPHOLOGY_EJECTA_1'].value_counts(dropna = False, normalize = True).sort_index()
print('Number of Unique Values: ', len(subme3_me1C))
print()
print(subme3_me1C)
print()
print(subme3_me1P)
print()


## 4. Graphing data, univariate analysis. 
#sb.palplot(sb.cubehelix_palette(18, start=.5, rot=-.75))
#sb.palplot(sb.color_palette("coolwarm", 18))
#sb.palplot(sb.diverging_palette(220, 20, n=18))
#sb.palplot(sb.color_palette("RdBu", n_colors=18))
#sb.set_palette("BrBG", n_colors=18)

### Aggregated ejecta morphology.
subme3['MORPHOLOGY_EJECTA_1']=subme3['MORPHOLOGY_EJECTA_1'].astype('category')
sb.countplot(y='MORPHOLOGY_EJECTA_1', data=subme3)
plt.xlabel('Count')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Ejecta Morphology Classification')
print()

### Crater depth.
sb.distplot(subme3['DEPTH_RIMFLOOR_TOPOG'], kde=False, color='k')
plt.xlabel('Histogram')
plt.ylabel('Count')
plt.title('Mars Craters Crater Depth')
print()

### Latitude.
sb.distplot(subme3['LATITUDE_CIRCLE_IMAGE'], kde=False, color='k')
plt.xlabel('Density Plot')
plt.title('Mars Craters Latitude')
print()


## 5. Graphing data, bivariate analysis.

### Factorplot trial...
#sb.factorplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG', col='MORPHOLOGY_EJECTA_1', data=subme3) 

### Aggregated ejecta morphology and crater depth.
sb.boxplot(x='DEPTH_RIMFLOOR_TOPOG', y='MORPHOLOGY_EJECTA_1', data=subme3)
plt.xlabel('Crater Depth')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Crater Depth by Ejecta Morphology Classification')
print()

### Aggregated ejecta morphologyh and latitude.
sb.boxplot(x='LATITUDE_CIRCLE_IMAGE', y='MORPHOLOGY_EJECTA_1', data=subme3)
plt.xlabel('Latitude')
plt.ylabel('Ejecta Morphology')
plt.title('Latitude by Ejecta Morphology Classification')
print()

### Crater depth and latitude.
sb.jointplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG',kind='hex', data=subme3)
print()

### Longitude and latitude.
sb.jointplot(x='LONGITUDE_CIRCLE_IMAGE', y='LATITUDE_CIRCLE_IMAGE', kind='hex', data=subme3)
print()