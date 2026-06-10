import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("zara_sales.csv")

# Dataset Information
print(df.info())

# Display First 5 Rows
print(df.head())

# Statistical Summary
print(df.describe())

# Check Missing Values
print(df.isnull().sum())

# List All Columns
print(df.columns.tolist())


# Sales Volume Distribution
plt.figure(figsize=(8,5))
plt.hist(df['Sales Volume'], bins=20)
plt.title('Sales Volume Distribution')
plt.xlabel('Sales Volume')
plt.ylabel('Frequency')
plt.show()

# Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df['price'], bins=20)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Product Position Analysis
df['Product Position'].value_counts().plot(kind='bar')
plt.title('Products by Position')
plt.xlabel('Position')
plt.ylabel('Count')
plt.show()

# Promotion vs Sales Volume
sns.boxplot(x='Promotion', y='Sales Volume', data=df)
plt.title('Promotion vs Sales Volume')
plt.show()

# Seasonal Product Analysis
sns.boxplot(
    x='Seasonal',
    y='Sales Volume',
    data=df
)

plt.title('Seasonal vs Sales Volume')
plt.show()

# Category Wise Sales
df.groupby('Product Category')['Sales Volume'] \
    .sum() \
    .plot(kind='bar')

plt.title('Sales by Category')
plt.show()

# Section Revenue Analysis
df.groupby('section')['Revenue_Estimate'] \
    .sum() \
    .plot(kind='bar')

plt.title('Revenue by Section')
plt.show()

# Correlation Heatmap
sns.heatmap(df[['Sales Volume', 'price']].corr(),
            annot=True,
            cmap='Blues')
plt.show()

# Price vs Sales Scatter Plot
sns.scatterplot(
    x='price',
    y='Sales Volume',
    hue='Promotion',
    data=df
)

plt.title('Price vs Sales')
plt.show()

# Top Product Terms
df['terms'].value_counts().head(10) \
    .plot(kind='bar')

plt.title('Top Product Terms')
plt.show()
















