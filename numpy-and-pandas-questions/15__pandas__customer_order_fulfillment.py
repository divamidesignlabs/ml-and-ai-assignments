"""
Exercise 05: Customer Order and Fulfillment Analysis

Real-world scenario: Analyze customer orders to understand fulfillment performance, 
order patterns, and customer satisfaction metrics.

Task:
1. Create DataFrame with customer orders and fulfillment data
2. Merge customer and order information
3. Calculate fulfillment metrics (on-time, complete orders)
4. Analyze order patterns by customer segment
5. Identify at-risk and high-value customers
6. Generate customer performance and recommendations
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create customer data
customers = pd.DataFrame({
    'Customer_ID': [f'CUST-{i:04d}' for i in range(1, 31)],
    'Customer_Name': [f'Company {i}' for i in range(1, 31)],
    'Segment': np.random.choice(['Retail', 'Wholesale', 'Enterprise'], 30),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 30),
    'Join_Date': [datetime(2022, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(30)],
    'Annual_Spend': np.random.uniform(10000, 500000, 30)
})

# Create orders data
np.random.seed(42)
num_orders = 200
orders = pd.DataFrame({
    'Order_ID': [f'ORD-{i:06d}' for i in range(1, num_orders + 1)],
    'Customer_ID': np.random.choice(customers['Customer_ID'], num_orders),
    'Order_Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_orders)],
    'Order_Amount': np.random.uniform(500, 50000, num_orders),
    'Required_Delivery_Date': None,
    'Actual_Delivery_Date': None,
    'Order_Status': np.random.choice(['Fulfilled', 'Partial', 'Not Fulfilled'], num_orders),
    'Fulfillment_Rate': np.random.uniform(0.7, 1.0, num_orders)
})

# Set delivery dates
for idx, row in orders.iterrows():
    required = row['Order_Date'] + timedelta(days=np.random.randint(5, 15))
    orders.at[idx, 'Required_Delivery_Date'] = required
    
    if row['Order_Status'] == 'Fulfilled':
        offset = np.random.randint(-5, 3)
    elif row['Order_Status'] == 'Partial':
        offset = np.random.randint(3, 10)
    else:
        offset = np.random.randint(10, 20)
    
    orders.at[idx, 'Actual_Delivery_Date'] = required + timedelta(days=offset)

print("Customer Order and Fulfillment Analysis")
print("\n" + "="*80)

print("\nCustomer Base Overview:")
print(customers.head(10))
print(f"\nTotal Customers: {len(customers)}")

print("\n\nOrders Sample:")
print(orders.head(10))
print(f"\nTotal Orders: {len(orders)}")

print("\n" + "="*80)

# Task 1: Merge customer and order data
# TODO: Merge customer and order data using appropriate join
print("\nMerging Customer and Order Data...")
customer_orders = None  # FILL IN

# Task 2: Calculate fulfillment metrics
# TODO: Analyze on-time delivery, fulfillment rates
print("\n\nFulfillment Performance Analysis:")
print("TODO: Calculate fulfillment metrics")

# Task 3: Customer segmentation
# TODO: Segment customers by order value or frequency
print("\n\nCustomer Segmentation:")
print("TODO: Segment customers")

# Task 4: High-value customer analysis
# TODO: Identify and analyze top customers
print("\n\nHigh-Value Customer Analysis:")
print("TODO: Analyze top customers")

# Task 5: Order fulfillment trends
# TODO: Analyze trends in fulfillment over time
print("\n\nFulfillment Trends:")
print("TODO: Analyze trends")

# Task 6: At-risk customer identification
# TODO: Find customers with low fulfillment rates
print("\n\nAt-Risk Customers:")
print("TODO: Identify at-risk customers")
customer_orders['Days_Late'] = (customer_orders['Actual_Delivery_Date'] - customer_orders['Required_Delivery_Date']).dt.days
customer_orders['On_Time'] = customer_orders['Days_Late'] <= 0

on_time_orders = customer_orders['On_Time'].sum()
total_orders = len(customer_orders)
on_time_rate = (on_time_orders / total_orders) * 100

print(f"Overall On-Time Delivery Rate: {on_time_rate:.1f}%")
print(f"Orders On-Time: {on_time_orders} out of {total_orders}")
print(f"Orders Late: {total_orders - on_time_orders}")

# Complete fulfillment
complete_orders = (customer_orders['Order_Status'] == 'Fulfilled').sum()
partial_orders = (customer_orders['Order_Status'] == 'Partial').sum()
unfulfilled = (customer_orders['Order_Status'] == 'Not Fulfilled').sum()

print(f"\nOrder Fulfillment Status:")
print(f"  Fully Fulfilled: {complete_orders} ({complete_orders/total_orders*100:.1f}%)")
print(f"  Partially Fulfilled: {partial_orders} ({partial_orders/total_orders*100:.1f}%)")
print(f"  Not Fulfilled: {unfulfilled} ({unfulfilled/total_orders*100:.1f}%)")

# Average fulfillment rate
avg_fulfillment = customer_orders['Fulfillment_Rate'].mean()
print(f"  Average Fulfillment Rate: {avg_fulfillment*100:.1f}%")

# Task 3: Analyze by customer segment
print("\n\nFulfillment Performance by Customer Segment:")
segment_metrics = customer_orders.groupby('Segment').agg({
    'Order_ID': 'count',
    'On_Time': lambda x: (x.sum() / len(x) * 100),
    'Order_Amount': 'sum',
    'Fulfillment_Rate': 'mean'
}).round(2)
segment_metrics.columns = ['Order_Count', 'On_Time_%', 'Total_Spend', 'Avg_Fulfill_Rate']
print(segment_metrics)

# Task 4: Customer-level analysis
print("\n\nCustomer Performance Summary:")
customer_performance = customer_orders.groupby('Customer_ID').agg({
    'Order_ID': 'count',
    'Order_Amount': ['sum', 'mean'],
    'On_Time': lambda x: (x.sum() / len(x) * 100),
    'Fulfillment_Rate': 'mean',
    'Days_Late': 'mean'
}).round(2)

customer_performance.columns = ['Order_Count', 'Total_Spend', 'Avg_Order', 'On_Time_%', 'Avg_Fulfill', 'Avg_Days_Late']
customer_performance = customer_performance.merge(customers[['Customer_ID', 'Customer_Name', 'Segment']], 
                                                   left_index=True, right_on='Customer_ID')

print("\nTop 10 Customers by Spend:")
top_customers = customer_performance.nlargest(10, 'Total_Spend')[
    ['Customer_Name', 'Segment', 'Order_Count', 'Total_Spend', 'On_Time_%', 'Avg_Fulfill']
]
print(top_customers)

# Task 5: Identify at-risk customers
print("\n\nAt-Risk Customers Identification:")

# At-risk: Low on-time rate and low fulfillment
at_risk = customer_performance[
    (customer_performance['On_Time_%'] < 70) | (customer_performance['Avg_Fulfill'] < 0.8)
]

if len(at_risk) > 0:
    print(f"Found {len(at_risk)} at-risk customers:")
    print(at_risk[['Customer_Name', 'Total_Spend', 'On_Time_%', 'Avg_Fulfill']].head(10))
else:
    print("No critical at-risk customers identified")

# Task 6: High-value customer focus
print("\n\nHigh-Value Customer Analysis:")
high_value = customer_performance[customer_performance['Total_Spend'] > customer_performance['Total_Spend'].quantile(0.75)]
print(f"High-value customers (Top 25% by spend): {len(high_value)}")
print(f"Combined spend: ${high_value['Total_Spend'].sum():,.0f}")
print(f"Average on-time rate: {high_value['On_Time_%'].mean():.1f}%")
print(f"Average fulfillment rate: {high_value['Avg_Fulfill'].mean():.1f}%")

# Task 7: Regional analysis
print("\n\nPerformance by Region:")
regional_metrics = customer_orders.groupby('Region').agg({
    'Order_ID': 'count',
    'On_Time': lambda x: (x.sum() / len(x) * 100),
    'Order_Amount': 'sum',
    'Days_Late': 'mean'
}).round(2)
regional_metrics.columns = ['Orders', 'On_Time_%', 'Total_Spend', 'Avg_Days_Late']
print(regional_metrics)

# Task 8: Delivery performance trends
print("\n\nDelivery Performance Timeline:")
customer_orders['Month'] = customer_orders['Order_Date'].dt.to_period('M')
monthly_performance = customer_orders.groupby('Month').agg({
    'Order_ID': 'count',
    'On_Time': lambda x: (x.sum() / len(x) * 100),
    'Days_Late': 'mean'
}).round(2)
monthly_performance.columns = ['Orders', 'On_Time_%', 'Avg_Days_Late']
print(monthly_performance)

# Task 9: Generate recommendations
print("\n\n" + "="*80)
print("\nRecommendations:")

print("\n1. Segment-Specific Actions:")
for segment in segment_metrics.index:
    on_time = segment_metrics.loc[segment, 'On_Time_%']
    if on_time < 75:
        print(f"   • {segment}: ON-TIME RATE LOW ({on_time:.1f}%) - Improve fulfillment")
    else:
        print(f"   • {segment}: On-time rate satisfactory ({on_time:.1f}%)")

print("\n2. High-Value Customer Retention:")
print(f"   • Prioritize fulfillment for top {len(high_value)} customers")
print(f"   • Implement dedicated customer success managers")
print(f"   • Target on-time rate of 95%+ for these accounts")

if len(at_risk) > 0:
    print("\n3. At-Risk Customer Recovery:")
    for idx, customer in at_risk.head(5).iterrows():
        print(f"   • {customer['Customer_Name']}: "
              f"On-time {customer['On_Time_%']:.1f}%, Fulfill {customer['Avg_Fulfill']:.1f}%")
    print("   • Create recovery plan with service improvements")

print("\n4. Regional Optimization:")
worst_region = regional_metrics['On_Time_%'].idxmin()
print(f"   • Focus on {worst_region} region (On-time: {regional_metrics.loc[worst_region, 'On_Time_%']:.1f}%)")
print("   • Audit warehouse and logistics operations")

print("\n5. Product/Service Expansion:")
print("   • Offer to expand services to high-performing customers")
print("   • Bundle products for wholesale/enterprise segments")
print("   • Create loyalty program for repeat customers")
