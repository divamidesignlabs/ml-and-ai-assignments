"""
Exercise 01: Supply Chain Transaction Analysis

Real-world scenario: Analyze supply chain transactions including purchases, 
shipments, and deliveries. Create a comprehensive transaction ledger with 
Pandas for tracking and analysis.

Task:
1. Create a DataFrame with transaction data (date, vendor, product, quantity, cost)
2. Calculate transaction statistics by vendor
3. Filter transactions by date range and product category
4. Group transactions by month and calculate totals
5. Create transaction summaries and identify patterns
6. Generate reports for different stakeholders
"""

import pandas as pd
import numpy as np

# Create transaction data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
transactions = pd.DataFrame({
    'Date': np.random.choice(dates, 100),
    'Vendor': np.random.choice(['Supplier-A', 'Supplier-B', 'Supplier-C', 'Supplier-D'], 100),
    'Product': np.random.choice(['Electronics', 'Raw Materials', 'Packaging', 'Tools'], 100),
    'Quantity': np.random.randint(10, 500, 100),
    'Unit_Cost': np.random.uniform(5, 200, 100),
    'Status': np.random.choice(['Ordered', 'Shipped', 'Delivered', 'Pending'], 100)
})

# Calculate total cost per transaction
transactions['Total_Cost'] = transactions['Quantity'] * transactions['Unit_Cost']

# Sort by date
transactions = transactions.sort_values('Date').reset_index(drop=True)

print("Supply Chain Transaction Analysis")
print("\n" + "="*80)
print("\nFirst 10 Transactions:")
print(transactions.head(10))

print(f"\nDataFrame Shape: {transactions.shape}")
print("\nData Types:")
print(transactions.dtypes)

print("\n" + "="*80)

# Task 1: Calculate transaction statistics by vendor
# TODO: Use groupby() with agg() to summarize by vendor
print("\nVendor Summary Statistics:")
vendor_stats = None  # FILL IN
print(vendor_stats)

# Task 2: Analyze transactions by product
# TODO: Group by Product and calculate spending metrics
print("\n\nProduct Category Analysis:")
product_stats = None  # FILL IN
print(product_stats)

# Task 3: Filter transactions by status
# TODO: Use value_counts() to show status distribution
print("\n\nTransaction Status Distribution:")
status_counts = None  # FILL IN
print(status_counts)

# Analyze pending transactions (potential delays)
pending_transactions = None  # FILL IN
print(f"\nPending Transactions: {len(pending_transactions) if pending_transactions is not None else 0}")

# Task 4: Group by month and calculate totals
# TODO: Extract year-month and aggregate by period
transactions['YearMonth'] = transactions['Date'].dt.to_period('M')
monthly_summary = None  # FILL IN
print("\n\nMonthly Summary:")
print(monthly_summary)

# Task 5: Vendor-Product cross-analysis
# TODO: Use pivot_table() to create vendor-product spending matrix
print("\n\nVendor-Product Spending Matrix:")
vendor_product = None  # FILL IN
print(vendor_product)

# Task 6: Identify top transactions
# TODO: Use nlargest() to find highest value transactions
print("\n\nTop 5 Largest Transactions:")
top_transactions = None  # FILL IN
print(top_transactions)

print("\n\nRecommendations:")
print("1. Review pending transactions for potential delays")
print("2. Consolidate vendor relationships to reduce fragmentation")
print("3. Negotiate bulk discounts with top vendors")
print("4. Monitor high-value transactions for cost optimization")
