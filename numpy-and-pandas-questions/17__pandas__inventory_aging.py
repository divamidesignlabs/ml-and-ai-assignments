"""
Exercise 07: Inventory Aging and Obsolescence Analysis

Real-world scenario: Identify slow-moving and obsolete inventory items to 
reduce carrying costs and prevent write-offs.

Task:
1. Create inventory data with aging information
2. Classify items by age and movement rate
3. Calculate holding costs and obsolescence risk
4. Identify slow-movers and dead stock
5. Recommend disposition strategies
6. Calculate potential cost avoidance
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create inventory data
np.random.seed(42)
num_items = 100

inventory = pd.DataFrame({
    'SKU': [f'SKU-{i:05d}' for i in range(1, num_items + 1)],
    'Product_Name': [f'Product {chr(65 + i%26)}{i//26}' for i in range(num_items)],
    'Category': np.random.choice(['Electronics', 'Hardware', 'Packaging', 'Tools'], num_items),
    'Units_In_Stock': np.random.randint(10, 1000, num_items),
    'Unit_Cost': np.random.uniform(5, 500, num_items),
    'Last_Receipt_Date': [datetime.now() - timedelta(days=np.random.randint(10, 730)) for _ in range(num_items)],
    'Last_Sale_Date': [datetime.now() - timedelta(days=np.random.randint(5, 720)) for _ in range(num_items)],
    'Units_Sold_YTD': np.random.randint(0, 2000, num_items),
    'Monthly_Demand': np.random.randint(0, 500, num_items)
})

# Calculate aging metrics
today = datetime.now()
inventory['Days_Since_Receipt'] = (today - inventory['Last_Receipt_Date']).dt.days
inventory['Days_Since_Last_Sale'] = (today - inventory['Last_Sale_Date']).dt.days
inventory['Total_Value'] = inventory['Units_In_Stock'] * inventory['Unit_Cost']
inventory['Daily_Carrying_Cost'] = inventory['Total_Value'] * 0.001  # 0.1% daily
inventory['Annual_Carrying_Cost'] = inventory['Daily_Carrying_Cost'] * 365

print("Inventory Aging and Obsolescence Analysis")
print("\n" + "="*80)

print("\nInventory Data Sample:")
print(inventory.head(10))

print(f"\nTotal Inventory Items: {len(inventory)}")
print(f"Total Inventory Value: ${inventory['Total_Value'].sum():,.0f}")
print(f"Total Annual Carrying Cost: ${inventory['Annual_Carrying_Cost'].sum():,.0f}")

print("\n" + "="*80)

# Task 1: Classify inventory by age
print("\nInventory Classification by Age:")

# Classification rules based on days since last sale
# TODO: Create a function to classify items by age and apply it to inventory
inventory['Age_Classification'] = None  # FILL IN

print("\nItems by Age Classification:")
print("TODO: Display classification summary")

# Task 2: Identify slow-moving inventory
print("\n\n" + "="*80)
print("\nSlow-Moving and Dead Stock Items:")

# TODO: Filter for slow-moving and dead stock items
slow_movers = None  # FILL IN

print("TODO: Display slow-moving inventory analysis")

# Task 3: Calculate obsolescence risk
print("\n\n" + "="*80)
print("\nObsolescence Risk Assessment:")

# TODO: Create function to calculate obsolescence risk score
inventory['Obsolescence_Risk_Score'] = None  # FILL IN
inventory['Risk_Category'] = None  # FILL IN

print("\nRisk Distribution:")
print("TODO: Display risk category summary")

# Task 4: Detailed analysis of critical items
print("\n\n" + "="*80)
print("\nCritical Obsolescence Risk Items:")

# TODO: Filter and display critical risk items
critical_items = None  # FILL IN

print("TODO: Display critical items analysis")

# Task 5: Recommend disposition strategies
print("\n\n" + "="*80)
print("\nRecommended Disposition Strategies:")

# TODO: Categorize items by risk and recommend disposition actions
clearance = None  # FILL IN
redistribute = None  # FILL IN
remanufacture = None  # FILL IN
scrap = None  # FILL IN

print("TODO: Recommend disposition strategies by risk level")

# Task 6: Financial impact analysis
print("\n\n" + "="*80)
print("\nFinancial Impact Analysis:")

# TODO: Calculate financial benefits of action plan
annual_carrying_saved = None  # FILL IN
write_off_avoidance = None  # FILL IN

print("TODO: Calculate and display financial impact")
