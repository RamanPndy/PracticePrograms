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

Principal Component Analysis (PCA) is a technique used to reduce the dimensionality of a dataset while retaining as much variance as possible. It’s widely used in data analysis, particularly in machine learning, for feature reduction and visualization of high-dimensional data.

### **Steps to Apply PCA in Python:**

Here’s an example of how to apply PCA using **scikit-learn** and **Pandas** for dimensionality reduction on a dataset.

### **1. Import Required Libraries**

```python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
```

### **2. Example Dataset**
Let’s use a simple dataset from **Pandas** for demonstration purposes:

```python
# Example data
data = pd.DataFrame({
    'height': [5.5, 6.1, 5.8, 5.7, 6.0, 5.9, 5.6],
    'weight': [150, 180, 160, 165, 175, 170, 155],
    'age': [22, 25, 23, 24, 26, 25, 23]
})
```

### **3. Standardize the Data**
PCA is sensitive to the scales of the data, so it's important to standardize the features by subtracting the mean and scaling to unit variance.

```python
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
```

### **4. Apply PCA**
Now, let’s reduce the data to two components using PCA.

```python
# Initialize PCA
pca = PCA(n_components=2)

# Apply PCA to the scaled data
pca_result = pca.fit_transform(scaled_data)

# Create a DataFrame with the PCA results
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
print(pca_df)
```

### **5. Explained Variance Ratio**
PCA allows you to check how much variance each principal component explains.

```python
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
```

This output shows how much of the variance is captured by each principal component. For instance, if `PC1` captures 80% of the variance and `PC2` captures 15%, you know that these two components represent 95% of the original data’s variance.

### **6. Visualizing PCA**
Finally, you can visualize the reduced dimensions in a 2D plot:

```python
# Plot the first two principal components
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_df['PC1'], y=pca_df['PC2'], s=100, color='blue', marker='o')
plt.title('PCA of Height, Weight, and Age')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()
```

### **7. Interpreting PCA Output**
- **PC1 and PC2** represent the first and second principal components.
- The **explained variance ratio** tells you how much of the original variance is explained by each component.

### **PCA on a Real Dataset (Iris Dataset)**

For a more realistic example, you can apply PCA on the **Iris dataset** to reduce its four features to two:

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualize the 2D PCA components
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='viridis', s=100)
plt.title('PCA on Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
```

### **Key Points to Remember:**
- PCA transforms the original data into a set of orthogonal components.
- These components are ordered by the amount of variance they explain from the original data.
- You can use PCA for dimensionality reduction, making it easier to visualize and analyze the data.
- **Scaling** is important when applying PCA since it’s sensitive to the variances of the features.

### **References**:
1. **Scikit-learn Documentation on PCA**: [PCA in Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
2. **PCA Tutorial on Towards Data Science**: [PCA in Python](https://towardsdatascience.com/principal-component-analysis-in-python-9d20e746a100)

This provides a comprehensive overview of how to apply PCA in Python for dimensionality reduction and feature analysis.

Using Principal Component Analysis (PCA) for model building typically involves reducing the dimensionality of a dataset while retaining the essential features that explain the variance in the data. This is especially useful when dealing with datasets that have many features, as PCA can improve model performance and reduce overfitting by removing noisy or redundant features.

### **Steps to Build a Model Using PCA:**

Here’s an example of using PCA followed by a classification model (like Logistic Regression) on the **Iris dataset** in Python:

### **1. Import Required Libraries**

```python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
```

### **2. Load the Dataset**

For this example, we’ll use the **Iris dataset**, which is built into **scikit-learn**.

```python
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels
```

### **3. Standardize the Data**

PCA is sensitive to the scales of the features, so it’s important to standardize the data (mean=0, variance=1) before applying PCA.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### **4. Apply PCA for Dimensionality Reduction**

Now, apply PCA to reduce the data to 2 components for visualization and model building.

```python
# Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualize the PCA components
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='viridis', s=100)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
```

### **5. Split the Data into Training and Test Sets**

You need to split the dataset into a training set and a test set for model evaluation.

```python
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.3, random_state=42)
```

### **6. Build a Classification Model**

Let’s use **Logistic Regression** as the classification model.

```python
# Build a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)
```

### **7. Evaluate the Model**

After training the model, you can make predictions on the test set and evaluate the model's performance.

```python
# Make predictions
y_pred = model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
```

### **8. Visualize the Results**

You can visualize the decision boundaries of the classifier using the PCA components.

```python
# Create a mesh grid for plotting decision boundaries
h = .02
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict using the trained model
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundaries
plt.contourf(xx, yy, Z, alpha=0.8)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='viridis', s=100, edgecolor='k')
plt.title('Logistic Regression - Decision Boundaries after PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
```

### **Key Points:**

- **PCA** reduces the dataset to 2 principal components for easier visualization and model building.
- **Standardization** is important because PCA is sensitive to the variance in each feature.
- After applying PCA, the reduced dimensions (here, two components) are used to train a **Logistic Regression** model.
- The **accuracy score** is computed to evaluate the model's performance.
- **Visualization** helps to interpret how the data is distributed in the reduced feature space and how the model's decision boundary looks.

### **Model Performance Consideration:**
If you reduce the dimensionality too much (e.g., reducing the number of components too far), you might lose important information from the original features. It's crucial to balance between the number of components kept and the model's ability to generalize.

### **References:**
1. **Scikit-learn PCA Documentation**: [Principal Component Analysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
2. **PCA Tutorial on Towards Data Science**: [Applying PCA for Model Building](https://towardsdatascience.com/pca-in-python-using-scikit-learn-cb2cb6b12568)

This process provides an efficient way to use PCA for dimensionality reduction followed by training a classification model.