R-squared, also known as the coefficient of determination, is a statistical measure that indicates the proportion of the variance in the dependent variable that is predictable from the independent variable(s) in a linear regression model. It provides an indication of the goodness of fit of the model.

Here's a more detailed explanation:

1. **Definition**:
   - \( R^2 = 1 - \frac{SS_{res}}{SS_{tot}} \)
   - \( SS_{res} \) (Sum of Squares of Residuals) is the sum of the squared differences between the observed values and the predicted values.
   - \( SS_{tot} \) (Total Sum of Squares) is the sum of the squared differences between the observed values and the mean of the observed values.

2. **Interpretation**:
   - **\( R^2 = 1 \)**: This means the model perfectly explains all the variability of the response data around its mean. Every point on the plot of actual vs. predicted values lies exactly on the regression line.
   - **\( R^2 = 0 \)**: This means the model does not explain any of the variability of the response data around its mean. The predicted values are no better than simply using the mean of the observed values.
   - **\( 0 < R^2 < 1 \)**: This indicates the proportion of the variance in the dependent variable that is predictable from the independent variable(s). For example, an \( R^2 \) of 0.8 means 80% of the variance in the dependent variable is explained by the model.

3. **Limitations**:
   - **Overfitting**: A very high \( R^2 \) value, especially in models with many predictors, might indicate overfitting rather than a genuinely good fit.
   - **Cannot Compare Models with Different Dependent Variables**: \( R^2 \) values cannot be used to compare models with different dependent variables.
   - **Doesn't Indicate Causation**: A high \( R^2 \) value does not imply that the independent variable(s) cause the dependent variable to change. It only indicates a statistical correlation.

4. **Adjusted R-squared**:
   - Adjusted \( R^2 \) is a modified version of \( R^2 \) that adjusts for the number of predictors in the model. It is used to prevent the problem of overfitting by taking into account the number of predictors relative to the number of data points.
   - The formula for adjusted \( R^2 \) is:
     \[
     R^2_{adj} = 1 - \left( \frac{1-R^2}{n-p-1} \right) \cdot (n-1)
     \]
     where \( n \) is the number of observations and \( p \) is the number of predictors.

In summary, \( R^2 \) is a useful measure for assessing the explanatory power of a linear regression model, but it should be used in conjunction with other metrics and domain knowledge to evaluate the model's performance comprehensively.

What according to you are the reasons for a linear regression model overfitting?
Overfitting in a linear regression model occurs when the model is too complex and fits the noise or random fluctuations in the training data rather than capturing the underlying relationship. Here are some common reasons for overfitting in linear regression:

Too Many Features:
Including too many predictor variables, especially if they are not relevant or have little predictive power, can cause the model to fit the noise in the training data.

High Multicollinearity:
When predictor variables are highly correlated with each other, it can lead to unstable estimates of coefficients and overfitting.

Insufficient Training Data:
Having a small training dataset with too many features can lead to a model that is too tailored to the specific data points in the training set.

Outliers:
Presence of outliers can significantly affect the regression model, leading to overfitting as the model tries to accommodate these extreme values.

Complex Polynomial Terms:
Adding high-degree polynomial terms or interaction terms can increase model complexity and result in overfitting.

Lack of Regularization:
Regularization techniques like Ridge (L2) or Lasso (L1) regression help to penalize large coefficients and reduce overfitting. Absence of such techniques can contribute to overfitting.

Noise in the Data:
If the data contains a lot of random noise, a complex model may fit this noise rather than the underlying trend.

Feature Engineering:
Creating too many derived or interaction features without proper validation can lead to an overly complex model.

To mitigate overfitting, one can use techniques such as cross-validation, regularization, simplifying the model by removing irrelevant features, and ensuring that the training dataset is sufficiently large and representative of the population.

when building an OLS model, we want to estimate the coefficients for which the cost/loss, i.e., RSS, is minimum. 
Optimising this cost function results in model coefficients with the least possible bias, although the model may have overfitted and hence have high variance. 

In case of overfitting, we know that we need to manage the model’s complexity by primarily taking care of the magnitudes of the coefficients.
The more extreme values of the coefficients are (high positive or negative values of the coefficients), the more complex the model is and, hence, the higher are the chances of overfitting. 

Ridge Regularization:
Unlike OLS, which has a single set of model coefficients, Ridge regressions gets different model coefficients for each value of lambda.
The model coefficients of ridge regression can shrink very close to 0 but do not become 0 and hence there is no feature selection with ridge regression.
The cost function in regularized regression models has two terms: the error term and the regularization term. The objective of the learning algorithm is to find the coefficients, betas, such that The sum of the error term and the regularization term is minimised. The objective is to minimise the error term and penalise the coefficients in the regularization term in order to obtain a simpler model
A large lambda implies a simpler model. Therefore, a simpler model would have higher bias and lower variance.

Lasso vs. Ridge
Generally, Lasso should perform better in situations where only a few among all the predictors that are used to build our model have a significant influence on the response variable. So, feature selection, which removes the unrelated variables, should help. But Ridge should do better when all the variables have almost the same influence on the response variable.

Lasso performs better in situations where only a few among all the predictors that are used to build our model have a significant influence on the response variable.

Higher the value of lambda in the shrinkage term, more are the model coefficients pushed towards 0 and hence more the regularization.

Standardizing variables is necessary before regularization.

As λ increases from 0 to infinity, select the correct option that describes the pattern of the residual sum of squares (RSS) of the training dataset. Differentiating the cost function with lambda=0 gives the value of the coefficients which minimizes the RSS. Again, putting λ = infinity gives us a constant model with maximum RSS. Thus, the RSS steadily increases with the variation of lambda.

When λ=0, the alphas have their least square estimate values. The actual estimates heavily depend on the training data and hence variance is high. As we increase λ, alphas start decreasing and model becomes simpler. In the limiting case of λ approaching infinity, all betas reduce to zero and model predicts a constant and has no variance.

When λ=0, alphas have their least-square estimate values and hence have the least bias. As λ increases, alphas start reducing towards zero, the model fits less accurately to training data and hence bias increases. In the limiting case of λ approaching infinity, the model predicts a constant and hence bias is maximum.

Higher the lambda, more the regularization and smaller the constraint region i.e. lower the value of c.
