<p>highest correlation</p>
<b>Ans :</b>
<code>ij_max = np.unravel_index(corrmat_diag_zero.argmax(), corrmat_diag_zero.shape)
print("ij_max",ij_max)</code><br>
<hr>

Here are some concise notes on using pandas for machine learning (ML) exam preparation, covering essential operations and techniques.

---

### **1. Introduction to Pandas**
- **Pandas** is a Python library for data manipulation and analysis, built on top of NumPy.
- The primary data structures are:
  - **Series**: 1-dimensional labeled array.
  - **DataFrame**: 2-dimensional labeled data structure (similar to a table in SQL or Excel spreadsheet).

### **2. Creating DataFrames**
- **From Dictionary**:
  ```python
  import pandas as pd
  data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
  df = pd.DataFrame(data)
  ```
- **From CSV File**:
  ```python
  df = pd.read_csv('filename.csv')
  ```
- **From NumPy Array**:
  ```python
  import numpy as np
  data = np.array([[1, 2], [3, 4]])
  df = pd.DataFrame(data, columns=['A', 'B'])
  ```

### **3. Basic Data Exploration**
- **Head and Tail**:
  ```python
  df.head()  # First 5 rows
  df.tail()  # Last 5 rows
  ```
- **Info and Describe**:
  ```python
  df.info()        # Overview of the data, including types and nulls
  df.describe()    # Statistical summary of numerical columns
  ```
- **Shape and Columns**:
  ```python
  df.shape         # (rows, columns)
  df.columns       # List of column names
  ```

### **4. Selecting Data**
- **Selecting Columns**:
  ```python
  df['column_name']          # Single column as a Series
  df[['col1', 'col2']]       # Multiple columns as a DataFrame
  ```
- **Selecting Rows**:
  ```python
  df.iloc[0]                 # First row by index
  df.loc[df['column'] > 5]   # Rows based on condition
  ```
- **Slicing**:
  ```python
  df.iloc[0:5, 0:2]          # Slicing rows and columns
  df.loc[0:5, ['col1', 'col2']]
  ```

### **5. Data Cleaning**
- **Handling Missing Data**:
  ```python
  df.isnull().sum()          # Count missing values per column
  df.dropna()                # Drop rows with any missing values
  df.fillna(value)           # Fill missing values with specified value
  ```
- **Replacing Values**:
  ```python
  df['col'] = df['col'].replace(old_value, new_value)
  ```
- **Removing Duplicates**:
  ```python
  df.drop_duplicates()
  ```

### **6. Data Transformation**
- **Creating New Columns**:
  ```python
  df['new_col'] = df['col1'] + df['col2']
  ```
- **Applying Functions**:
  ```python
  df['col'] = df['col'].apply(lambda x: x * 2)
  df['col'] = df['col'].map({'A': 1, 'B': 2})  # Mapping values
  ```
- **Binning**:
  ```python
  df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['Child', 'Young', 'Adult', 'Senior'])
  ```

### **7. Grouping and Aggregation**
- **GroupBy**:
  ```python
  grouped = df.groupby('col')
  grouped.mean()            # Aggregate mean for each group
  ```
- **Aggregate Multiple Functions**:
  ```python
  df.groupby('col').agg({'col1': 'sum', 'col2': 'mean'})
  ```
- **Pivot Table**:
  ```python
  df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='mean')
  ```

### **8. Merging and Joining**
- **Concatenate**: Combine DataFrames along rows or columns.
  ```python
  pd.concat([df1, df2], axis=0)  # Row-wise
  ```
- **Merge**: SQL-like join on columns.
  ```python
  pd.merge(df1, df2, on='key', how='inner')
  ```
- **Join**: Combine DataFrames by index.
  ```python
  df1.join(df2, on='key')
  ```

### **9. Data Aggregation**
- **Summarizing Data**:
  ```python
  df['col'].sum()
  df['col'].mean()
  df['col'].max()
  df['col'].min()
  ```
- **Crosstab**:
  ```python
  pd.crosstab(df['col1'], df['col2'])
  ```

### **10. Reshaping Data**
- **Melt**: Convert wide data into long format.
  ```python
  pd.melt(df, id_vars=['id'], value_vars=['var1', 'var2'])
  ```
- **Pivot**: Convert long data into wide format.
  ```python
  df.pivot(index='id', columns='variable', values='value')
  ```

### **11. Time Series Analysis**
- **Date Parsing**:
  ```python
  df['date'] = pd.to_datetime(df['date'])
  ```
- **Setting Date as Index**:
  ```python
  df.set_index('date', inplace=True)
  ```
- **Resampling**:
  ```python
  df.resample('M').mean()  # Monthly average
  ```

### **12. Essential DataFrame Operations**
- **Sorting**:
  ```python
  df.sort_values(by='col', ascending=False)
  ```
- **Renaming Columns**:
  ```python
  df.rename(columns={'old_name': 'new_name'})
  ```
- **Dropping Columns or Rows**:
  ```python
  df.drop(['col1', 'col2'], axis=1)  # Drop columns
  df.drop([0, 1], axis=0)            # Drop rows
  ```

### **13. Data Scaling**
- **Standardization**:
  ```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  df[['col1', 'col2']] = scaler.fit_transform(df[['col1', 'col2']])
  ```
- **Normalization**:
  ```python
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  df[['col1', 'col2']] = scaler.fit_transform(df[['col1', 'col2']])
  ```

### **14. Encoding Categorical Variables**
- **One-Hot Encoding**:
  ```python
  pd.get_dummies(df, columns=['category_column'])
  ```
- **Label Encoding**:
  ```python
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  df['category_column'] = le.fit_transform(df['category_column'])
  ```

### **15. EDA & Visualization with Pandas**
- **Basic Plots** (using Matplotlib or Seaborn):
  ```python
  df['column'].hist()                # Histogram
  df.plot(kind='box')                 # Boxplot
  df.plot(kind='scatter', x='col1', y='col2')  # Scatter plot
  ```

### **16. Useful Pandas Tips for Exams**
- **Check Data Types Quickly**:
  ```python
  df.dtypes
  ```
- **Value Counts**:
  ```python
  df['col'].value_counts()
  ```
- **Memory Usage**:
  ```python
  df.memory_usage(deep=True)
  ```
- **Copying Data**:
  ```python
  df_copy = df.copy()
  ```

### **17. Pandas and Machine Learning Workflow**
- **Data Splitting**:
  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```
- **Pandas + Sklearn Pipeline**:
  - Combine `pandas` data preprocessing with `scikit-learn` pipelines for streamlined ML workflows.

---
Pandas is a powerful library for data manipulation and analysis in Python. For machine learning, it is often used for preprocessing and exploratory data analysis (EDA). Below are some important Pandas functions categorized by their purpose:

---

### **1. Data Loading**
- **`pd.read_csv()`**: Load CSV files into a DataFrame.
- **`pd.read_excel()`**: Read Excel files.
- **`pd.read_sql()`**: Load data from an SQL query or database.
- **`pd.read_json()`**: Load JSON data.

---

### **2. Data Exploration**
- **`df.head(n)`**: View the first `n` rows of a DataFrame.
- **`df.tail(n)`**: View the last `n` rows of a DataFrame.
- **`df.info()`**: Get a summary of the DataFrame, including data types and non-null counts.
- **`df.describe()`**: Get statistical summaries for numerical columns.
- **`df.shape`**: Get the dimensions of the DataFrame (rows, columns).
- **`df.columns`**: List all column names.
- **`df.isnull().sum()`**: Check the number of missing values in each column.

---

### **3. Data Cleaning**
- **`df.drop(columns=[...])`**: Drop specific columns.
- **`df.dropna()`**: Remove rows with missing values.
- **`df.fillna(value)`**: Fill missing values with a specified value.
- **`df.duplicated()`**: Check for duplicate rows.
- **`df.drop_duplicates()`**: Remove duplicate rows.
- **`df.replace(old_value, new_value)`**: Replace specific values.

---

### **4. Data Transformation**
- **`df['column'] = df['column'].astype(type)`**: Convert data types.
- **`pd.get_dummies(df['column'])`**: Perform one-hot encoding for categorical columns.
- **`df.apply(func, axis=0 or 1)`**: Apply a function across rows or columns.
- **`df.rename(columns={'old_name': 'new_name'})`**: Rename columns.

---

### **5. Feature Engineering**
- **`df['new_column'] = df['col1'] + df['col2']`**: Create new features by combining columns.
- **`pd.cut(df['column'], bins)`**: Bin numerical data into intervals.
- **`pd.qcut(df['column'], q)`**: Bin data into quantiles.
- **`df.groupby('column').mean()`**: Group data and compute aggregate functions.

---

### **6. Indexing and Filtering**
- **`df.loc[]`**: Access rows/columns by labels.
- **`df.iloc[]`**: Access rows/columns by integer indices.
- **`df[df['column'] > value]`**: Filter rows based on a condition.
- **`df.set_index('column')`**: Set a column as the DataFrame index.
- **`df.reset_index()`**: Reset the index.

---

### **7. Statistical Analysis**
- **`df.corr()`**: Compute the correlation matrix.
- **`df.cov()`**: Compute covariance.
- **`df.value_counts()`**: Count unique values in a column.
- **`df.pivot_table()`**: Create pivot tables for aggregation.

---

### **8. Handling Dates**
- **`pd.to_datetime(df['column'])`**: Convert a column to datetime format.
- **`df['column'].dt.year`**, **`.month`**, **`.day`**: Extract date components.
- **`df['column'].dt.strftime(format)`**: Format dates.

---

### **9. Data Export**
- **`df.to_csv('file.csv')`**: Save a DataFrame to a CSV file.
- **`df.to_excel('file.xlsx')`**: Save a DataFrame to an Excel file.
- **`df.to_sql('table', connection)`**: Write data to a SQL database.

---

### **10. Visualization with Pandas**
- **`df.plot()`**: Basic plots of data.
- **`df.hist()`**: Plot histograms of columns.
- **`df.boxplot()`**: Create boxplots.

---

### **Common Machine Learning Use Cases**
1. **Data Preprocessing:**
   - Handle missing values (`fillna`, `dropna`).
   - Encode categorical variables (`get_dummies`, `replace`).
   - Scale features (integrate with libraries like `sklearn`).

2. **Feature Selection:**
   - Use `corr()` to analyze relationships between features.
   - Remove irrelevant features (`drop`).

3. **Train-Test Split:**
   - Pandas often works alongside `sklearn` for splitting datasets into train/test sets.

---