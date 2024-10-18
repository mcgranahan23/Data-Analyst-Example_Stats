import statsmodels.formula.api as smf

model3 = smf.ols('total_wins ~ avg_pts + avg_elo_n + avg_pts_differential + avg_elo_differential ', nba_wins_df).fit()
print(model3.summary())
