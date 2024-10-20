import statsmodels.formula.api as smf

# Simple Linear Regression

model1 = smf.ols('total_wins ~ avg_elo_n', nba_wins_df).fit()
print(model1.summary())


                            OLS Regression Results                            
==============================================================================
Dep. Variable:             total_wins   R-squared:                       0.823
Model:                            OLS   Adj. R-squared:                  0.823
Method:                 Least Squares   F-statistic:                     2865.
Date:                Tue, 15 Oct 2024   Prob (F-statistic):          8.06e-234
Time:                        17:00:58   Log-Likelihood:                -1930.3
No. Observations:                 618   AIC:                             3865.
Df Residuals:                     616   BIC:                             3873.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   -128.2475      3.149    -40.731      0.000    -134.431    -122.064
avg_elo_n      0.1121      0.002     53.523      0.000       0.108       0.116
==============================================================================
Omnibus:                      152.822   Durbin-Watson:                   1.098
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              393.223
Skew:                          -1.247   Prob(JB):                     4.10e-86
Kurtosis:                       6.009   Cond. No.                     2.14e+04
==============================================================================
