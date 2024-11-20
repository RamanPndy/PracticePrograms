Feature extraction for a linear regression model involves selecting, transforming, or engineering features (independent variables) from raw data to improve the model's performance. Here's how you can approach it:

---

### 1. **Understanding Feature Extraction**
   - Feature extraction is about transforming raw data into meaningful inputs for the model.
   - This includes selecting relevant features, creating new features, or reducing the dimensionality of features.

---

### 2. **Steps for Feature Extraction**

#### A. **Handle Categorical Variables**
   - Convert non-numeric data into numeric form using:
     - **One-Hot Encoding**: Create binary columns for each category.
     - **Label Encoding**: Assign integers to categories.
   - Example:
     ```python
     import pandas as pd
     data = pd.DataFrame({'Category': ['A', 'B', 'A', 'C']})
     encoded = pd.get_dummies(data['Category'], prefix='Category')
     print(encoded)
     ```

#### B. **Feature Scaling**
   - Normalize or standardize numerical features to bring them to a similar scale.
   - Techniques:
     - **Min-Max Scaling**: Scale values between 0 and 1.
     - **Standardization**: Center data around 0 with a unit standard deviation.
   - Example:
     ```python
     from sklearn.preprocessing import StandardScaler
     scaler = StandardScaler()
     scaled_features = scaler.fit_transform([[10], [20], [30]])
     ```

#### C. **Polynomial Features**
   - Create interaction terms or higher-degree features to capture non-linear relationships.
   - Example:
     ```python
     from sklearn.preprocessing import PolynomialFeatures
     poly = PolynomialFeatures(degree=2, include_bias=False)
     X_poly = poly.fit_transform([[2], [3]])
     print(X_poly)  # Output includes squared terms
     ```

#### D. **Dimensionality Reduction**
   - Techniques like PCA (Principal Component Analysis) reduce feature dimensions while preserving variance.
   - Example:
     ```python
     from sklearn.decomposition import PCA
     pca = PCA(n_components=2)
     X_reduced = pca.fit_transform([[2, 3], [3, 4], [4, 5]])
     ```

#### E. **Extract Domain-Specific Features**
   - Create new features based on domain knowledge.
   - Example: For housing price prediction, extract features like "Price per Square Foot" or "Age of House".

---

### 3. **Automated Feature Selection**
- Use statistical or algorithmic techniques to choose relevant features:
  - **Variance Threshold**: Remove low-variance features.
  - **Correlation Matrix**: Remove highly correlated features.
  - **Recursive Feature Elimination (RFE)**: Use an estimator to rank features.
  - Example:
    ```python
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    rfe = RFE(model, n_features_to_select=2)
    rfe.fit(X, y)
    print(rfe.support_)  # Features selected
    ```

---

### 4. **Example Workflow**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression

# Step 1: Load Data
data = pd.DataFrame({
    'Feature1': [1, 2, 3, 4],
    'Feature2': [5, 6, 7, 8],
    'Target': [10, 15, 20, 25]
})

# Step 2: Split Data
X = data[['Feature1', 'Feature2']]
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 3: Apply Polynomial Features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled = scaler.transform(X_test_poly)

# Step 5: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Step 6: Evaluate Model
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
```

---

### 5. **Summary**
Feature extraction enhances the model by:
- Improving interpretability.
- Reducing noise and redundancy.
- Capturing non-linear or interaction effects.

Choose techniques that align with your dataset and problem domain for the best performance.