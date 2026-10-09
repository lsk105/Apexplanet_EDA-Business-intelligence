from statistics import correlation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# descriptive statistics & univariate analysis
df=pd.read_csv("ApexPlanet_dataanalytics.csv")
print(df.head())
print(df.shape)
print(df.info())
# numerical columns
numeric_cols = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

print(df[numeric_cols].describe())
# interpret the statistics
# age
print("Average Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())
print("Minimum Age:", df["Age"].min())
print("Maximum Age:", df["Age"].max())

# sales statistics
print("Average Sales: ",df["Total_Sales"].mean())
print("Median Sales:",df["Total_Sales"].median())
print("Minimum Sales:",df["Total_Sales"].min())
print("Maximum Sales:",df["Total_Sales"].max())
# categorical analysis
print(df["Gender"].value_counts())
print(df["Category"].value_counts())
print(df["Product"].value_counts())

# Gender bar chart
df["Gender"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Customer Transactions by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.show()

# Category bar chart
category_counts = df["Category"].value_counts()

category_counts.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Transactions by Product Category")
plt.xlabel("Category")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#product distribution
product_counts = df["Product"].value_counts()

product_counts.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Transactions by Product")
plt.xlabel("Product")
plt.ylabel("Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# histogram -- age
plt.figure(figsize=(8,5))

plt.hist(
    df["Age"],
    bins=10
)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# histogram --total sales
plt.figure(figsize=(8,5))

plt.hist(
    df["Total_Sales"],
    bins=20
)

plt.title("Total Sales Distribution")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# step _3 multivariate analysis & correlation

numeric_cols = ["Age","Quantity","Unit_Price","Total_Sales"]
correlation= df[numeric_cols].corr()
print(correlation)
# then visualize it
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# quantity vs Total sales
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x="Quantity",y= "Total_Sales",)
plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# category vs gender
category_gender = pd.crosstab(
    df["Category"],
    df["Gender"]
)

print(category_gender)

category_gender.plot(
    kind="bar",
    figsize=(10,6)
)

plt.title("Category Transactions by Gender")
plt.xlabel("Category")
plt.ylabel("Order_id")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# pair plot
sns.pairplot(
    df[
        [
            "Age",
            "Quantity",
            "Unit_Price",
            "Total_Sales"
        ]
    ]
)

plt.show()








