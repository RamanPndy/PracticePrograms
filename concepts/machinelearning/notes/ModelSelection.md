<h3>Model Variance</h3>
<p>How do you measure the variance of a model?</p>
<b>Ans :</b>By measuring how much does the estimates of the model change on the test data on changing the training data<br>
<b>Explaination :</b>Variance measures the extent of change in a model with respect to the training data.
<hr>

<h3>Regularization</h3>
<p>What is regularization?</p>
<b>Ans :</b>It is a technique that is used to strike a balance between model complexity and model accuracy on training data.<br>
<b>Explaination :</b>Regularization does not improve accuracy; it improves the balance between accuracy and complexity.
<hr>

<h3>Simple Models</h3>
<p>Which of the following is incorrect with respect to creating simpler models?</p>
<b>Ans :</b>Simpler models will always have fewer test errors than a complex model.<br>
<b>Explaination :</b>Complex models, assuming that you have enough training data available, can do a quite accurate job of prediction.
<hr>
<p>Which of the following is correct with respect to creating simpler models?</p>
<b>Ans :</b>
<ul>
<li>Simpler models are more generic.
<li>Simpler models require less training data.
</ul>
<hr>

<h3>Simplicity of a model</h3>
<p>How would you quantify the simplicity of a model?</p>
<b>Ans :</b>
<ul>
<li>By the number of features used in the model<br>
If you use more features in your model, it would become more complex and might even overfit with the given data. An overfitted model is not simple enough for prediction purposes.
</li>
<li>By the number of nodes and depth of trees in case of a tree model<br>
The number of nodes and tree depth determine the complexity of a decision tree. If a decision tree has a higher number of features, it will have more nodes and, hence, will be more complicated.</li>
</ul>
<hr>

<h3>k-fold Cross Validation</h3>
<p>Which of the following statements is correct with respect to k-fold cross validation?</p>
<b>Ans :</b>As k increases, the training time for k-fold cross validation increases.<br>
<b>Explaination :</b>A high k means that the training runs for a higher number of times, leading to a high training time.
<hr>
<p>Which of the following about k-fold cross validation is not true?</p>
<b>Ans :</b>
<ul>
<li>You repeat the process k-1 times.<br>
With k-fold cross validation, training happens k times while each sample is used as validation data at least once.
<li>A model trained with k-fold cross validation will never overfit.<br>
Overfitting is possible with cross validation. Cross-validation does not prevent overfitting by itself, but it may help in identifying a case of overfitting.
</ul>
<hr>
<p>Which of the following about k-fold cross validation are true?</p>
<b>Ans :</b>
<ul>
<li>You repeat the cross validation process ‘k’ times.
<li>Each ‘kth’ fold is used as the validation data once.
</ul>
<hr>