"""
Exercise 06: Inventory Turnover and ABC Analysis

Real-world scenario: Perform ABC (Pareto) analysis on inventory to classify 
products by value and identify items requiring different management strategies.

Task:
1. Create inventory data with quantities and unit values
2. Calculate total value per product (quantity × price)
3. Sort products by value and calculate cumulative percentage
4. Classify products as A (top 80% value), B (next 15%), C (remaining 5%)
5. Calculate turnover rates for each category
6. Provide inventory management recommendations by category
"""

import numpy as np

# Product inventory data
product_names = np.array([
    'Electronic Module', 'Plastic Housing', 'Motor Unit', 'Control Board',
    'Connector Cable', 'Power Supply', 'Cooling Fan', 'Sensor Array',
    'Display Panel', 'Fastener Kit', 'Thermal Paste', 'Label Sheet'
])

# Quantity in stock (units)
quantities = np.array([150, 8000, 45, 80, 2200, 120, 300, 60, 35, 15000, 500, 20000])

# Unit cost/value ($)
unit_values = np.array([250, 2, 180, 95, 5, 300, 25, 120, 200, 0.10, 3, 0.05])

num_products = len(product_names)

print("Inventory Data:")
print(f"{'Product':<20} {'Quantity':<12} {'Unit Value':<12} {'Total Value':<12}")
print("-" * 56)
for i in range(num_products):
    total = quantities[i] * unit_values[i]
    print(f"{product_names[i]:<20} {quantities[i]:<12} ${unit_values[i]:<11.2f} ${total:<11.2f}")
print("\n" + "="*60)

# Task 1: Calculate total value per product
# TODO: Use element-wise multiplication
total_values = None  # FILL IN

print("\nTotal Inventory Values:")
if total_values is not None:
    for i in range(num_products):
        print(f"  {product_names[i]}: ${total_values[i]:,.2f}")

# Task 2: Sort by value and calculate cumulative percentage
# TODO: Use np.argsort() and cumulative sum
sorted_indices = None  # FILL IN
sorted_products = None  # FILL IN
sorted_values = None  # FILL IN
total_inventory_value = None  # FILL IN

cumulative_values = None  # FILL IN
cumulative_percentage = None  # FILL IN

print("\nProducts Ranked by Total Inventory Value:")
if sorted_indices is not None:
    print(f"{'Rank':<6} {'Product':<20} {'Total Value':<15} {'Cumulative %':<15}")
    print("-" * 60)
    for i in range(num_products):
        print(f"{i+1:<6} {sorted_products[i]:<20} ${sorted_values[i]:>13,.2f} {cumulative_percentage[i]:>13.1f}%")

# Task 3: ABC Classification
# TODO: Classify based on cumulative percentage thresholds (A:0-80%, B:80-95%, C:95-100%)
abc_classification = None  # FILL IN

print("\nABC Classification (Pareto Analysis):")
if abc_classification is not None:
    print(f"{'Rank':<6} {'Product':<20} {'Class':<8} {'Cumulative %':<15} {'Total Value':<15}")
    print("-" * 70)
    for i in range(num_products):
        print(f"{i+1:<6} {sorted_products[i]:<20} {abc_classification[i]:<8} "
              f"{cumulative_percentage[i]:>13.1f}% ${sorted_values[i]:>13,.2f}")

# Task 4: Count items and value in each category
# TODO: Use boolean masks to filter
class_a_count = None  # FILL IN
class_a_value = None  # FILL IN
class_b_count = None  # FILL IN
class_b_value = None  # FILL IN
class_c_count = None  # FILL IN
class_c_value = None  # FILL IN

print("\nABC Category Summary:")
if class_a_count is not None:
    print(f"{'Class':<10} {'Items':<12} {'% of Items':<15} {'Total Value':<15} {'% of Value':<15}")
    print("-" * 70)
    print(f"{'A':<10} {class_a_count:<12} {(class_a_count/num_products)*100:<14.1f}% "
          f"${class_a_value:>13,.2f} {(class_a_value/total_inventory_value)*100:>13.1f}%" if total_inventory_value else "")
    print(f"{'B':<10} {class_b_count:<12} {(class_b_count/num_products)*100:<14.1f}% "
          f"${class_b_value:>13,.2f} {(class_b_value/total_inventory_value)*100:>13.1f}%" if total_inventory_value else "")
    print(f"{'C':<10} {class_c_count:<12} {(class_c_count/num_products)*100:<14.1f}% "
          f"${class_c_value:>13,.2f} {(class_c_value/total_inventory_value)*100:>13.1f}%" if total_inventory_value else "")

# Task 5: Calculate inventory metrics by category
print("\nInventory Metrics by Category:")
print(f"{'Class':<10} {'Avg Unit Value':<18} {'Avg Quantity':<18}")
print("-" * 50)

for class_letter in ['A', 'B', 'C']:
    avg_value = None  # FILL IN
    avg_quantity = None  # FILL IN
    
    if avg_value is not None:
        print(f"{class_letter:<10} ${avg_value:<17.2f} {avg_quantity:<17.0f}")

# Task 6: Inventory management recommendations
print("\nRecommended Inventory Management Strategies:")
print("\nClass A (High Value - 80% of inventory value):")
print("  • Maintain tight control and frequent monitoring")
print("  • Use just-in-time (JIT) ordering to minimize carrying costs")
print("  • Implement advanced forecasting and demand planning")
print("  • Conduct regular physical counts (weekly or bi-weekly)")

print("\nClass B (Medium Value - 15% of inventory value):")
print("  • Use periodic review systems")
print("  • Implement moderate safety stock policies")
print("  • Conduct quarterly cycle counts")
print("  • Balance between stockouts and excess inventory")

print("\nClass C (Low Value - 5% of inventory value):")
print("  • Use simplified ordering systems (two-bin method)")
print("  • Maintain higher safety stock relative to value")
print("  • Less frequent monitoring (annual counts)")
print("  • Consider bulk purchasing and centralized storage")
print(f"\nTotal Inventory Value: ${total_inventory_value:,.2f}")
print(f"Number of Products: {num_products}")
print(f"Average Value per Product: ${total_inventory_value/num_products:,.2f}")
