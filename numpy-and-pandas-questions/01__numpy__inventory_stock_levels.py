"""
Exercise 01: Inventory Stock Level Analysis

Real-world scenario: A warehouse manager needs to analyze stock levels across 
multiple distribution centers. Calculate statistics on inventory and identify 
low-stock items that need replenishment.

Task:
1. Create a 2D NumPy array representing stock levels for 5 products across 4 distribution centers
2. Calculate total stock per product (sum across centers)
3. Calculate average stock per distribution center (mean across products)
4. Find the minimum and maximum stock levels overall
5. Create a boolean mask to identify products with stock below 20 units
6. Use the mask to get the indices of low-stock products
"""

import numpy as np

# TODO: Create a 2D array (5 products x 4 distribution centers)
# Sample data: warehouse_stock = np.array([[...], [...], ...])
# Each row represents a product, each column represents a distribution center
warehouse_stock = None  # FILL IN: Create 2D array of stock levels

print("Warehouse Stock Levels (Products x Distribution Centers):")
print(warehouse_stock)
print("\n" + "="*60)

# Task 1: Calculate total stock per product
# TODO: Use np.sum() along appropriate axis
total_per_product = None  # FILL IN
print("\nTotal stock per product:")
print(total_per_product)

# Task 2: Calculate average stock per distribution center
# TODO: Use np.mean() along appropriate axis
avg_per_center = None  # FILL IN
print("\nAverage stock per distribution center:")
print(avg_per_center)

# Task 3: Find minimum and maximum stock levels
# TODO: Use np.min() and np.max()
min_stock = None  # FILL IN
max_stock = None  # FILL IN
print(f"\nMinimum stock level: {min_stock}")
print(f"Maximum stock level: {max_stock}")

# Task 4: Create boolean mask for low-stock items (< 20 units)
# TODO: Use boolean indexing
low_stock_mask = None  # FILL IN
print("\nBoolean mask for low-stock locations (< 20):")
print(low_stock_mask)

# Task 5: Get indices of products with any low stock
# TODO: Use np.where() or find which products have any True in their row
low_stock_product_indices = None  # FILL IN
print(f"\nProduct indices with low stock: {low_stock_product_indices}")
if low_stock_product_indices is not None:
    print(f"Products needing replenishment: {['Product ' + chr(65+i) for i in low_stock_product_indices]}")

# Bonus: Calculate reorder quantity for low-stock products
# Assume target inventory is 80 units per distribution center
target_per_center = 80
reorder_quantities = None  # FILL IN: target_per_center * 4 - total_per_product
reorder_needed = None  # FILL IN
print(f"\nReorder quantities for low-stock products: {reorder_needed}")
