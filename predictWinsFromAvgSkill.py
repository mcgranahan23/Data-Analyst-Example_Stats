import statsmodels.formula.api as smf

# Simple Linear Regression

model1 = smf.ols('total_wins ~ avg_elo_n', nba_wins_df).fit()
print(model1.summary())
