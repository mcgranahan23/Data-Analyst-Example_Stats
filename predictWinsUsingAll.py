import statsmodels.formula.api as smf

model3 = smf.ols('total_wins ~ avg_pts + avg_elo_n + avg_pts_differential + avg_elo_differential ', nba_wins_df).fit()
print(model3.summary())


                            OLS Regression Results                            
==============================================================================
Dep. Variable:             total_wins   R-squared:                       0.878
Model:                            OLS   Adj. R-squared:                  0.877
Method:                 Least Squares   F-statistic:                     1102.
Date:                Tue, 15 Oct 2024   Prob (F-statistic):          3.07e-278
Time:                        17:37:34   Log-Likelihood:                -1815.5
No. Observations:                 618   AIC:                             3641.
Df Residuals:                     613   BIC:                             3663.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept               34.5753     25.867      1.337      0.182     -16.223      85.373
avg_pts                  0.2597      0.043      6.070      0.000       0.176       0.344
avg_elo_n               -0.0134      0.017     -0.769      0.442      -0.048       0.021
avg_pts_differential     1.6206      0.135     12.024      0.000       1.356       1.885
avg_elo_differential     0.0525      0.018      2.915      0.004       0.017       0.088
==============================================================================
Omnibus:                      193.608   Durbin-Watson:                   0.979
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              598.416
Skew:                          -1.503   Prob(JB):                    1.14e-130
Kurtosis:                       6.769   Cond. No.                     2.11e+05
==============================================================================
