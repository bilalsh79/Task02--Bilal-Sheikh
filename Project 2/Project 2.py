import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Loads the dataset from an Excel file."""
    try:
        df = pd.read_excel(filepath, sheet_name='Sheet1')
        print("Data successfully loaded. Shape:", df.shape)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def calculate_basic_statistics(df):
    """Calculates and prints basic descriptive statistics."""
    print("\n--- BASIC STATISTICS ---")
    numeric_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']
    stats = df[numeric_cols].describe().T
    # Selecting count, mean, median (50%), min, max, and standard deviation
    print(stats[['count', 'mean', '50%', 'min', 'max', 'std']].round(2))

def plot_distributions_and_trends(df):
    """Generates visualizations for distributions and trends."""
    sns.set_theme(style="whitegrid")

    # 1. Distribution of Total Price
    plt.figure(figsize=(10, 6))
    sns.histplot(df['TotalPrice'], bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Total Price per Order', fontsize=14)
    plt.xlabel('Total Price ($)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('total_price_dist.png')
    plt.show()

    # 2. Total Revenue by Product
    plt.figure(figsize=(10, 6))
    product_sales = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
    sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
    plt.title('Total Revenue by Product', fontsize=14)
    plt.xlabel('Product')
    plt.ylabel('Total Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('revenue_by_product.png')
    plt.show()

    # 3. Monthly Order Volume Trend
    df['Month_Year'] = df['Date'].dt.to_period('M')
    monthly_orders = df.groupby('Month_Year')['OrderID'].count()
    
    plt.figure(figsize=(12, 6))
    monthly_orders.plot(kind='line', marker='o', color='coral', linewidth=2)
    plt.title('Monthly Order Volume Trend', fontsize=14)
    plt.xlabel('Month-Year')
    plt.ylabel('Number of Orders')
    plt.tight_layout()
    plt.savefig('monthly_trend.png')
    plt.show()

def identify_outliers(df, column):
    """Identifies outliers using the Interquartile Range (IQR) method."""
    print(f"\n--- OUTLIER ANALYSIS ({column}) ---")
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Identified {len(outliers)} outliers.")
    if not outliers.empty:
        print(f"Highest outlier value: ${outliers[column].max():.2f}")

def main():
    filepath = 'Cleaned_Dataset.xlsx'
    df = load_data(filepath)
    
    if df is not None:
        calculate_basic_statistics(df)
        plot_distributions_and_trends(df)
        identify_outliers(df, 'TotalPrice')

        # Additional Categorical Insight
        print("\n--- CATEGORICAL INSIGHTS ---")
        print("Top 3 Referral Sources:\n", df['ReferralSource'].value_counts().head(3))
        print("\nOrder Status Breakdown:\n", df['OrderStatus'].value_counts())

if __name__ == "__main__":
    main()