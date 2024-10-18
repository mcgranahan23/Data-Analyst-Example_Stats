import statsmodels.formula.api as smf

# Multiple Regression
model2 = smf.ols('total_wins ~ avg_pts + avg_elo_n', nba_wins_df).fit()
print(model2.summary())


                            OLS Regression Results                            
==============================================================================
Dep. Variable:             total_wins   R-squared:                       0.837
Model:                            OLS   Adj. R-squared:                  0.837
Method:                 Least Squares   F-statistic:                     1580.
Date:                Tue, 15 Oct 2024   Prob (F-statistic):          4.41e-243
Time:                        17:19:37   Log-Likelihood:                -1904.6
No. Observations:                 618   AIC:                             3815.
Df Residuals:                     615   BIC:                             3829.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   -152.5736      4.500    -33.903      0.000    -161.411    -143.736
avg_pts        0.3497      0.048      7.297      0.000       0.256       0.444
avg_elo_n      0.1055      0.002     47.952      0.000       0.101       0.110
==============================================================================
Omnibus:                       89.087   Durbin-Watson:                   1.203
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              160.540
Skew:                          -0.869   Prob(JB):                     1.38e-35
Kurtosis:                       4.793   Cond. No.                     3.19e+04
==============================================================================
