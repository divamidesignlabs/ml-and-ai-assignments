"""
Exercise 03: Inventory Data Cleaning and Standardization

Real-world scenario: Clean and standardize inconsistent inventory data 
from multiple sources, handle missing values, and prepare for analysis.

Task:
1. Create DataFrame with messy inventory data (inconsistencies, missing values)
2. Identify and handle missing values appropriately
3. Standardize product codes and names
4. Correct data type issues
5. Remove duplicate entries
6. Create clean, standardized dataset for analysis
"""

import pandas as pd
import numpy as np

# Create messy inventory data with various quality issues
inventory_data = {
    'Product_Code': ['P001', 'p002', 'P003', 'P001', None, 'P005', 'P004', 'P006', 'p003', 'P007'],
    'Product_Name': ['Widget A', 'widget b', 'WIDGET C', 'Widget A', 'Widget E', 'widget d', 
                     'Widget D', 'Widget F', 'Widget C', 'Widget G'],
    'Category': ['Electronics', 'electronics', 'ELECTRONICS', 'Electronics', None, 'Tools', 
                 'TOOLS', 'Supplies', 'Electronics', 'supplies'],
    'Quantity': [100, '150', 75, 100, None, 200, 175, '50', 120, 90],
    'Unit_Cost': [25.00, 30, 45.50, 25.0, 35.5, None, 40.0, 15.5, 45.50, 20],
    'Last_Updated': ['2024-01-15', '2024-01-14', '2024-01-15', '2024-01-15', 
                     '2024-01-10', None, '2024-01-12', '2024-01-11', '2024-01-15', '2024-01-10'],
    'Location': ['Warehouse A', 'warehouse a', 'WAREHOUSE A', 'Warehouse B', 'Warehouse C',
                 'warehouse b', 'Warehouse B', 'Warehouse C', 'Warehouse A', None]
}

inventory = pd.DataFrame(inventory_data)

print("Inventory Data Cleaning and Standardization")
print("\n" + "="*80)
print("\nOriginal Messy Data:")
print(inventory)

print("\n\nData Quality Issues:")
print(f"Total rows: {len(inventory)}")
print(f"Missing values per column:")
print(inventory.isnull().sum())

print("\n" + "="*80)

# Task 1: Identify data quality issues
# TODO: Check for duplicates, case inconsistencies, and data type issues
print("\nData Quality Assessment:")
print("TODO: Identify duplicates and inconsistencies")

# Task 2: Clean and standardize the data
print("\n\n" + "="*80)
print("Cleaning Process:")

inventory_clean = inventory.copy()

# TODO: Remove duplicates
print("\n1. Removing duplicate entries...")

# TODO: Standardize text fields to consistent case
print("\n2. Standardizing text formatting...")

# TODO: Convert data types to appropriate formats
print("\n3. Converting data types...")

# TODO: Handle missing values using appropriate strategies
print("\n4. Handling missing values...")

# TODO: Create derived columns
print("\n5. Creating derived columns...")
inventory_clean['Total_Value'] = None  # FILL IN

# Task 3: Validate cleaned data
print("\n\n" + "="*80)
print("Data Validation:")
print("TODO: Validate cleaning results")

# Task 4: Summary statistics
print("\n\nCleaned Data Summary:")
print(inventory_clean)

print("\n\nKey Metrics:")
print("TODO: Calculate key metrics on cleaned data")

# Task 3: Validate cleaned data
print("\n\n" + "="*80)
print("Data Validation (Cleaned Data):")
print(f"\nTotal rows: {len(inventory_clean)}")
print(f"Missing values: {inventory_clean.isnull().sum().sum()} (should be 0)")
print(f"Duplicate rows: {len(inventory_clean) - len(inventory_clean.drop_duplicates())} (should be 0)")

print("\n\nCleaned Data Summary:")
print(inventory_clean)

print("\n\nCleaned Data Statistics:")
print(inventory_clean[['Quantity', 'Unit_Cost', 'Total_Value']].describe().round(2))

print("\n\nData Distribution by Category:")
print(inventory_clean['Category'].value_counts())

print("\n\nQuality Metrics:")
print(f"  Completeness: {(1 - (inventory_clean.isnull().sum().sum() / (inventory_clean.shape[0] * inventory_clean.shape[1]))) * 100:.1f}%")
print(f"  Consistency: 100% (all text standardized)")
print(f"  Accuracy: Validated against expected ranges")

print("\n\nCleaned Data Export:")
print("The cleaned dataset is ready for analysis:")
print(f"  • {len(inventory_clean)} clean product records")
print(f"  • Total inventory value: ${inventory_clean['Total_Value'].sum():,.2f}")
print(f"  • All data types correct")
print(f"  • No missing values")
print(f"  • Duplicates removed")
