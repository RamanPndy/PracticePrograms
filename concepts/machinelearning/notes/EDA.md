### **1. What is EDA?**
EDA is the process of analyzing data sets to summarize their main characteristics, often with visual methods. It’s a crucial first step in any machine learning pipeline to understand the data structure, detect outliers, and uncover relationships between variables.

### **2. Steps in EDA**

1. **Data Collection & Loading**: 
   - Import the data using libraries like `pandas` (Python) or `data.table` (R).
   - Verify that the data is loaded correctly with a quick overview (e.g., `.head()` and `.info()` in pandas).

2. **Data Cleaning**:
   - **Check for missing values**: Use `.isnull().sum()` to identify columns with missing data.
   - **Handle missing values**: Options include filling with mean/median/mode, forward/backward filling, or dropping rows/columns.
   - **Detect duplicates**: Use `.duplicated()` to find duplicates, and remove if necessary.
   - **Standardize formats**: Ensure consistency in categorical data and date formats.

3. **Data Profiling**:
   - **Data types**: Check data types (`.dtypes`) and convert where necessary (e.g., `int` to `float` or `object` to `category`).
   - **Summary statistics**: `.describe()` gives statistics like mean, median, min, and max, which help to understand variable distributions.

### **3. Univariate Analysis**
   - **Numeric Data**:
     - Use histograms or box plots to understand distributions, skewness, and outliers.
     - Look at summary statistics (mean, median, variance) to understand central tendency and spread.
   - **Categorical Data**:
     - Use bar plots or count plots to visualize the frequency of categories.
     - Consider frequency tables for a quantitative view.

### **4. Bivariate Analysis**
   - **Numeric vs. Numeric**: Use scatter plots to identify relationships or correlations.
     - Check for linear or non-linear relationships, clusters, or potential outliers.
     - Calculate correlation coefficients (e.g., Pearson, Spearman) to quantify relationships.
   - **Numeric vs. Categorical**: Use box plots or violin plots to see distribution of numerical values within each category.
   - **Categorical vs. Categorical**: Use cross-tabulations and stacked bar plots to observe relationships between categories.

### **5. Multivariate Analysis**
   - **Heatmaps**: Visualize correlations between multiple numeric variables.
   - **Pairplots**: Show pairwise relationships between multiple numeric variables.
   - **PCA (Principal Component Analysis)**: Reduces dimensionality and helps visualize high-dimensional data.
   - **Clustering**: Cluster analysis (e.g., k-means) can reveal natural groupings in the data.

### **6. Outlier Detection**
   - **Box Plot**: Helps visualize outliers in numerical data.
   - **Z-score and IQR**:
     - Z-score: Values with an absolute Z-score > 3 are typically considered outliers.
     - IQR (Interquartile Range): Outliers are values outside \(Q1 - 1.5 \times IQR\) and \(Q3 + 1.5 \times IQR\).
   - **Domain knowledge**: Sometimes, outliers can only be identified with specific knowledge about the data context.

### **7. Feature Engineering**
   - **Encoding Categorical Variables**: Use one-hot encoding for nominal variables and label encoding for ordinal variables.
   - **Binning**: Convert continuous variables into categories (e.g., age groups).
   - **Feature Transformation**: Apply transformations (e.g., log, square root) to normalize skewed data.
   - **Interaction Features**: Create new features based on the interaction of existing ones (e.g., combining “age” and “income”).

### **8. Data Scaling and Normalization**
   - **Standardization**: Scale features to have a mean of 0 and standard deviation of 1.
   - **Normalization**: Scale features to a range (often [0, 1]) using min-max scaling.
   - **When to Use**:
     - Use standardization for algorithms sensitive to feature magnitudes (e.g., SVM, k-means).
     - Normalization is useful when features have different ranges, especially in neural networks.

### **9. Dimensionality Reduction**
   - **PCA**: Reduces dimensionality while preserving variance, useful for visualization or speeding up models.
   - **t-SNE**: Helps visualize high-dimensional data in 2D or 3D spaces, commonly used for clustering.

### **10. EDA Tools**
   - **Libraries**:
     - **Python**: `pandas`, `matplotlib`, `seaborn`, `plotly`, `scipy`, `statsmodels`
     - **R**: `dplyr`, `ggplot2`, `data.table`
   - **Automated EDA**: Libraries like `Pandas Profiling`, `Sweetviz`, or `D-Tale` can generate detailed reports automatically.

### **11. Common Visualizations**
   - **Histograms**: Distribution of numerical data.
   - **Box Plots**: Outlier detection and distribution overview.
   - **Scatter Plots**: Bivariate relationships for numeric variables.
   - **Heatmaps**: Correlations or frequency counts.
   - **Pair Plots**: Relationships across multiple features.

### **12. Key EDA Checks**
   - **Data Balance**: Check for class imbalance in target variables, especially in classification tasks.
   - **Feature Correlation**: Highly correlated features may indicate redundancy; consider feature selection or dimensionality reduction.
   - **Feature Variability**: Features with little variation may be less informative for modeling.

---

### **Tips for EDA in Exams**
1. **Understand Key Concepts**: Focus on interpreting different visualizations, correlation, and handling outliers and missing values.
2. **Memorize Common Commands**: Practice basic pandas commands and common visualizations.
3. **Feature Engineering**: Know when to apply transformations, encoding, and scaling.
4. **Practice Interpreting Plots**: Be able to read and draw conclusions from histograms, scatter plots, and correlation matrices.

---

Exploratory Data Analysis (EDA) with pandas is an essential step in understanding and preparing your dataset for further analysis or modeling. Here’s a set of notes summarizing key pandas techniques for EDA:

---

### **1. Loading and Inspecting Data**
- **Load data:**
  ```python
  import pandas as pd
  df = pd.read_csv("file.csv")  # or pd.read_excel(), pd.read_sql(), etc.
  ```
- **Preview data:**
  ```python
  df.head()  # First 5 rows
  df.tail()  # Last 5 rows
  ```
- **Data information:**
  ```python
  df.info()  # Column types, non-null counts
  df.describe()  # Statistical summary for numeric columns
  df.shape  # Rows and columns count
  df.columns  # List of column names
  ```

---

### **2. Handling Missing Data**
- **Check missing values:**
  ```python
  df.isnull().sum()  # Count of missing values per column
  ```
- **Fill missing values:**
  ```python
  df['col'].fillna(value, inplace=True)  # Replace NaN with a value
  ```
- **Drop rows or columns:**
  ```python
  df.dropna(inplace=True)  # Drop rows with NaN
  df.dropna(axis=1, inplace=True)  # Drop columns with NaN
  ```

---

### **3. Understanding Data Types**
- **Check data types:**
  ```python
  df.dtypes
  ```
- **Convert data types:**
  ```python
  df['col'] = df['col'].astype('int')  # Convert to integer
  ```

---

### **4. Summarizing and Aggregating Data**
- **Basic statistics:**
  ```python
  df['col'].mean()
  df['col'].median()
  df['col'].std()
  ```
- **Count values:**
  ```python
  df['col'].value_counts()
  ```
- **Group by operations:**
  ```python
  df.groupby('col1')['col2'].mean()
  ```

---

### **5. Handling Duplicates**
- **Check duplicates:**
  ```python
  df.duplicated().sum()
  ```
- **Remove duplicates:**
  ```python
  df.drop_duplicates(inplace=True)
  ```

---

### **6. Data Visualization with pandas**
- **Histograms:**
  ```python
  df['col'].hist()
  ```
- **Scatter plots:**
  ```python
  df.plot.scatter(x='col1', y='col2')
  ```
- **Box plots:**
  ```python
  df.boxplot(column=['col'])
  ```

---

### **7. Feature Engineering**
- **Create new columns:**
  ```python
  df['new_col'] = df['col1'] + df['col2']
  ```
- **Apply functions:**
  ```python
  df['col'] = df['col'].apply(lambda x: x * 2)
  ```

---

### **8. Correlation and Relationships**
- **Compute correlations:**
  ```python
  df.corr()  # Correlation matrix
  ```
- **Visualize correlations:**
  ```python
  import seaborn as sns
  sns.heatmap(df.corr(), annot=True)
  ```

---

### **9. Pivot Tables**
- **Create pivot tables:**
  ```python
  df.pivot_table(values='col', index='col1', columns='col2', aggfunc='mean')
  ```

---

### **10. Data Sampling**
- **Random sampling:**
  ```python
  df.sample(frac=0.1)  # 10% of the data
  ```

---

### **11. Saving Processed Data**
- **Export to file:**
  ```python
  df.to_csv("processed_data.csv", index=False)
  df.to_excel("processed_data.xlsx", index=False)
  ```