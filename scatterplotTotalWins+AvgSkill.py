import scipy.stats as st

plt.plot(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'], 'o')

plt.title('Total Number of Wins by Average Relative Skill', fontsize=20)
plt.xlabel('Average Relative Skill')
plt.ylabel('Total Number of Wins')
plt.show()


correlation_coefficient, p_value = st.pearsonr(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'])

print("Correlation between Average Relative Skill and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", round(p_value,4))
