# Craters on Mars  
### Ejecta Morphology and Crater Depth  


## 1. Set-up. 

### Load packages. 
import pandas as pd
import numpy as np
import decimal
import seaborn as sb
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 


### Import data.
data=pd.read_csv("marscrater_pds.csv", low_memory=False)

### Bug fix for display formats. 
pd.set_option('display.float_format', lambda x:'%f'%x)

### Force Spyder to display full results.
pd.set_option('display.max_rows', None)

### Ensure relevant data is in numeric format. 
data['DEPTH_RIMFLOOR_TOPOG']=pd.to_numeric(data['DEPTH_RIMFLOOR_TOPOG'])


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
print()

#### Ejecta morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Ejecta Morphology 1 Classification')
me1S=data['MORPHOLOGY_EJECTA_1'].describe()
print(me1S)
print()


## 3. Data management.

### Ejecta morphology.

#### Exclude craters with non-empty MORPHOLOGY_EJECTA_1.
print('Subset, non-empty Ejecta Morphology')
sub=data[data['MORPHOLOGY_EJECTA_1']!=" "]
sub_me1S=sub['MORPHOLOGY_EJECTA_1'].describe()
print(sub_me1S)
print()

#### Collapse morphology categories to first entry before the first '/'.
sub2=sub.copy()
print('Subset, Aggregated non-empty Ejecta Morphology')
sub2['MORPHOLOGY_EJECTA_1']=sub2['MORPHOLOGY_EJECTA_1'].str.replace('/\D+', '', case=False)
sub2_me1S=sub2['MORPHOLOGY_EJECTA_1'].describe()
print(sub2_me1S)
sub2_me1C=sub2['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print(sub2_me1C)
print()

#### Exclude MORPHOLOGY_EJECTA_1='Rd' (approximately 60% of the non-empty sample).
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


## 5. Graphing data, bivariate analysis.
    
### Aggregated ejecta morphology and crater depth.
sb.boxplot(x='DEPTH_RIMFLOOR_TOPOG', y='MORPHOLOGY_EJECTA_1', data=sub4)
plt.xlabel('Crater Depth')
plt.ylabel('Ejecta Morphology')
plt.title('Mars Craters Crater Depth by Ejecta Morphology Classification')
plt.show()
print()


## 6. ANOVA (ANalysis Of VAriance).

### Use OLS estimator (ordinary least squares) function to calculate the F-statistic and associated p-value.

#### Aggregated ejecta morphology and crater depth.
subemD=sub4[['DEPTH_RIMFLOOR_TOPOG', 'MORPHOLOGY_EJECTA_1']].dropna()

emDOls=smf.ols(formula='DEPTH_RIMFLOOR_TOPOG ~ C(MORPHOLOGY_EJECTA_1)', data=subemD)
emDOR=emDOls.fit()
print(emDOR.summary())
print()

print('Crater Depth by Aggregated Ejecta Morphology')
emDM=subemD.groupby('MORPHOLOGY_EJECTA_1').mean()
print('Mean')
print(emDM)
print()
emDS=subemD.groupby('MORPHOLOGY_EJECTA_1').std()
print('Standard Deviation')
print(emDS)
print()

##### Post hoc analysis using Tukey's Honestly Significant Difference Test.
emDMc=multi.MultiComparison(subemD['DEPTH_RIMFLOOR_TOPOG'], subemD['MORPHOLOGY_EJECTA_1'])
emDMR=emDMc.tukeyhsd()
print(emDMR.summary())
print()