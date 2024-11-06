<h3>Elimination based on p-values</h3>

![Alt text](images/lr-num-of-tweets.png)

<b>Ans :</b> Number of Tweets<br>
<p>Yes! As you can see, the p-value of 'Number of Tweets' is very high and thus, this variable is insignificant. Now, there are other variables in the list which also have a high p-value but we don't drop these simultaneously as it might happen that dropping 'Number of Tweets' might reduce the p-value of the other variables and make them significant.</p>
<hr>
<h3>Scaling Variables</h3>
<p>Which of the following is/are true regarding the scaling of variables? More than one option(s) may be correct.</p><br>
<b>Ans:</b>
<ul>
<li>Scaling should be done after the test-train split.<br>
<b>Explaination:</b><p>Correct! Scaling should always be done after the test-train split since you don't want the test dataset to learn anything from the train data. So if you're performing the test-train split earlier, the test data will then have information regarding the data like the minimum and maximum values, etc.</p>
</li>
<li>Standardised scaling will affect the values of dummy variables but MinMax scaling will not.<br>
<b>Explaination:</b>

![Alt text](images/min-max-scaling.png)
</li>
</ul>
<hr>
<h3>Multiple Linear Regression</h3>

![Alt text](images/multiple-lr.png)
<b>Ans:</b><p> The predicted value of Y increases by β1 for a unit increase in X1, given X2 does not change.</p><br>
<b>Explaination:</b><p>Consider the value of X1 changes from 0 to 1 and the value of X2 stays as 0 or a constant. Then, the value of Y would have changed by β1 units given beta2 and X2 are constants.</p>
<hr>
<h3>Rsq-Adjusted</h3>
<p>In the R-squared Adjusted metric, R-squared is “adjusted” or modified according to:</p>
<b>Ans:</b>
<ul>
<li>Number of predictors<br>
<p>In the R-squared Adjusted formula, you can see the term ‘k’ in the denominator, where ‘k’ refers to the number of predictors or features in the model.</p>
</li>
<li>Sample size<br>
<p>In the R-squared Adjusted formula, you can see the term ‘n’ in both numerator and denominator, where ‘n’ refers to sample size.</p>
</li>
</ul>
<hr>
<h3>Using Linear Regression</h3>
<p>A researcher wishes to find out the amount of rainfall on a given day, given that pressure, temperature and wind conditions are known.</p>
<b>Explaination:</b><p>Past data could be used to predict what the rainfall will be based on the given predictors.</p>
<hr>
<h3>Projection</h3>
<p>Which of the following are true in case of projection?</p>
<b>Ans:</b>
<ul>
<li>While making a projection, it is assumed that the conditions in which the model was built continue to be the same<br>
<p>Forecast assumes that conditions remain the same as they were when the model was built.</p></li>
<li>The accuracy of the final outcome is more important than the identification of the most important driver variables<br>
<p>While making a projection, the aim is accuracy. Thus, a complex model containing a large number of variables, with high accuracy is more valuable than a simple model with lower accuracy.</p></li>
</ul>
<hr>
<h3> Multiple Linear Regression</h3>
<p>You are given a multiple linear regression model: Y = β0 + β1.x1 + β2.x2 + β3.x3<br>
Recall that the null hypothesis states that the variable is insignificant. Thus, if we fail to reject the null hypothesis, you can say that the predictor is insignificant.<br>
For e.g. if you fail to reject null hypothesis for x1, you can say that x1 is insignificant. This would also imply that the coefficient for x1 i.e., β1 = 0.<br>
In other words, the null hypothesis tests if the predictor's coefficient, i.e βi = 0. If the null hypothesis is rejected then βi ≠ 0.</p><br>
<p>If β1 = β2 = 0 holds and β3 = 0 fails to hold, then what can you conclude?
<b>Ans:</b><p>There is a linear relationship between the outcome variable(Y) and x3</p>
<b>Explaination:</b><p>Since, β3=0 fails to hold, this means that x3 is a significant variable in this linear regression model. Thus, we can say that there is a linear relationship between the outcome variable(Y) and x3</p>
<hr>
<p>An analyst observes a positive relationship between digital marketing expenses and online sales for a firm. However, she intuitively feels that she should add an additional predictor variable, one which has a high correlation with marketing expenses.<br>

If the analyst adds this independent variable to the model, which of the following could happen? More than one choices could be correct.</p>
<b>Ans:</b>
<ul>
<li>The model’s adjusted R-squared could decrease<br>
<p>Adjusted R-squared could decrease if the variable does not add much to the model, to explain Online Sales.</p>
</li>
<li>The relationship between marketing expenses and sales can become insignificant<br>
<p>The relation between marketing expenses and sales can become insignificant with the addition of a new variable.</p>
</li>
</ul>
<hr>
<p>Suppose you need to build a model on a data set which contains 2 categorical variables with 2 and 4 levels respectively. How many dummy variables should you create for model building?>
<b>Ans:</b><p>Since n-1 dummy variables can be used to describe a variable with n levels, you will get 1 dummy variable for the variable with two levels, and 3 dummy variables for the variable with 4 levels.</p>
<hr>
<p>If one of the feature variables say, A is being explained well by some of the other feature variables, this would mean that the variable A has:</p>
<b>Ans:</b>A high VIF<br>
<b>Explaination:</b><p>Correct! If the feature variable A is being well explained by the other feature variables, this would mean that A has a high VIF. This is also evident from the formula for VIF: 1/(1−Ri^2). <br>
Now, if A is being explained by some of the other feature variables, this would mean that the R-squared value is pretty high, which would make the denominator which is (1−Ri^2) very low, which again, in turn, would make the VIF value high. </p>
<hr>
<p>Given different Rsq values of linear regression models on the same dataset, which model would you choose as the best predictor?</p>
<b>Ans:</b><p>Rsq values alone are insufficient to answer this question.</p><br>
<b>Explaination:</b><p> Rsq values are sometimes too high even due to overfitting. You cannot compare models with a different number of features/predictors without the rsq adjusted value.</p>
<hr>
<p>Which of the following is indicative of a strong relationship between X and y?</p>
<b>Ans:</b><p>The correlation coefficient between X and y is 0.95</p><br>
<b>Explaination:</b><p>The correlation coefficient specifies how strong is the relationship between two variables. And in this case, the value is 0.95 which is quite high indicating a strong relationship between X and y.</p><br>
<hr>
<p>In order to determine whether the coefficient in a simple linear regression model is significant or not, which Null Hypothesis do we propose?</p>
<b>Ans:</b><p>β1 = 0</p><br>
<b>Explaination:</b><p>This is kept so because in case that the Null hypothesis is rejected, you can conclude that β1 is not zero and the coefficient is significant, but if we fail to reject the Null Hypothesis, the coefficient is deemed insignificant.</p><br>
<hr>
<p>Which metric is used to determine the significance of the overall model fit?</p>
<b>Ans:</b><p>F-statistic</p><br>
<b>Explaination:</b><p>The F-statistic tells whether the overall model fit is significant or not.</p><br>
<hr>
<p>Why do you add a constant to the train set using the sm.add_constant() command, when you’re fitting a line using statsmodels?</p>
<b>Ans:</b><p>statsmodels fits a line passing through the origin by default.</p><br>
<b>Explaination:</b><p>By default, statsmodels fits a line passing through the origin, i.e. it doesn't fit an intercept. Hence, you need to use the command 'add_constant' so that it also fits an intercept.</p><br>
<hr>
<p>The correlation coefficient between the age of a person and their IQ test score is found to be -1.0087.
What can you conclude from this?</p>
<b>Ans:</b><p>The correlation coefficient should be in the range [1,-1]. A value beyond this range indicates an error in measurement.</p><br>
<hr>
<p>A Singapore-based startup Healin launched an app called JustShakeIt, which enables a user to send an emergency alert to emergency contacts and/or caregivers simply by shaking the phone with one hand. The program uses a machine learning algorithm to distinguish between actual emergency shakes and everyday jostling, using data with labels.

What kind of problem is this?</p>
<b>Ans:</b><p>Supervised learning-Classification</p><br>
<b>Explaination:</b><p>The algorithm has to distinguish between actual emergency shakes and everyday jostling. Here, your output variable has predefined labels (shake/jostle), which are categorical in nature. So, this is a supervised learning-classification problem.</p><br>
<hr>
<h3>Regression in Machine Learning</h3>
<p>Select all the tasks where linear regression algorithm can be applied.</p>
<b>Ans:</b>
<ul>
<li>You have a dataset of BMI (body mass index) and the fat percentage of the customers of a fitness centre. Now, the fitness centre wants to predict the fat percentage of a new customer, given his BMI.<br>
Here, the output variable (dependent variable, which is to be predicted) is the fat percentage, which is a numeric variable. So, this is a regression task.</li>
<li>You want to predict the sales of a retail store based on its size, given the dataset of sales of retail stores and their sizes.<br>
Here, the output variable (dependent variable, which is to be predicted) is sales, which is a numeric variable. So, this is a regression task.</li>
</ul>
<hr>
<h3>Coefficients of Regression Equation</h3>
<p>The independent variable X from a linear regression is measured in miles. If you convert it to kilometres (keeping the unit of the dependent variable Y the same), how will the slope coefficient change? (Note: 1 mile = 1.6 km)</p>
<b>Ans:</b><p>It will get divided by 1.6.</p><br>
<b>Explaination:</b><p>In the linear regression equation, X gets multiplied by 1.6 with no change in Y. So, the slope will be divided by 1.6.</p><br>
<hr>
<h3>Strength of the Regression Model</h3>

![Alt text](images/strength-regression-model.png)

<b>Ans:</b><p>The linear relation between X and Y is strong, and their correlation will be negative.</p><br>
<b>Explaination:</b><p>A higher value of R² means a strong linear relation. As Y is decreasing with the increasing value of X, you can conclude that their correlation will be negative.</p><br>
<hr>