<h3>Calculating Sensitivity</h3>

![Alt text](images/churn-senstivity.png)

<b>Ans :</b> 0.1<br>
<b>Explaination :</b><p>Recall that the formula for sensitivity is given by -<br>

Sensitivity = TP/(TP+FN)<br>

Here, TP = 1050 and FN = 350<br>

Hence, initially, the sensitivity was -<br>

Sensitivity = 1050/(1050+350)=75%<br>

Now, when you changed the threshold, the number of true positives changes from 1050 to 1190. Now, since the number of actual positives will be the same always, i.e. (1050 + 350 = 1400) from the original confusion matrix, you can now calculate the new sensitivity as - <br>

Sensitivity =1190/1400=0.85<br>

Hence, the change in sensitivity = 0.85 - 0.75 = 0.1</p>
<hr>

<h3>Calculating Precision</h3>

<p> Consider the confusion matrix you had in the last question. Calculate the values of precision and recall for the model and determine which of the two is higher.</p>

<b>Ans :</b> Recall<br>
<b>Explaination :</b><p>Recall that precision and recall are given by -<br>

Precision=TP/(TP+FP)<br>

Recall=TP/(TP+FN)<br>

Here, TP = 1050; FP = 400; FN= 350<br>

Hence, you get -<br>

Precision=1050/(1050+400) ≈ 72.41%<br>

Recall=1050/(1050+350) ≈ 75%<br>

As you can see, of the two, recall is higher.</p>
<hr>

<h3>True Positive Rate</h3>

<p> The True Positive Rate (TPR) metric is exactly the same as?</p>

<b>Ans :</b> Sensitivity<br>
<b>Explaination :</b><p>Recall the formula for TPR is given as:<br>

TPR = True Positives / Total Number of Actual Positives<br>

Which can be rewritten as -<br>

TPR = TP / (TP + FN)<br>

And this is exactly the same as sensitivity as you might remember.<br>
Recall == senstivity == TPR == TP / (TP + FN)
</p>
<hr>

<h3>Threshold</h3>

![Alt text](images/churn-threshold.png)

<b>Ans :</b>0.50 and 0.55<br>
<b>Explaination :</b>See the table carefully. For patient 1007, the predicted probability is 0.48 and the predicted class is 0. This means that the cutoff has to be greater than 0.48. Also, for patient 1002, the predicted probability is 0.58 and the predicted class is 1. This means that the cutoff has to be lesser than 0.58.<br>

Therefore, the cutoff can lie between 0.48-0.58 and hence, 0.50 are 0.55 can be valid cutoffs for the model above.
<hr>

<h3>Evaluation Metrics</h3>

![Alt text](images/patient-evaluation-metrics.png)

<p>Calculate the values of Accuracy, Sensitivity, Specificity, and Precision. Which of these four metrics is the highest for the model?</p>

<b>Ans :</b> Sensitivity<br>

![Alt text](images/patient-evaluation-metrics-answer.png)

<hr>

<h3>Logistic Regression in Python</h3>

<p> Which of these methods is used for fitting a logistic regression model using statsmodels?</p>

<b>Ans :</b> GLM() <br>
<p>The GLM() method is used to fit a logistic regression model using statsmodels.</p>
<hr>

<h3>Confusion Matrix</h3>

<p> Given the following confusion matrix, calculate the accuracy of the model.</p>
<table>
<tr>
<td>Actual/Predicted</td>
<td>Nos</td>
<td>Yeses</td>
</tr>
<tr>
<td>Nos</td>
<td>1000</td>
<td>50</td>
</tr>
<tr>
<td>Yeses</td>
<td>250</td>
<td>1200</td>
</tr>
</table>

<b>Ans :</b> 88% <br>
<b>Explaination :</b><p>Recall that the formula for accuracy is given as - <br>

Accuracy = Correctly Predicted Labels / Total Number of Labels<br>

Here, the number of correctly predicted labels is = 1000 + 1200 = 2200.<br>

And the total number of labels is = 1000 + 250 + 50 + 1200 = 2500<br>

Hence, you have - <br>

Accuracy = 2200/ 2500 = 0.88 = 88%</p>
<hr>

<h3>Diabetic based on Threshold</h3>

![Alt text](images/diabetic-threshold.png)

<b>Ans :</b> 6 <br>
<b>Explaination :</b> <p>The cut-off is given to be 0.4. Hence, for a patient to be classified as diabetic, Probability(Diabetes) needs to be greater than 0.4. As you can see in the table above, there are 6 patients who have Probability(Diabetes) > 0.4. These are:

A: 0.82, D: 0.41, E: 0.55, F: 0.62, H: 0.91, I: 0.74</p>
<hr>

<h3>Log Odds</h3>
In **logistic regression**, the **log odds** (or logit) is the natural logarithm of the odds of an event occurring. It represents the relationship between the input variables (predictors) and the probability of a binary outcome.

### Explanation of Log Odds:
- **Odds**: The odds of an event happening is the ratio of the probability that the event occurs to the probability that it does not occur. 
  \[
  \text{Odds} = \frac{P(\text{event})}{1 - P(\text{event})}
  \]
  where \( P(\text{event}) \) is the probability of the event happening.

- **Log Odds (Logit)**: Logistic regression models the **logarithm of odds**. The **logit** is the natural logarithm of the odds, which makes the relationship linear, allowing the model to estimate coefficients.
  \[
  \text{Log Odds} = \log \left( \frac{P(\text{event})}{1 - P(\text{event})} \right)
  \]

In logistic regression, the model is typically expressed as:
\[
\text{logit}(P) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
\]
where:
- \( P \) is the probability of the event occurring (e.g., success, positive outcome),
- \( \beta_0, \beta_1, \dots, \beta_n \) are the regression coefficients,
- \( x_1, x_2, \dots, x_n \) are the input features.

The log odds are then transformed back into a probability using the **logistic function**:
\[
P = \frac{1}{1 + e^{-\text{logit}}}
\]
This maps the log odds into a probability between 0 and 1.

### Example:
If the log odds of an event occurring are 2, then the odds are \( e^2 \), and the probability of the event happening can be computed from the odds. This concept is crucial in **logistic regression** because it allows the model to predict probabilities based on input features.

### Key Points:
1. **Log odds** transform the problem into a linear one, which allows logistic regression to be solved like a linear regression problem.
2. The **odds ratio** is interpreted as the multiplicative change in the odds for a one-unit increase in the predictor variable.

### Why Log Odds?
Log odds are used in logistic regression because they ensure that the model can handle probabilities that are constrained between 0 and 1. By modeling log odds as a linear function of the predictors, logistic regression ensures that the resulting probabilities are valid (i.e., between 0 and 1) through the logistic transformation.

### Summary:
In logistic regression, the **log odds** represent the log-transformed odds of an event happening, and the model uses this transformation to make predictions that are probabilities between 0 and 1.

![Alt text](images/log-odds.png)

<b>Ans :</b> Reetesh <br>
<b>Explaination :</b>

![Alt text](images/log-odds-answer.png)
<hr>

To build a **Logistic Regression** model in Python, you can use **scikit-learn** or implement it manually for a deeper understanding. Logistic regression is primarily used for binary classification problems, where the output is either 0 or 1.

---

### **1. Using Scikit-Learn**

#### Example: Predicting if a student will pass based on study hours.

```python
# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Example dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Features and target
X = df[['Hours_Studied']]  # Independent variable
y = df['Pass']             # Dependent variable (binary classification)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
```

---

### **2. Logistic Regression from Scratch**

Logistic regression uses the **sigmoid function** to map predictions to probabilities.

#### Sigmoid Function:
\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

Where \(z = X \cdot \theta\).

#### Steps:
1. Initialize weights (\(\theta\)).
2. Compute predictions using the sigmoid function.
3. Use the **log-loss function** to calculate error.
4. Optimize weights using gradient descent.

#### Example Implementation:

```python
import numpy as np

# Example dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Hours Studied
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Pass/Fail

# Add bias term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialize weights
theta = np.zeros(X.shape[1])

# Learning rate and iterations
learning_rate = 0.1
iterations = 1000

# Gradient descent
for i in range(iterations):
    z = np.dot(X, theta)
    predictions = sigmoid(z)
    error = predictions - y
    gradient = np.dot(X.T, error) / len(y)
    theta -= learning_rate * gradient

# Print final weights
print("Trained Weights:", theta)

# Make predictions
def predict(X, theta):
    z = np.dot(X, theta)
    return sigmoid(z) >= 0.5

print("Predictions:", predict(X, theta))
```

---

### **3. Model Evaluation**
- **Confusion Matrix**: Evaluates true positives, false positives, true negatives, and false negatives.
- **Accuracy**: Ratio of correct predictions to total predictions.
- **Precision, Recall, F1-Score**: Useful for imbalanced datasets.

### **4. Use Cases**
- Spam detection.
- Disease prediction.
- Customer churn prediction.

<hr>
In a **logistic regression model**, the choice between **recall**, **precision**, or **sensitivity** depends on the specific use case and the aspect of accuracy you want to evaluate. Here's a breakdown:

---

### 1. **Recall (Sensitivity or True Positive Rate)**:
- **Definition**: Measures the proportion of actual positive cases correctly identified by the model.
\[
\text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}}
\]
- **Use Case**: Use when **false negatives** are critical.
  - Example: In a medical diagnosis model, failing to identify a disease (false negative) is more critical than false alarms (false positives).

---

### 2. **Precision**:
- **Definition**: Measures the proportion of predicted positive cases that are actually positive.
\[
\text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}}
\]
- **Use Case**: Use when **false positives** are critical.
  - Example: In spam detection, flagging a legitimate email as spam (false positive) is more critical than missing a spam email (false negative).

---

### 3. **Accuracy**:
- **Definition**: The overall correctness of the model, measuring the proportion of correctly predicted instances (both positives and negatives).
\[
\text{Accuracy} = \frac{\text{True Positives (TP)} + \text{True Negatives (TN)}}{\text{Total Predictions}}
\]
- **Use Case**: Use for balanced datasets where false positives and false negatives have similar costs.

---

### 4. **Sensitivity (Recall)**:
- Sensitivity is synonymous with **recall**. It’s important when identifying all positive cases is a priority.

---

### 5. **F1 Score**:
- **Definition**: The harmonic mean of precision and recall, used when you need a balance between the two.
\[
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
\]
- **Use Case**: Use for imbalanced datasets where both false positives and false negatives are costly.

---

### Choosing the Right Metric:
1. **Imbalanced Dataset**: Focus on **precision**, **recall**, or **F1-score**.
   - **High cost of false negatives**: Use **recall/sensitivity**.
   - **High cost of false positives**: Use **precision**.
2. **Balanced Dataset**: Use **accuracy**.
3. **General Purpose**: Use **F1-score** for a balance between precision and recall.

### Example:
- In a fraud detection system:
  - **Recall** ensures all fraudulent transactions are identified (low false negatives).
  - **Precision** ensures flagged transactions are truly fraudulent (low false positives).

In logistic regression, the **log odds** (also known as the logit function) are used to predict the probability of an event occurring based on the given input features. The log odds are transformed using the logistic (sigmoid) function to produce a probability between 0 and 1.

### Steps to Use Log Odds in Logistic Regression for Model Prediction:

1. **Linear Model (Log Odds)**:
   The first step in logistic regression is to compute the **log odds** (logit). It is a linear combination of the input features and their corresponding weights (coefficients):
   \[
   \text{logit}(P) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
   \]
   Here:
   - \( \beta_0 \) is the intercept,
   - \( \beta_1, \beta_2, \dots, \beta_n \) are the coefficients,
   - \( x_1, x_2, \dots, x_n \) are the input features.

2. **Logistic Function (Sigmoid)**:
   To convert log odds into probabilities, we apply the **logistic function** (also called the **sigmoid function**):
   \[
   P = \frac{1}{1 + e^{-\text{logit}}}
   \]
   This maps the log odds to a value between 0 and 1, which can then be interpreted as the probability of the event happening.

### Example Code to Use Log Odds for Prediction:

Let’s walk through an example where we use a logistic regression model to calculate probabilities using log odds.

#### Example Code:

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data: X features and y labels (0 or 1 for binary classification)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])

# Train a logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Predicting log odds (logit)
log_odds = model.decision_function(X)  # This gives the log odds
print("Log Odds:", log_odds)

# Converting log odds to probability using the sigmoid function
probabilities = 1 / (1 + np.exp(-log_odds))
print("Predicted Probabilities:", probabilities)
```

### Explanation of the Code:
1. We use `sklearn`'s `LogisticRegression` model to train a logistic regression classifier on the sample data.
2. `model.decision_function(X)` returns the **log odds** for each data point. These are the raw outputs (logits) from the model before the logistic function is applied.
3. We then convert these log odds to probabilities using the **sigmoid function** (i.e., \( P = \frac{1}{1 + e^{-z}} \)).

### Log Odds Interpretation:
- A positive log odd means that the event is more likely to happen (probability > 0.5).
- A negative log odd means the event is less likely to happen (probability < 0.5).
- Log odds close to 0 means the event is equally likely to occur or not.

### Example Output:
```
Log Odds: [-3.31205344 -1.8968904   0.51829243  2.93344547]
Predicted Probabilities: [0.03557642 0.13082746 0.62674386 0.94933789]
```

Here, the **log odds** are negative for the first two points (indicating the event is less likely to happen) and positive for the last two points (indicating a higher likelihood of the event occurring).

### Practical Use in Logistic Regression:
- **Log odds** are used internally by the logistic regression model to make predictions.
- **Probabilities** are the final output, which can be thresholded (e.g., classifying as 1 if the probability is greater than 0.5, or 0 otherwise).
  
### When to Use Log Odds in Logistic Regression:
- **Model Interpretation**: Log odds are useful for interpreting the coefficients of the logistic regression model. For instance, a coefficient of 1 means that for each unit increase in the feature, the odds of the event occurring are multiplied by \( e^1 \approx 2.718 \).
- **Odds Ratio**: The log odds can be converted into **odds ratios** (which are easier to interpret) by exponentiating the log odds.

### Summary:
- **Log odds** are the linear combination of input features and their corresponding coefficients.
- The **sigmoid function** transforms log odds into probabilities (between 0 and 1).
- You can use the **log odds** in logistic regression for making predictions, but usually, the final predicted probabilities are of greater interest.

This approach ensures that logistic regression models handle classification tasks effectively by predicting probabilities from log odds.