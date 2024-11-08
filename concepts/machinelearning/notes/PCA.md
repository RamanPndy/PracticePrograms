<p>Which of the following preprocessing steps is the most crucial before performing PCA?
<b>Ans :</b>Standardisation of data
<b>Explaination :</b>If variables are on a different scale (e.g. fractions and millions), then PCA (while trying to maximise the variance) will give higher importance to the variables with high variance simply because of scale. For example, if you change one variable from km to cm (increasing its variance), it may go from having little impact to dominating the first.
<hr>


<h3>Change in Basis</h3>

![Alt text](images/change-in-basis.png)
<b>Ans :</b>

![Alt text](images/change-in-basis-ans.png)
<hr>

<h3>Find the new representation</h3>

![Alt text](images/repr.png)
<b>Ans :</b>

![Alt text](images/repr-ans.png)
<hr>

<h3>PCA - Properties</h3>
<p>Consider the following statements<br>

Statement 1 - PCA helps in solving the multicollinearity problem by creating new uncorrelated features which are used as input for the predictive model.<br>

Statement 2 - With a dimensionality reduction technique like PCA, you convert a dataset having N dimensions to another dataset having k dimensions where N > k.<br>

Now choose the correct option.<br>
</p>
<b>Ans :</b>Both the statements are correct<br>
<b>Explaination :</b>PCA does create uncorrelated features which solve the problem of multicollinearity. PCA also reduces the number of dimensions from N to k (or N > k )
<hr>