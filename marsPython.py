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
print()

#### Depth.
depC=data['DEPTH_RIMFLOOR_TOPOG'].value_counts().sort_index() 
print('Crater Depth')
print('Number of Unique Values: ', len(depC))
depS=data['DEPTH_RIMFLOOR_TOPOG'].describe()
print(depS)

#### Ejecta morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Ejecta Morphology 1 Classification')
me1S=data['MORPHOLOGY_EJECTA_1'].describe()
print(me1S)

#### Latitiude.
latC=data['LATITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Latitude')
print('Number of Unique Values: ', len(latC))
latS=data['LATITUDE_CIRCLE_IMAGE'].describe()
print(latS)

#### Longitude.
lonC=data['LONGITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Longitude')
print('Number of Unique Values: ', len(lonC))
lonS=data['LONGITUDE_CIRCLE_IMAGE'].describe()
print(lonS)
print()


## 3. Data management.

### Ejecta morphology.

#### Exlude craters with non-empty MORPHOLOGY_EJECTA_1.
print('Subset, non-empty Ejecta Morphology')
sub=data[data['MORPHOLOGY_EJECTA_1']!=" "]
sub_me1S=sub['MORPHOLOGY_EJECTA_1'].describe()
print(sub_me1S)
print()

#### Collapse morphology catagories to first entry before the first '/'.
sub2=sub.copy()
print('Subset, Aggregated non-empty Ejecta Morphology')
sub2['MORPHOLOGY_EJECTA_1']=sub2['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)
sub2_me1S=sub2['MORPHOLOGY_EJECTA_1'].describe()
print(sub2_me1S)
print()
sub2_me1C=sub2['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print(sub2_me1C)
print()

#### Exlude MORPHOLOGY_EJECTA_1='Rd' (approximately 60% of the non-empty sample).
sub3=sub2.copy()
print('Subset, Selected, Aggregated non-empty Ejecta Morphology 1 Classification')
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="Rd"]
#### Exclude classifications with frequencies < 10.
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="DLEPSPd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="DLEPd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="DLERCPd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="DLERSRd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="DLSPC"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="MLERSRd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="Pd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="RD"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="SLEPCRd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="SLEPSRd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="SLERSRd"]
sub3=sub3[sub3['MORPHOLOGY_EJECTA_1']!="SLErS"]
sub3_me1S=sub3['MORPHOLOGY_EJECTA_1'].describe()
print(sub3_me1S)
print()
sub3_me1C=sub3['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print(sub3_me1C)
print()

#### Exclude crater depths > 2.5.
sub4=sub3.copy()
sub4=sub4[(sub4['DEPTH_RIMFLOOR_TOPOG']<=2.5)]

#### Summary.
print('Summary of Cleaned Data')
print('Selected, Aggregated non-empty Ejecta Morphology 1 Classification')
print('Crater Depth <= 2.5')
sub4S=sub4.describe()
print(sub4S)
sub4_me1S=sub4['MORPHOLOGY_EJECTA_1'].describe()
print(sub4_me1S)
print()

## 4. Graphing data, univariate analysis. 
sb.set(style="whitegrid")
sb.set_palette(sb.cubehelix_palette(18, start=3, rot=-.75))

### Aggregated ejecta morphology.
sub4['MORPHOLOGY_EJECTA_1']=sub4['MORPHOLOGY_EJECTA_1'].astype('category')
sb.countplot(y='MORPHOLOGY_EJECTA_1', data=sub4)
plt.xlabel('Count')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Ejecta Morphology Classification')
plt.show()
print()

### Crater depth.
sb.distplot(sub4['DEPTH_RIMFLOOR_TOPOG'], kde=False, color="y")
plt.xlabel('Histogram')
plt.ylabel('Count')
plt.title('Mars Craters Crater Depth')
plt.show()
print()

### Latitude.
sb.distplot(sub4['LATITUDE_CIRCLE_IMAGE'], kde=True, color="y")
plt.xlabel('Density Plot')
plt.title('Mars Craters Latitude')
plt.show()
print()


## 5. Graphing data, bivariate analysis.
    
### Aggregated ejecta morphology and crater depth.
sb.boxplot(x='DEPTH_RIMFLOOR_TOPOG', y='MORPHOLOGY_EJECTA_1', data=sub4)
plt.xlabel('Crater Depth')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Crater Depth by Ejecta Morphology Classification')
plt.show()
print()

### Aggregated ejecta morphologyh and latitude.
sb.boxplot(x='LATITUDE_CIRCLE_IMAGE', y='MORPHOLOGY_EJECTA_1', data=sub4)
plt.xlabel('Latitude')
plt.ylabel('Ejecta Morphology')
plt.title('Latitude by Ejecta Morphology Classification')
plt.show()
print()

### Crater depth and latitude.
sb.jointplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG',kind='hex', data=sub4)
plt.show()
print()

### Longitude and latitude.
sb.jointplot(x='LONGITUDE_CIRCLE_IMAGE', y='LATITUDE_CIRCLE_IMAGE', kind='hex', data=sub4)
plt.show()
print()