# Craters on Mars

## 1. Set-up. 

### Load packages. 
import pandas as pd
import numpy as np
import decimal
import seaborn as sb
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import scipy.stats



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
print()

#### Ejecta morphology.
me1C=data['MORPHOLOGY_EJECTA_1'].value_counts().sort_index()
print('Ejecta Morphology 1 Classification')
me1S=data['MORPHOLOGY_EJECTA_1'].describe()
print(me1S)
print()

#### Latitude.
latC=data['LATITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Latitude')
print('Number of Unique Values: ', len(latC))
latS=data['LATITUDE_CIRCLE_IMAGE'].describe()
print(latS)
print()

#### Longitude.
lonC=data['LONGITUDE_CIRCLE_IMAGE'].value_counts().sort_index()
print('Longitude')
print('Number of Unique Values: ', len(lonC))
lonS=data['LONGITUDE_CIRCLE_IMAGE'].describe()
print(lonS)
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

### Aggregated ejecta morphology and latitude.
sb.boxplot(x='LATITUDE_CIRCLE_IMAGE', y='MORPHOLOGY_EJECTA_1', data=sub4)
plt.xlabel('Latitude')
plt.ylabel('Ejecta Morphology')
plt.title('Latitude by Ejecta Morphology Classification')
plt.show()
print()

### Crater depth and latitude.
sb.jointplot(x='LATITUDE_CIRCLE_IMAGE', y='DEPTH_RIMFLOOR_TOPOG', kind='hex', data=sub4)
plt.show()
print()

### Longitude and latitude.
sb.jointplot(x='LONGITUDE_CIRCLE_IMAGE', y='LATITUDE_CIRCLE_IMAGE', kind='hex', data=sub4)
plt.show()
print()


## 6. ANOVA (ANalysis Of VAriance).

### Use OLS estimator (ordinary least squares) function to calculate the F-statistic and associated p-value.

### Aggregated ejecta morphology and crater depth.
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

### Post hoc analysis using Tukey's Honestly Significant Difference Test.
emDMc=multi.MultiComparison(subemD['DEPTH_RIMFLOOR_TOPOG'], subemD['MORPHOLOGY_EJECTA_1'])
emDMR=emDMc.tukeyhsd()
print(emDMR.summary())
print()

### Aggregated ejecta morphology and latitude.
subemLa=sub4[['LATITUDE_CIRCLE_IMAGE', 'MORPHOLOGY_EJECTA_1']].dropna()

emLaOls=smf.ols(formula='LATITUDE_CIRCLE_IMAGE ~ MORPHOLOGY_EJECTA_1', data=subemLa)
emLaRe = emLaOls.fit()
print (emLaRe.summary())

print('Crater Depth by Aggregated Ejecta Morphology')
emLaM=subemLa.groupby('MORPHOLOGY_EJECTA_1').mean()
print('Mean')
print(emLaM)
print()
emLaS=subemLa.groupby('MORPHOLOGY_EJECTA_1').std()
print('Standard Deviation')
print(emLaS)
print()

### Post hoc analysis using Tukey's Honestly Significant Difference Test.
emLaMc=multi.MultiComparison(subemLa['LATITUDE_CIRCLE_IMAGE'], subemLa['MORPHOLOGY_EJECTA_1'])
emLaMR=emLaMc.tukeyhsd()
print(emLaMR.summary())
print()


## 7. Chi-Squared Test of Independence.

### Bin LATITUDE_CIRCLE_IMAGE into to categories: northern (positive values), and southern hemisphere (negative values). Craters along the equator (latitude 0) are included in counts for the southern hemisphere for simplicity.
sub4['LATITUDE_CIRCLE_IMAGE2']=pd.cut(sub4['LATITUDE_CIRCLE_IMAGE'], [-91, 0, 91], labels=['Southern', 'Northern'])
sub4['LATITUDE_CIRCLE_IMAGE2']=sub4['LATITUDE_CIRCLE_IMAGE2'].astype('category')

### Create a contingency table of observed counts of aggregated ejecta morphology by number of layers. Explanatory: aggregated; ejecta morphology. Response: location (north vs. south).
emLaT=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['MORPHOLOGY_EJECTA_1'])
print('Cross-Tab Frequency Table, Aggregated Ejecta Morphology and Hemisphere')
print (emLaT)
print()

#### Graph.
#emLaT.plot(kind='bar', stacked=True, grid=False)

### Calculate column percentages.
print('Cross-Tab Frequency Table, Aggregated Ejecta Morphology and Hemisphere')
colsum=emLaT.sum(axis=0)
colpct=emLaT/colsum
print(colpct)
print()

### Run chi-squared test.
print('Aggregated Ejecta Morphology and Location')
print ('Chi-Square, p-value, Expected Values')
emLaCs= scipy.stats.chi2_contingency(emLaT)
print (emLaCs)

### Run post-hoc analysis using the Bonferroni Adjustment.

#### Calculate adjusted p-value (p* = p/c, where c=number of comparisons, p=original p-vlue, = p*=adjusted p-value).
padjem=sub4['MORPHOLOGY_EJECTA_1'].value_counts()
padjn=len(padjem)
print('Number of levels: ', padjn)
padjc=scipy.misc.comb(padjn, 2, exact=True, repetition=False)
print('Number of Comparisons: ', padjc)
padj=0.05/padjc
print('Adjusted p-value, p*: ', padj)
print()

##### Comparisons.
print('Selected, Aggregated non-empty Ejecta Morphology  Classification')
print(sub4['MORPHOLOGY_EJECTA_1'].value_counts().sort_index())

##### Because of the large number of comparisons required, the post-hoc analysis will focus on one specific ejecta morphology type, SLERS, which is themost common type in the sample.  

#### DLEPC vs SLERS.
print('DLEPC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode1 = {'DLEPC':'DLEPC', 'SLERS':'SLERS'}
sub4['COMP1']= sub4['MORPHOLOGY_EJECTA_1'].map(recode1)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp1T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP1'])
#print (comp1T)
comp1S=comp1T.sum(axis=0)
comp1P=comp1T/comp1S
#print(comp1P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp1CS= scipy.stats.chi2_contingency(comp1T)
print(comp1CS)
print()

#### DLEPCPd vs SLERS.
print('DLEPCPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode2 = {'DLEPCPd':'DLEPCPd', 'SLERS':'SLERS'}
sub4['COMP2']= sub4['MORPHOLOGY_EJECTA_1'].map(recode2)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp2T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP2'])
#print (comp2T)
comp2S=comp2T.sum(axis=0)
comp2P=comp2T/comp2S
#print(comp2P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp2CS= scipy.stats.chi2_contingency(comp2T)
print(comp2CS)
print()

#### DLEPS vs SLERS.
print('DLEPS vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode3 = {'DLEPS':'DLEPS', 'SLERS':'SLERS'}
sub4['COMP3']=sub4['MORPHOLOGY_EJECTA_1'].map(recode3)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp3T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP3'])
#print (comp3T)
comp3S=comp3T.sum(axis=0)
comp3P=comp3T/comp3S
#print(comp3P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp3CS= scipy.stats.chi2_contingency(comp3T)
print(comp3CS)
print()

#### DLERC vs SLERS.
print('DLERC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode4 = {'DLERC':'DLERC', 'SLERS':'SLERS'}
sub4['COMP4']=sub4['MORPHOLOGY_EJECTA_1'].map(recode4)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp4T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP4'])
#print (comp4T)
comp4S=comp4T.sum(axis=0)
comp4P=comp4T/comp4S
#print(comp4P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp4CS= scipy.stats.chi2_contingency(comp4T)
print(comp4CS)
print()

#### DLERS vs SLERS.
print('DLERS vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode5 = {'DLERS':'DLERS', 'SLERS':'SLERS'}
sub4['COMP5']= sub4['MORPHOLOGY_EJECTA_1'].map(recode5)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp5T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP5'])
#print (comp5T)
comp5S=comp5T.sum(axis=0)
comp5P=comp5T/comp5S
#print(comp5P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp5CS= scipy.stats.chi2_contingency(comp5T)
print(comp5CS)
print()

#### MLEPC vs SLERS.
print('MLEPC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode6 = {'MLEPC':'MLEPC', 'SLERS':'SLERS'}
sub4['COMP6']= sub4['MORPHOLOGY_EJECTA_1'].map(recode6)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp6T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP6'])
#print (comp6T)
comp6S=comp6T.sum(axis=0)
comp6P=comp6T/comp6S
#print(comp6P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp6CS= scipy.stats.chi2_contingency(comp6T)
print(comp6CS)
print()

#### MLEPS vs SLERS.
print('MLEPS vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode7 = {'MLEPS':'MLEPS', 'SLERS':'SLERS'}
sub4['COMP7']= sub4['MORPHOLOGY_EJECTA_1'].map(recode7)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp7T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP7'])
#print (comp7T)
comp7S=comp7T.sum(axis=0)
comp7P=comp7T/comp7S
#print(comp7P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp7CS= scipy.stats.chi2_contingency(comp7T)
print(comp7CS)
print()

#### MLERC vs SLERS.
print('MLERC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode8 = {'MLERC':'MLERC', 'SLERS':'SLERS'}
sub4['COMP8']= sub4['MORPHOLOGY_EJECTA_1'].map(recode8)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp8T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP8'])
#print (comp8T)
comp8S=comp8T.sum(axis=0)
comp8P=comp8T/comp8S
#print(comp8P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp8CS= scipy.stats.chi2_contingency(comp8T)
print(comp8CS)
print()

#### MLERS vs SLERS.
print('MLERS vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode9 = {'MLERS':'MLERS', 'SLERS':'SLERS'}
sub4['COMP9']= sub4['MORPHOLOGY_EJECTA_1'].map(recode9)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp9T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP9'])
#print (comp9T)
comp9S=comp9T.sum(axis=0)
comp9P=comp9T/comp9S
#print(comp9P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp9CS= scipy.stats.chi2_contingency(comp9T)
print(comp9CS)
print()

#### SLEPC vs SLERS.
print('SLEPC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode10 = {'SLEPC':'SLEPC', 'SLERS':'SLERS'}
sub4['COMP10']= sub4['MORPHOLOGY_EJECTA_1'].map(recode10)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp10T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP10'])
#print (comp10T)
comp10S=comp10T.sum(axis=0)
comp10P=comp10T/comp10S
#print(comp10P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp10CS= scipy.stats.chi2_contingency(comp10T)
print(comp10CS)
print()

#### SLEPCPd vs SLERS.
print('SLEPCPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode11 = {'SLEPCPd':'SLEPCPd', 'SLERS':'SLERS'}
sub4['COMP11']= sub4['MORPHOLOGY_EJECTA_1'].map(recode11)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp11T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP11'])
#print (comp11T)
comp11S=comp11T.sum(axis=0)
comp11P=comp11T/comp11S
#print(comp11P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp11CS= scipy.stats.chi2_contingency(comp11T)
print(comp11CS)
print()

#### SLEPS vs SLERS.
print('SLEPS vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode12 = {'SLEPS':'SLEPS', 'SLERS':'SLERS'}
sub4['COMP12']= sub4['MORPHOLOGY_EJECTA_1'].map(recode12)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp12T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP12'])
#print (comp12T)
comp12S=comp12T.sum(axis=0)
comp12P=comp12T/comp12S
#print(comp12P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp12CS= scipy.stats.chi2_contingency(comp12T)
print(comp12CS)
print()

#### SLEPSPd vs SLERS.
print('SLEPSPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode13 = {'SLEPSPd':'SLEPSPd', 'SLERS':'SLERS'}
sub4['COMP13']= sub4['MORPHOLOGY_EJECTA_1'].map(recode13)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp13T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP13'])
#print (comp13T)
comp13S=comp13T.sum(axis=0)
comp13P=comp13T/comp13S
#print(comp13P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp13CS= scipy.stats.chi2_contingency(comp13T)
print(comp13CS)
print()

#### SLEPd vs SLERS.
print('SLEPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode14 = {'SLEPd':'SLEPd', 'SLERS':'SLERS'}
sub4['COMP14']= sub4['MORPHOLOGY_EJECTA_1'].map(recode14)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp14T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP14'])
#print (comp14T)
comp14S=comp14T.sum(axis=0)
comp14P=comp14T/comp14S
#print(comp14P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp14CS= scipy.stats.chi2_contingency(comp14T)
print(comp14CS)
print()

#### SLERC vs SLERS.
print('SLERC vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode15 = {'SLERC':'SLERC', 'SLERS':'SLERS'}
sub4['COMP15']= sub4['MORPHOLOGY_EJECTA_1'].map(recode15)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp15T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP15'])
#print (comp15T)
comp15S=comp15T.sum(axis=0)
comp15P=comp15T/comp15S
#print(comp15P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp15CS= scipy.stats.chi2_contingency(comp15T)
print(comp15CS)
print()

#### SLERCPd vs SLERS.
print('SLERCPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode16 = {'SLERCPd':'SLERCPd', 'SLERS':'SLERS'}
sub4['COMP16']= sub4['MORPHOLOGY_EJECTA_1'].map(recode16)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp16T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP16'])
#print (comp16T)
comp16S=comp16T.sum(axis=0)
comp16P=comp16T/comp16S
#print(comp16P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp16CS= scipy.stats.chi2_contingency(comp16T)
print(comp16CS)
print()

#### SLERSPd vs SLERS.
print('SLERSPd vs SLERS')
##### Recode to isolate desired values. Map to new variable.
recode17 = {'SLERSPd':'SLERSPd', 'SLERS':'SLERS'}
sub4['COMP17']= sub4['MORPHOLOGY_EJECTA_1'].map(recode17)
##### Compute sum and percentage tables. 
#print('Post-Hoc Comparisons: Cross-Tab Tables, Counts and Percentages')
comp17T=pd.crosstab(sub4['LATITUDE_CIRCLE_IMAGE2'], sub4['COMP17'])
#print (comp17T)
comp17S=comp17T.sum(axis=0)
comp17P=comp17T/comp17S
#print(comp17P)
##### Chi-squared test.
print('Chi-Square, p-value, Expected Values')
print('chi-square value, p value, expected counts')
comp17CS= scipy.stats.chi2_contingency(comp17T)
print(comp17CS)
print()
