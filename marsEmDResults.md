### OLS Regression Results  
|Dep. Variable: |    DEPTH_RIMFLOOR_TOPOG |  R-squared:       |                0.260|  
|---------------|-------------------------|-----------------------------------------|  
|Model:         |                     OLS |  Adj. R-squared:  |                0.259|  
|Method:        |           Least Squares |  F-statistic:     |                362.0|  
|Date:          |        Sat, 16 Jan 2016 |  Prob (F-statistic): |              0.00|  
|Time:          |                20:26:05 |  Log-Likelihood:     |           -4326.5|  
|No. Observations:  |               17527 |  AIC:                |             8689.|  
|Df Residuals:      |               17509 |  BIC:                |             8829.|  
|Df Model:          |                  17 |                      |                  |  
|Covariance Type:   |           nonrobust |                      |                  |  
  
|                                  |      coef  |  std err |         t  |    P>|t|  |    [95.0% Conf. Int.]  |  
|----------------------------------|------------|----------|------------|-----------|------------------------|  
|Intercept                         |    0.2259  |    0.014 |    16.218  |    0.000  |       0.199     0.253|  
|C(MORPHOLOGY_EJECTA_1)[T.DLEPCPd] |   -0.2229  |    0.099 |    -2.252  |    0.024  |      -0.417    -0.029|  
|C(MORPHOLOGY_EJECTA_1)[T.DLEPS]   |    0.1643  |    0.019 |     8.833  |    0.000  |       0.128     0.201|  
|C(MORPHOLOGY_EJECTA_1)[T.DLERC]   |   -0.0266  |    0.021 |    -1.266  |    0.206  |      -0.068     0.015|  
|C(MORPHOLOGY_EJECTA_1)[T.DLERS]   |    0.5243  |    0.016 |    31.830  |    0.000  |       0.492     0.557|  
|C(MORPHOLOGY_EJECTA_1)[T.MLEPC]   |    0.1555  |    0.068 |     2.303  |    0.021  |       0.023     0.288|  
|C(MORPHOLOGY_EJECTA_1)[T.MLEPS]   |    0.4646  |    0.049 |     9.430  |    0.000  |       0.368     0.561|  
|C(MORPHOLOGY_EJECTA_1)[T.MLERC]   |    0.1879  |    0.065 |     2.901  |    0.004  |       0.061     0.315|  
|C(MORPHOLOGY_EJECTA_1)[T.MLERS]   |    0.8630  |    0.020 |    43.657  |    0.000  |       0.824     0.902|  
|C(MORPHOLOGY_EJECTA_1)[T.SLEPC]   |    0.0195  |    0.015 |     1.285  |    0.199  |      -0.010     0.049|  
|C(MORPHOLOGY_EJECTA_1)[T.SLEPCPd] |   -0.2164  |    0.038 |    -5.636  |    0.000  |      -0.292    -0.141|  
|C(MORPHOLOGY_EJECTA_1)[T.SLEPS]   |    0.1805  |    0.015 |    12.359  |    0.000  |       0.152     0.209|  
|C(MORPHOLOGY_EJECTA_1)[T.SLEPSPd] |   -0.1738  |    0.045 |    -3.847  |    0.000  |      -0.262    -0.085|  
|C(MORPHOLOGY_EJECTA_1)[T.SLEPd]   |    0.2793  |    0.049 |     5.730  |    0.000  |       0.184     0.375|  
|C(MORPHOLOGY_EJECTA_1)[T.SLERC]   |    0.0481  |    0.016 |     2.935  |    0.003  |       0.016     0.080|  
|C(MORPHOLOGY_EJECTA_1)[T.SLERCPd] |   -0.2189  |    0.099 |    -2.211  |    0.027  |      -0.413    -0.025|  
|C(MORPHOLOGY_EJECTA_1)[T.SLERS]   |    0.3121  |    0.015 |    21.398  |    0.000  |       0.284     0.341|  
|C(MORPHOLOGY_EJECTA_1)[T.SLERSPd] |   -0.1796  |    0.079 |    -2.282  |    0.022  |      -0.334    -0.025|  
  
|--------------------------------------|-----------------------------------------|
|Omnibus:                      702.553 |  Durbin-Watson:                   1.081 |  
|Prob(Omnibus):                  0.000 |  Jarque-Bera (JB):              903.394 |  
|Skew:                           0.431 |  Prob(JB):                    6.77e-197 |  
|Kurtosis:                       3.703 |  Cond. No.                         47.6 |  
  
Warnings:  
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.  
  
Crater Depth by Aggregated Ejecta Morphology  
Mean  
|MORPHOLOGY_EJECTA_1 | DEPTH_RIMFLOOR_TOPOG|  
|--------------------|---------------------|                   
|DLEPC               |             0.225879|  
|DLEPCPd             |             0.003000|  
|DLEPS               |             0.390222|  
|DLERC               |             0.199249|  
|DLERS               |             0.750161|  
|MLEPC               |             0.381364|  
|MLEPS               |             0.690465|  
|MLERC               |             0.413750|  
|MLERS               |             1.088873|  
|SLEPC               |             0.245406|  
|SLEPCPd             |             0.009467|  
|SLEPS               |             0.406343|  
|SLEPSPd             |             0.052115|  
|SLEPd               |             0.505227|  
|SLERC               |             0.274016|  
|SLERCPd             |             0.007000|  
|SLERS               |             0.538012|  
|SLERSPd             |             0.046250|  
  
Standard Deviation  
  
|MORPHOLOGY_EJECTA_1 | DEPTH_RIMFLOOR_TOPOG|  
|--------------------|---------------------|  
|DLEPC               |             0.262318|  
|DLEPCPd             |             0.009487|  
|DLEPS               |             0.379797|  
|DLERC               |             0.252662|  
|DLERS               |             0.412736|  
|MLEPC               |             0.367298|  
|MLEPS               |             0.441102|  
|MLERC               |             0.375092|  
|MLERS               |             0.426162|  
|SLEPC               |             0.223601|  
|SLEPCPd             |             0.032958|  
|SLEPS               |             0.298070|  
|SLEPSPd             |             0.109658|  
|SLEPd               |             0.415085|  
|SLERC               |             0.274048|  
|SLERCPd             |             0.011595|  
|SLERS               |             0.324965|  
|SLERSPd             |             0.087015|  
  
Multiple Comparison of Means - Tukey HSD,FWER=0.05  
| group1 | group2 | meandiff | lower |  upper | reject|  
|--------|--------|----------|-------|--------|------|  
| DLEPC  |DLEPCPd -0.2229  -0.5682  0.1225 False |  
| DLEPC  | DLEPS   0.1643   0.0994  0.2293  True |  
| DLEPC  | DLERC  -0.0266  -0.1001  0.0468 False |  
| DLEPC  | DLERS   0.5243   0.4668  0.5818  True |  
| DLEPC  | MLEPC   0.1555  -0.0801  0.3911 False |  
| DLEPC  | MLEPS   0.4646   0.2927  0.6365  True |  
| DLEPC  | MLERC   0.1879  -0.0381  0.4139 False |  
| DLEPC  | MLERS   0.863    0.794   0.932   True |  
| DLEPC  | SLEPC   0.0195  -0.0335  0.0726 False |  
| DLEPC  |SLEPCPd -0.2164  -0.3504 -0.0824  True |  
| DLEPC  | SLEPS   0.1805   0.1295  0.2314  True |  
| DLEPC  |SLEPSPd -0.1738  -0.3314 -0.0161  True |  
| DLEPC  | SLEPd   0.2793   0.1092  0.4494  True |  
| DLEPC  | SLERC   0.0481  -0.0091  0.1054 False |  
| DLEPC  |SLERCPd -0.2189  -0.5642  0.1265 False |  
| DLEPC  | SLERS   0.3121   0.2612  0.363   True |  
| DLEPC  |SLERSPd -0.1796  -0.4543  0.095  False |  
|DLEPCPd | DLEPS   0.3872   0.0426  0.7319  True |  
|DLEPCPd | DLERC   0.1962  -0.1501  0.5426 False |  
|DLEPCPd | DLERS   0.7472   0.4039  1.0905  True |  
|DLEPCPd | MLEPC   0.3784   -0.034  0.7907 False |  
|DLEPCPd | MLEPS   0.6875   0.3079  1.0671  True |  
|DLEPCPd | MLERC   0.4108   0.0038  0.8177  True |  
|DLEPCPd | MLERS   1.0859   0.7405  1.4313  True |  
|DLEPCPd | SLEPC   0.2424  -0.1002  0.585  False |  
|DLEPCPd |SLEPCPd  0.0065  -0.3575  0.3705 False |  
|DLEPCPd | SLEPS   0.4033   0.0611  0.7456  True |  
|DLEPCPd |SLEPSPd  0.0491  -0.3242  0.4225 False |  
|DLEPCPd | SLEPd   0.5022   0.1234  0.881   True |  
|DLEPCPd | SLERC   0.271   -0.0722  0.6143 False |  
|DLEPCPd |SLERCPd  0.004   -0.4796  0.4876 False |  
|DLEPCPd | SLERS   0.535    0.1927  0.8773  True |  
|DLEPCPd |SLERSPd  0.0433  -0.3926  0.4791 False |  
| DLEPS  | DLERC   -0.191  -0.2608 -0.1211  True |  
| DLEPS  | DLERS   0.3599   0.3071  0.4128  True |  
| DLEPS  | MLEPC  -0.0089  -0.2434  0.2257 False |  
| DLEPS  | MLEPS   0.3002   0.1298  0.4707  True |  
| DLEPS  | MLERC   0.0235  -0.2013  0.2484 False |  
| DLEPS  | MLERS   0.6987   0.6335  0.7638  True |  
| DLEPS  | SLEPC  -0.1448  -0.1928 -0.0968  True |  
| DLEPS  |SLEPCPd -0.3808  -0.5128 -0.2487  True |  
| DLEPS  | SLEPS   0.0161  -0.0296  0.0618 False |  
| DLEPS  |SLEPSPd -0.3381  -0.4941 -0.1821  True |  
| DLEPS  | SLEPd   0.115   -0.0536  0.2836 False |  
| DLEPS  | SLERC  -0.1162  -0.1688 -0.0636  True |  
| DLEPS  |SLERCPd -0.3832  -0.7279 -0.0386  True |  
| DLEPS  | SLERS   0.1478   0.1022  0.1934  True |  
| DLEPS  |SLERSPd  -0.344  -0.6177 -0.0702  True |  
| DLERC  | DLERS   0.5509   0.4879  0.6139  True |  
| DLERC  | MLEPC   0.1821  -0.0549  0.4191 False |  
| DLERC  | MLEPS   0.4912   0.3174  0.6651  True |  
| DLERC  | MLERC   0.2145   -0.013  0.442  False |  
| DLERC  | MLERS   0.8896   0.816   0.9633  True |  
| DLERC  | SLEPC   0.0462  -0.0128  0.1051 False |  
| DLERC  |SLEPCPd -0.1898  -0.3262 -0.0533  True |  
| DLERC  | SLEPS   0.2071    0.15   0.2642  True |  
| DLERC  |SLEPSPd -0.1471  -0.3069  0.0126 False |  
| DLERC  | SLEPd   0.306    0.1339  0.478   True |  
| DLERC  | SLERC   0.0748   0.012   0.1376  True |  
| DLERC  |SLERCPd -0.1922  -0.5386  0.1541 False |  
| DLERC  | SLERS   0.3388   0.2817  0.3958  True |  
| DLERC  |SLERSPd  -0.153  -0.4289  0.1229 False |  
| DLERS  | MLEPC  -0.3688  -0.6014 -0.1362  True |  
| DLERS  | MLEPS  -0.0597  -0.2274  0.108  False |  
| DLERS  | MLERC  -0.3364  -0.5592 -0.1136  True |  
| DLERS  | MLERS   0.3387   0.2809  0.3965  True |  
| DLERS  | SLEPC  -0.5048   -0.542 -0.4675  True |  
| DLERS  |SLEPCPd -0.7407  -0.8693 -0.6121  True |  
| DLERS  | SLEPS  -0.3438  -0.3781 -0.3095  True |  
| DLERS  |SLEPSPd  -0.698  -0.8511  -0.545  True |  
| DLERS  | SLEPd  -0.2449  -0.4108 -0.0791  True |  
| DLERS  | SLERC  -0.4761  -0.5192 -0.4331  True |  
| DLERS  |SLERCPd -0.7432  -1.0865 -0.3999  True |  
| DLERS  | SLERS  -0.2121  -0.2464 -0.1779  True |  
| DLERS  |SLERSPd -0.7039   -0.976 -0.4319  True |  
| MLEPC  | MLEPS   0.3091   0.0257  0.5925  True |  
| MLEPC  | MLERC   0.0324  -0.2868  0.3515 False |  
| MLEPC  | MLERS   0.7075   0.4718  0.9432  True |  
| MLEPC  | SLEPC   -0.136  -0.3675  0.0955 False |  
| MLEPC  |SLEPCPd -0.3719  -0.6341 -0.1097  True |  
| MLEPC  | SLEPS   0.025   -0.2061  0.256  False |  
| MLEPC  |SLEPSPd -0.3292  -0.6043 -0.0542  True |  
| MLEPC  | SLEPd   0.1239  -0.1585  0.4062 False |  
| MLEPC  | SLERC  -0.1073  -0.3399  0.1252 False |  
| MLEPC  |SLERCPd -0.3744  -0.7867  0.038  False |  
| MLEPC  | SLERS   0.1566  -0.0744  0.3877 False |  
| MLEPC  |SLERSPd -0.3351  -0.6904  0.0202 False |  
| MLEPS  | MLERC  -0.2767  -0.5522 -0.0012  True |  
| MLEPS  | MLERS   0.3984   0.2264  0.5704  True |  
| MLEPS  | SLEPC  -0.4451  -0.6113 -0.2788  True |  
| MLEPS  |SLEPCPd  -0.681  -0.8878 -0.4742  True |  
| MLEPS  | SLEPS  -0.2841  -0.4497 -0.1185  True |  
| MLEPS  |SLEPSPd -0.6383  -0.8612 -0.4155  True |  
| MLEPS  | SLEPd  -0.1852  -0.4171  0.0466 False |  
| MLEPS  | SLERC  -0.4164  -0.5841 -0.2488  True |  
| MLEPS  |SLERCPd -0.6835  -1.0631 -0.3039  True |  
| MLEPS  | SLERS  -0.1525   -0.318  0.0131 False |  
| MLEPS  |SLERSPd -0.6442  -0.9609 -0.3276  True |  
| MLERC  | MLERS   0.6751   0.449   0.9012  True |  
| MLERC  | SLEPC  -0.1683  -0.3901  0.0534 False |  
| MLERC  |SLEPCPd -0.4043  -0.6579 -0.1507  True |  
| MLERC  | SLEPS  -0.0074  -0.2287  0.2138 False |  
| MLERC  |SLEPSPd -0.3616  -0.6285 -0.0948  True |  
| MLERC  | SLEPd   0.0915  -0.1829  0.3659 False |  
| MLERC  | SLERC  -0.1397  -0.3625  0.083  False |  
| MLERC  |SLERCPd -0.4068  -0.8137  0.0002 False |  
| MLERC  | SLERS   0.1243   -0.097  0.3455 False |  
| MLERC  |SLERSPd -0.3675  -0.7165 -0.0185  True |  
| MLERS  | SLEPC  -0.8435  -0.8968 -0.7901  True |  
| MLERS  |SLEPCPd -1.0794  -1.2135 -0.9453  True |  
| MLERS  | SLEPS  -0.6825  -0.7338 -0.6312  True |  
| MLERS  |SLEPSPd -1.0368  -1.1945  -0.879  True |  
| MLERS  | SLEPd  -0.5836  -0.7538 -0.4134  True |  
| MLERS  | SLERC  -0.8149  -0.8724 -0.7573  True |  
| MLERS  |SLERCPd -1.0819  -1.4273 -0.7365  True |  
| MLERS  | SLERS  -0.5509  -0.6021 -0.4996  True |  
| MLERS  |SLERSPd -1.0426  -1.3173 -0.7679  True |  
| SLEPC  |SLEPCPd -0.2359  -0.3626 -0.1093  True |  
| SLEPC  | SLEPS   0.1609   0.1348  0.1871  True |  
| SLEPC  |SLEPSPd -0.1933  -0.3447 -0.0419  True |  
| SLEPC  | SLEPd   0.2598   0.0954  0.4242  True |  
| SLEPC  | SLERC   0.0286  -0.0083  0.0655 False |  
| SLEPC  |SLERCPd -0.2384   -0.581  0.1042 False |  
| SLEPC  | SLERS   0.2926   0.2666  0.3187  True |  
| SLEPC  |SLERSPd -0.1992  -0.4703  0.072  False |  
|SLEPCPd | SLEPS   0.3969   0.2711  0.5227  True |  
|SLEPCPd |SLEPSPd  0.0426  -0.1525  0.2378 False |  
|SLEPCPd | SLEPd   0.4958   0.2904  0.7011  True |  
|SLEPCPd | SLERC   0.2645   0.1361  0.393   True |  
|SLEPCPd |SLERCPd -0.0025  -0.3665  0.3615 False |  
|SLEPCPd | SLERS   0.5285   0.4028  0.6543  True |  
|SLEPCPd |SLERSPd  0.0368   -0.261  0.3345 False |  
| SLEPS  |SLEPSPd -0.3542   -0.505 -0.2035  True |  
| SLEPS  | SLEPd   0.0989  -0.0648  0.2626 False |  
| SLEPS  | SLERC  -0.1323  -0.1662 -0.0985  True |  
| SLEPS  |SLERCPd -0.3993  -0.7416 -0.0571  True |  
| SLEPS  | SLERS   0.1317   0.1102  0.1532  True |  
| SLEPS  |SLERSPd -0.3601  -0.6308 -0.0893  True |  
|SLEPSPd | SLEPd   0.4531   0.2316  0.6746  True |  
|SLEPSPd | SLERC   0.2219   0.0689  0.3749  True |  
|SLEPSPd |SLERCPd -0.0451  -0.4185  0.3282 False |  
|SLEPSPd | SLERS   0.4859   0.3352  0.6366  True |  
|SLEPSPd |SLERSPd -0.0059   -0.315  0.3033 False |  
| SLEPd  | SLERC  -0.2312   -0.397 -0.0654  True |  
| SLEPd  |SLERCPd -0.4982   -0.877 -0.1194  True |  
| SLEPd  | SLERS   0.0328  -0.1309  0.1965 False |  
| SLEPd  |SLERSPd  -0.459  -0.7746 -0.1433  True |  
| SLERC  |SLERCPd  -0.267  -0.6103  0.0762 False |  
| SLERC  | SLERS   0.264    0.2302  0.2978  True |  
| SLERC  |SLERSPd -0.2278  -0.4998  0.0442 False |  
|SLERCPd | SLERS   0.531    0.1887  0.8733  True |  
|SLERCPd |SLERSPd  0.0393  -0.3966  0.4751 False |  
| SLERS  |SLERSPd -0.4918  -0.7625  -0.221  True |  

