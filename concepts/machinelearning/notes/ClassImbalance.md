Class imbalance occurs when one class in a dataset significantly outnumbers other classes. For example, in a binary classification problem, if 90% of samples belong to class `0` and only 10% belong to class `1`, the model may become biased toward predicting the majority class. To handle this, techniques such as resampling, using algorithms robust to imbalance, and adjusting evaluation metrics can be applied.

---

Identifying class imbalance in a dataset is a crucial step in machine learning, especially for classification problems. Here's how you can detect it:

---

### **1. Visual Inspection**
Use visualizations to quickly understand the distribution of classes:
- **Bar Plot**: A simple way to compare the frequency of each class.
  ```python
  import pandas as pd
  import matplotlib.pyplot as plt

  # Example: Checking class distribution
  df = pd.DataFrame({'Target': [0, 0, 0, 1, 1, 0, 0, 1, 1, 0]})
  df['Target'].value_counts().plot(kind='bar')
  plt.title("Class Distribution")
  plt.xlabel("Class")
  plt.ylabel("Frequency")
  plt.show()
  ```

---

### **2. Statistical Summary**
- **Class Counts**:
  Compute the count of samples in each class using `value_counts()` in Pandas or `Counter` from the collections module.
  ```python
  from collections import Counter

  # Example dataset
  y = [0, 0, 0, 0, 1, 1, 0, 0, 1, 1]
  print(Counter(y))
  ```
- **Class Ratios**:
  Calculate the proportion of each class relative to the total dataset size.
  ```python
  # Class ratio calculation
  class_ratios = df['Target'].value_counts(normalize=True)
  print(class_ratios)
  ```

---

### **3. Imbalance Metrics**
- **Imbalance Ratio (IR)**:
  \[
  \text{IR} = \frac{\text{Majority Class Size}}{\text{Minority Class Size}}
  \]
  A high imbalance ratio indicates a significant imbalance.
  ```python
  majority_class = max(Counter(y).values())
  minority_class = min(Counter(y).values())
  imbalance_ratio = majority_class / minority_class
  print("Imbalance Ratio:", imbalance_ratio)
  ```

---

### **4. Using Visualization Libraries**
- **Seaborn Count Plot**:
  ```python
  import seaborn as sns

  sns.countplot(x='Target', data=df)
  plt.title("Class Distribution")
  plt.show()
  ```

- **Pie Chart** (Optional):
  ```python
  df['Target'].value_counts().plot(kind='pie', autopct='%1.1f%%')
  plt.title("Class Distribution")
  plt.show()
  ```

---

### **5. Automatic Detection in Scikit-Learn**
Some libraries offer utilities to detect imbalance directly:
- **Scikit-Learn `make_classification`** (for simulated datasets):
  The `weights` parameter can simulate imbalances.
  ```python
  from sklearn.datasets import make_classification

  X, y = make_classification(n_samples=1000, weights=[0.9, 0.1])
  print(Counter(y))
  ```

---

### **6. Red Flags for Imbalance**
- Majority class constitutes more than 80% of the data (or other thresholds based on domain knowledge).
- Evaluation metrics like accuracy are misleadingly high.

---

### **Example: Handling Class Imbalance with Scikit-Learn**

#### Dataset Simulation
We simulate a dataset with an imbalanced target class.

```python
from sklearn.datasets import make_classification
import pandas as pd
from collections import Counter

# Create imbalanced dataset
X, y = make_classification(n_classes=2, class_sep=2, 
                           weights=[0.9, 0.1], n_informative=3, n_redundant=1,
                           flip_y=0, n_features=5, n_clusters_per_class=1,
                           n_samples=1000, random_state=42)

# Check class distribution
print("Class Distribution:", Counter(y))

# Convert to DataFrame for inspection
df = pd.DataFrame(X, columns=[f'Feature_{i}' for i in range(X.shape[1])])
df['Target'] = y
print(df.head())
```

---

#### **1. Resampling Methods**
##### **a. Oversampling the Minority Class**
Using **SMOTE (Synthetic Minority Oversampling Technique)**.

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
print("Resampled Class Distribution:", Counter(y_resampled))
```

##### **b. Undersampling the Majority Class**
Removing some majority class samples.

```python
from imblearn.under_sampling import RandomUnderSampler

undersampler = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = undersampler.fit_resample(X, y)
print("Resampled Class Distribution:", Counter(y_resampled))
```

---

#### **2. Algorithm-Level Techniques**
##### **a. Class Weights**
Specify class weights in models like Logistic Regression or Random Forest to penalize misclassification of minority classes.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression with class weights
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
```

---

#### **3. Evaluation Metrics**
Use metrics that account for class imbalance, such as:
- **Precision, Recall, and F1-Score**: Focus on minority class performance.
- **ROC-AUC Curve**: Evaluates model performance across all thresholds.

```python
from sklearn.metrics import roc_auc_score

# Example ROC-AUC score
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
print("ROC-AUC Score:", roc_auc)
```

---

### **When to Use These Techniques**
1. **Resampling**: When the dataset is small.
2. **Class Weights**: For large datasets where resampling is computationally expensive.
3. **Evaluation Metrics**: Always evaluate with metrics robust to imbalance to avoid misleading accuracy.

---