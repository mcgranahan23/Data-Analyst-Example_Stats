As a data analyst for the Bulls, I’ve been asked by our coach to predict the total number of wins in a season using regression models based on performance metrics. 
The metrics included are total wins, average points, average relative skill, average point differential, and average skill differential. 

Our coach is expecting teams to win more games in a season if they have a higher average relative skill compared to other teams because the chances of winning are higher if 
the team maintains a high average relative skill. 
If this statement is true, the total number of wins and the average relative skill are correlated or dependent on each other. If a correlation is positive, as one 
variable increases the other increases as well. 
If a correlation is negative, as one variable increases the other decreases; so, our coach is predicting a positive correlation. 

We created a scatterplot to visualize the correlation between average relative skill and total number of wins and calculated a correlation coefficient of 0.9072. 
This coefficient represents a strong positive correlation between the two variables because the coefficient is between 0.80 and 1.0. 
The correlation is positive because as the average relative skill increases, so does the total number of wins. 
A correlation this strong is sufficient evidence to support our coach’s hypothesis that the total number of wins is dependent on the average relative skill of a team. 

Our coach believes a team has more wins in a season if it maintains a high average relative skill during that season. 
We created a regression model to predict how many games our team might win in a regular season by using the total number of wins in a season as the response variable (the variable 
we are trying to predict) and the average relative skill as a predictor variable (the variable used to make the prediction). 
From our calculations we can predict that as the average relative skill goes up by one, the total number of wins increases by 0.1121. 
We also have a p-value equal to zero, proving the null hypothesis incorrect and showing the number of wins in a season is dependent on the average relative skill of a team. 
To predict how many games our team will win in a season our coach can use the model Y^ = -128.2475 + 0.1121x and replace the ‘x’ with the average relative skill level of our team. 
The result of the equation will be the predicted number of wins that season. 

We also created a scatterplot to find correlation between the average number of points scored in a game and the total number of wins in a season. 
Our coach’s hypothesis is that the number of wins in a season increases as the average number of points scored increases, which makes the null hypothesis state that these 
two variables have no effect on each other. 
From our calculations we ended up with a correlation coefficient of 0.4777, which is considered a moderate correlation but is very close to a weak correlation. 
From these calculations we can assume the number of wins in a season is correlated to the number of points scored per game, but it doesn’t have as much as an effect 
as the average relative skill does.   

We created a multiple regression model to predict the total number of wins in a season by using the total number of wins as a response variable and 
using the average number of points scored and the average relative skill as predictor variables. We once again have a p-value of zero, so we can reject the null hypothesis 
that stated these variables had no effect on each other. Our calculations predict Y^ = -152.5736 + 0.3497x1 + 0.1055x2. The x1 variable represents the average points scored and 
the x2 variable represents the average relative skill, so for the coach to use this model for predictions he would replace those variables with points and skill level and the result 
of the equation will provide the estimated number of wins. 


Our final calculation is to predict the total number of wins in a season using the average points, average relative skill level, average point differential between teams, and 
average skill differential between teams as predictor variables. Using this many variables in our calculation increased the explained variance to 87.8%, meaning about 88% of the 
variance in the total number of wins can be explained by the variance in the other four variables. Our other models only gave us about 83% explained variance, so this method should 
be about 5% more accurate. Our coach can predict the total number of wins in a season by using this model; Y^ = 34.5753 + 0.2597x1 – 0.0134x2 + 1.6206x3 + 0.0525x4, where x1 = average 
points, x2 = average relative skill, x3 = average point differential, and x4 = average skill differential. The result of the equation will give you the most accurate estimation of total wins in a season. 

With these tools in hand our coach can confidently estimate the total number of wins in a season using our team’s average points, average skill, average point differential, and average skill 
differential, either individually or combined. 
