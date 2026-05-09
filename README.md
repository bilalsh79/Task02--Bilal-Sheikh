# Task02--Bilal-Sheikh
# Project 2: Exploratory Data Analysis (EDA) & Visualization

## 📌 Project Overview
This project represents the **Discovery Phase** of the data analytics lifecycle. Building on the foundation of Project 1, I utilized Python to perform a deep-dive Exploratory Data Analysis (EDA) on the cleaned e-commerce dataset.

The goal of this project was to move beyond raw numbers and identify business-critical trends, seasonal patterns, and revenue drivers through statistical analysis and high-impact data visualizations.

## 📊 Core Analysis Features
The analysis script (`Project 2.py`) provides a comprehensive overview of business health through four distinct analytical lenses:

1.  **Descriptive Statistics:** Comprehensive breakdown of central tendency and dispersion (Mean, Median, Standard Deviation) for `TotalPrice`, `Quantity`, and `UnitPrice`.
2.  **Distribution Profiling:** Identifying the "shape" of the business by visualizing order value frequency.
3.  **Revenue Attribution:** Categorical analysis to determine which products act as the primary revenue engines.
4.  **Time-Series Analysis:** Tracking monthly order volume to identify peak seasons and growth trends.
5.  **Anomaly Detection:** Implementing the **Interquartile Range (IQR)** method to mathematically identify and isolate revenue outliers.

## 🛠️ Tools & Technologies
* **Python 3.x**
* **Pandas:** For statistical aggregation and time-series manipulation.
* **Matplotlib & Seaborn:** For designing professional, publication-quality visualizations.

## 📈 Visual Insights
The following visualizations were generated to provide actionable intelligence:

### 1. Revenue Distribution
* **Observation:** Visualized the frequency of order totals to understand common transaction sizes.
* **Insight:** Helped identify whether the business relies on high-volume small purchases or low-volume high-ticket items.

### 2. Product Performance
* **Observation:** Ranked products by total revenue contribution.
* **Insight:** Directly identifies top-selling products vs. underperformers to guide inventory and marketing focus.

### 3. Order Volume Trends
* **Observation:** A monthly line chart tracking order counts over time.
* **Insight:** Essential for identifying seasonality and measuring the success of long-term marketing efforts.

## 🔍 Statistical Outlier Analysis
Beyond visual trends, I applied a rigorous mathematical approach to identify anomalies:
* Calculated **Q1 (25th percentile)** and **Q3 (75th percentile)**.
* Used the **IQR (Interquartile Range)** to set upper and lower bounds.
* Successfully isolated high-value "Outlier" orders that significantly impact total revenue figures.

## 🚀 How to Run
1. Ensure the cleaned dataset from Project 1 (`Cleaned_Dataset.xlsx`) is in the directory.
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
