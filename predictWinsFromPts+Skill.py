import statsmodels.formula.api as smf

# Multiple Regression
model2 = smf.ols('total_wins ~ avg_pts + avg_elo_n', nba_wins_df).fit()
print(model2.summary())
