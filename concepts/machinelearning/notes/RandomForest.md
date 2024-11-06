<h3>Random Forest</h3>
<p>Which of these is most appropriate to use as a baseline (benchmark) model?</p>
<b>Ans :</b>Logistic regression<br>
<b>Explaination :</b>Logistic regression is simple to run, with no hyperparameters to tune. It can be used as a benchmark to compare the performance of other models.
<hr>

<p>Which of the following algorithms is not advisable to use when you have limited CPU resources and time, and when the data set is relatively large?</p>
<b>Ans :</b>Support vector machines<br>
<b>Explaination :</b>Support vector machines can take quite a bit of time to run because of their resource-intensive nature. It also takes multiple runs to choose the best kernel for a particular problem.
<hr>

<p>On a binary classification task, a logistic regression model gives 67% accuracy on the training set, a decision tree model gives 82% accuracy and an SVM model with a linear kernel gives 69% accuracy. What is NOT a likely reason for the superior results of the tree model?</p>
<b>Ans :</b>The dataset contains only continuous attributes<br>
<b>Explaination :</b>A decision tree generally does not perform well on a dataset with a lot of continuous variables. Since the tree is performing well on the dataset, it is highly unlikely that the data has only continuous attributes.
<hr>

<p>Given a decision tree model on a binary classification task, which among the following is the best way to check whether the tree is overfitting?</p>
<b>Ans :</b>Compare the accuracy of the tree model on the training and validation sets.<br>
<b>Explaination :</b>If the difference between training and validation accuracy is significant, then you can conclude that the tree has overfitted the data.
<hr>

<p>Given a binary classification dataset, say having Y = 1 or 0 as the target variable and X1 and X2 as two numeric attributes, what does it mean to say that the dataset is linearly separable?</p>
<b>Ans :</b>A straight line a.X1 + b.X2 + c = 0 can separate the points Y=0 from Y=1<br>
<b>Explaination :</b>A dataset is linearly separable when the different classes can be separated using a line. Here, classes 0 and 1 are being separated by the given equation of line.
<hr>

<p>Why is logistic regression called a linear model?</p>
<b>Ans :</b>The log odds of the target variable Y and the attribute X lie on a straight line<br>
<b>Explaination :</b>The equation of log odds is​ ln(P/1−P) = β0 + β1.X1 + β2.X2​. <br>The right handside of the above equation is a linear line where the log odds of the target variable Y and the attributes X1 and X2 , all lie on the same line.
<hr>

<h3>Random Forests over Decision Trees</h3>
<p>Which of the following is/are benefit(s) of random forest over a decision tree? (More than one option may be correct.)</p>
<b>Ans :</b>
<ul>
<li>It is more stable than a decision tree
<li>It reduces overfitting
</ul>
<hr>

<h3>Decision Trees</h3>
<p>Consider decision tree A learned with min_samples_leaf = 500. Now consider decision tree B trained on the same dataset and parameters, except that the min_samples_leaf=50. Which of the following is/are always true? (More than one option may be correct.)</p>
<b>Ans :</b>
<ul>
<li>The depth of B >= the depth of A<br>
min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further.
<li>It reduces overfitting<br>
min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further. As the tree grows no of nodes increases.
<li>The training error of B <= the training error of A<br>
min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further. As the tree grows no of nodes increases. With more nodes and deeper tree , it tends to memorize training data and variance of the model increases.
</ul>
<hr>

<h3>OOB Error</h3>
<p>Select all that apply with regards to OOB or Out of Bag Error. (More than one option may be correct)</p>
<b>Ans :</b>
<ul>
<li>All the data points in the training set are considered while calculating the OOB error.<br>
All the observations of the training set are used to calculate the OOB error.
<li>Each data point in the training set is considered only for some of the trees in the random forest while calculating OOB error.<br>
Each data point is considered to calculate OOB error, but for each of the points, only the trees which didn't have that data point in their bootstrap sample will be considered to calculate the OOB error.
</ul>
<hr>

<h3>Feature Importance in Random Forests</h3>
<p>How do you calculate feature importance in random forests for a particular attribute?</p>
<b>Ans :</b>We take an attribute and check all the trees it was present in and take the average values of the change in the homogeneity on this attribute split. This average value of change in the homogeneity gives us the feature importance of that attribute.
<b>Explaination :</b>Recall that we take all the trees that attribute was present in and aggregate the homogeneity measures to calculate feature importance. We basically select all the trees the attribute was present in and calculate the ΔHomogeneity on the attribute split. We then take an average of all of these ΔHomogeneity to arrive at the final feature importance.
<hr>