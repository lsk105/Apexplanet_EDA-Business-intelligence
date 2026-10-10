# ApexPlanet Internship – Task 2: Exploratory Data Analysis & Business Intelligence

## 📌 Project Overview

This project is part of my Data Analytics Internship at ApexPlanet. The objective is to explore sales data, identify meaningful patterns and trends, answer business questions using SQL, perform multivariate analysis, and design a static dashboard mock-up to communicate business insights.

The project demonstrates a practical data analytics workflow, from exploring a dataset to translating analytical findings into business-oriented information.

## 🎯 Objectives

* Perform descriptive statistics and Exploratory Data Analysis (EDA).
* Analyze numerical and categorical variables.
* Answer business questions using Microsoft SQL Server.
* Explore relationships and correlations between numerical variables.
* Identify sales trends and product/category performance.
* Design a static dashboard mock-up with key performance indicators (KPIs).
* Improve data interpretation and business storytelling skills.

## 🛠️ Tools & Technologies

* **Python** – Data analysis and exploration
* **Pandas** – Data manipulation and summarization
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization and correlation heatmaps
* **Microsoft SQL Server (SSMS)** – SQL-based business analysis
* **Microsoft Excel** – Dataset inspection and preparation
* **PowerPoint** – Static dashboard mock-up and project presentation

## 📂 Dataset Description

The project uses a sales dataset containing 1,000 transaction records and 12 original columns.

| Column        | Description               |
| ------------- | ------------------------- |
| Order_ID      | Order identifier          |
| Order_Date    | Date of transaction       |
| Customer_ID   | Customer identifier       |
| Customer_Name | Customer name             |
| Age           | Customer age              |
| Gender        | Customer gender           |
| City          | Customer city             |
| Product       | Product purchased         |
| Category      | Product category          |
| Quantity      | Number of units purchased |
| Unit_Price    | Price per unit            |
| Total_Sales   | Total sales amount        |

## 📊 Project Workflow

### 1. Descriptive Statistics

Analyzed numerical variables such as Age, Quantity, Unit_Price, and Total_Sales.

Calculated summary statistics, including:

* Mean and median
* Minimum and maximum
* Standard deviation
* Quartiles and distribution summaries

### 2. Univariate Analysis

Explored individual variables to understand the data distribution.

Activities included:

* Histograms for numerical variables
* Bar charts for categorical variables
* Product and category transaction counts
* Customer distribution by gender and city
* Identification of frequently occurring values

### 3. SQL Business Analysis

Used Microsoft SQL Server to translate business questions into SQL queries.

Key business questions included:

1. Which products generate the highest revenue?
2. Which categories contribute the most to total sales?
3. How do sales change month by month?
4. Which cities generate the highest sales?
5. What is the average transaction value by category?
6. Which customer age groups contribute the most to sales?
7. How does revenue compare across genders?

SQL concepts used or practiced include:

* SELECT and WHERE
* GROUP BY and ORDER BY
* Aggregate functions such as SUM, COUNT, and AVG
* Filtering and sorting
* Date-based grouping
* Ranking and aggregations

### 4. Multivariate Analysis

Explored relationships between multiple numerical and categorical variables.

Analysis techniques included:

* Correlation matrix
* Correlation heatmap
* Scatter plots
* Quantity versus Total_Sales analysis
* Unit_Price versus Total_Sales analysis
* Age versus Total_Sales exploration
* Comparisons across customer groups and product categories

Correlation was interpreted as an association between variables, not proof of causation.

### 5. Business Intelligence Dashboard Mock-up

Designed a static dashboard concept to present key business metrics and sales patterns.

Proposed KPI cards:

* Total Sales
* Total order_id
* Total Units Sold
* Average Transaction Value

Proposed visualizations:

* Monthly sales trends
* Category-wise revenue
* Top-performing products
* City-wise sales
* Customer age-group analysis

The mock-up demonstrates how analytical results can be organized into a business-friendly report.

## 📈 Initial Dataset Summary

The initial dataset summary showed approximately:

| Metric                        |           Value |
| ----------------------------- | --------------: |
| Total Sales                   | ₹139.40 million |
| order_id                |           1,000 |
| Units Sold                    |           5,435 |
| Average Sales per Transaction |        ₹139.40K |
| Products                      |               6 |

*Note: These are dataset-specific summary figures. The average sales per transaction is calculated as total sales divided by the number of transaction records.*

## 💡 Key Learnings

* Performing EDA with Python and Pandas
* Understanding numerical and categorical data distributions
* Converting business questions into SQL queries
* Analyzing sales trends and product performance
* Interpreting correlations and relationships
* Selecting useful KPIs for business reporting
* Communicating analytical findings through visualizations and dashboard planning

## 📁 Suggested Repository Structure

```text
ApexPlanet-Task2-EDA-Business-Intelligence/
│
├── data/
│   └── cleaned_sales_dataset.csv
│
├── python/
│   └── task2_eda.py
│
├── sql/
│   └── business_analysis_queries.sql
│
├── visuals/
│   ├── sales_distribution.png
│   ├── category_analysis.png
│   └── correlation_heatmap.png
│
├── dashboard/
│   └── dashboard_mockup.png
│
├── reports/
│   └── ApexPlanet_Task2_EDA_Business_Intelligence.pptx
│
└── README.md
```

*The structure above is a suggested organization. Add only the files you have actually created.*

## 🚀 Conclusion

This project strengthened my understanding of the data analytics workflow by combining Python-based EDA, SQL business analysis, multivariate analysis, and dashboard design.

I will continue developing my skills in Python, SQL, Excel, Power BI, and data storytelling to solve practical business problems using data.

## 👨‍💻 Author

**Santosh Kumar Lakkoju**

Aspiring Data Analyst | Python | SQL Server | Excel | Power BI
