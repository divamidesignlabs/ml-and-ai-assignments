"""
Exercise 04: Multi-Location Purchase Order Analysis

Real-world scenario: Analyze purchase orders across multiple distribution centers 
to identify procurement patterns, consolidate orders, and optimize purchasing.

Task:
1. Create DataFrames for orders and suppliers from multiple locations
2. Merge order and supplier data
3. Aggregate orders by location and supplier
4. Identify consolidation opportunities
5. Analyze order frequency and patterns
6. Recommend procurement strategy optimizations
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create purchase orders data
np.random.seed(42)
num_orders = 100

orders = pd.DataFrame({
    'Order_ID': [f'PO-{i:05d}' for i in range(1, num_orders + 1)],
    'Order_Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_orders)],
    'Location': np.random.choice(['NYC', 'LA', 'Chicago', 'Dallas', 'Atlanta'], num_orders),
    'Supplier_ID': np.random.choice(['SUP-001', 'SUP-002', 'SUP-003', 'SUP-004'], num_orders),
    'Product': np.random.choice(['Electronics', 'Hardware', 'Packaging', 'Raw Materials'], num_orders),
    'Quantity': np.random.randint(50, 1000, num_orders),
    'Unit_Price': np.random.uniform(10, 500, num_orders),
    'Order_Status': np.random.choice(['Completed', 'Pending', 'Cancelled'], num_orders, p=[0.7, 0.2, 0.1])
})

# Calculate order value
orders['Order_Value'] = orders['Quantity'] * orders['Unit_Price']

# Create supplier data
suppliers = pd.DataFrame({
    'Supplier_ID': ['SUP-001', 'SUP-002', 'SUP-003', 'SUP-004'],
    'Supplier_Name': ['Global Electronics', 'Tech Components', 'Industrial Supply', 'Premium Parts Co'],
    'Country': ['China', 'Taiwan', 'USA', 'Germany'],
    'Lead_Time_Days': [14, 10, 3, 21],
    'Min_Order_Qty': [100, 50, 25, 200],
    'Quality_Rating': [4.2, 4.5, 4.0, 4.8]
})

# Create location info
locations = pd.DataFrame({
    'Location': ['NYC', 'LA', 'Chicago', 'Dallas', 'Atlanta'],
    'Region': ['Northeast', 'West', 'Midwest', 'South', 'Southeast'],
    'Annual_Budget': [500000, 450000, 400000, 350000, 300000]
})

print("Multi-Location Purchase Order Analysis")
print("\n" + "="*80)
print("\nOrders Data Sample:")
print(orders.head(10))

print(f"\nOrders Dataset: {orders.shape[0]} orders across {orders['Location'].nunique()} locations")
print(f"Date Range: {orders['Order_Date'].min().date()} to {orders['Order_Date'].max().date()}")

print("\n\nSuppliers Data:")
print(suppliers)

print("\n\nLocation Information:")
print(locations)

print("\n" + "="*80)

# Task 1: Merge orders with supplier and location data
# TODO: Use merge() to combine data from multiple sources
print("\nMerging Data Sources...")
orders_merged = None  # FILL IN: Merge orders, suppliers, and locations

# Task 2: Aggregate orders by location
# TODO: Group by location and calculate summary statistics
print("\n\nOrders Analysis by Location:")
location_summary = None  # FILL IN
print(location_summary)

# Task 3: Analyze orders by supplier
# TODO: Group by supplier and calculate metrics
print("\n\nOrders Analysis by Supplier:")
supplier_summary = None  # FILL IN
print(supplier_summary)

# Task 4: Identify consolidation opportunities
# TODO: Find location-supplier combinations with fragmentation
print("\n\nOrder Consolidation Analysis:")
location_supplier = None  # FILL IN

print("\nTop 10 Location-Supplier Combinations by Spend:")
top_combinations = None  # FILL IN
print(top_combinations)

# Task 5: Analyze order frequency and patterns
print("\n\n" + "="*80)
print("\nOrder Frequency Analysis:")
monthly_orders = None  # FILL IN
print(monthly_orders)

# Analyze order status
print("\n\nOrder Status Distribution:")
status_dist = None  # FILL IN
print(status_dist)

# Task 6: Product analysis by location
print("\n\nProduct Analysis by Location:")
print("TODO: Complete product analysis")
print("\n\nProduct Distribution Across Locations:")
product_location = orders_merged.pivot_table(
    values='Order_Value',
    index='Product',
    columns='Location',
    aggfunc='sum',
    fill_value=0
).round(2)
print(product_location)

# Task 7: Lead time impact analysis
print("\n\n" + "="*80)
print("\nSupplier Lead Time Impact:")

orders_with_lead = orders_merged[['Supplier_Name', 'Lead_Time_Days', 'Order_Value']].drop_duplicates(
    subset=['Supplier_Name']
)
orders_with_lead = orders_with_lead.sort_values('Lead_Time_Days')
print(orders_with_lead)

# Task 8: Budget utilization
print("\n\nBudget Utilization by Location:")
budget_util = orders_merged.groupby('Location').agg({
    'Order_Value': 'sum',
    'Annual_Budget': 'first'
}).round(2)
budget_util['Utilization_%'] = (budget_util['Order_Value'] / budget_util['Annual_Budget'] * 100).round(1)
budget_util.columns = ['YTD_Spend', 'Annual_Budget', 'Utilization_%']
print(budget_util)

# Task 9: Recommendations
print("\n\n" + "="*80)
print("\nProcurement Optimization Recommendations:")

print("\n1. Supplier Consolidation:")
print(f"   • Consolidate {len(location_supplier[location_supplier['Orders'] > 3])} fragmented location-supplier pairs")
print(f"   • Focus on top 2-3 suppliers per location")
best_suppliers = supplier_summary.nlargest(3, 'Total_Spend')
for supplier in best_suppliers.index:
    print(f"     - {supplier}")

print("\n2. Bulk Ordering Strategy:")
print("   • Increase order sizes by 20-30% to reduce per-unit costs")
print("   • Establish quarterly purchase agreements for stable products")
print("   • Negotiate volume discounts with top suppliers")

print("\n3. Lead Time Optimization:")
shortest_lead = supplier_summary['Lead_Time'].idxmin()
longest_lead = supplier_summary['Lead_Time'].idxmax()
print(f"   • Increase orders from {shortest_lead} (Lead time: {supplier_summary.loc[shortest_lead, 'Lead_Time']:.0f} days)")
print(f"   • Reduce reliance on {longest_lead} (Lead time: {supplier_summary.loc[longest_lead, 'Lead_Time']:.0f} days)")

print("\n4. Quality Focus:")
high_quality = supplier_summary[supplier_summary['Quality_Rating'] >= 4.5]
if len(high_quality) > 0:
    print(f"   • Prioritize suppliers with quality rating ≥4.5:")
    for supplier in high_quality.index:
        print(f"     - {supplier}: {supplier_summary.loc[supplier, 'Quality_Rating']:.1f}")

print("\n5. Location-Specific Actions:")
for loc in location_summary.index:
    spend = location_summary.loc[loc, 'Total_Spend']
    budget = locations[locations['Location'] == loc]['Annual_Budget'].values[0]
    util = spend / budget * 100
    print(f"   • {loc}: ${spend:,.0f} ({util:.1f}% of budget)")
