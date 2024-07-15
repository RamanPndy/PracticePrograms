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