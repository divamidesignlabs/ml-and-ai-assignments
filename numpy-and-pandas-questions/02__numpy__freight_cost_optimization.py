"""
Exercise 02: Freight Cost Calculation and Optimization

Real-world scenario: A logistics company needs to calculate shipping costs based on 
weight, distance, and freight class. Use NumPy's broadcasting to apply rates across 
multiple shipments efficiently.

Task:
1. Create arrays for shipment weights, distances, and freight classes
2. Use broadcasting to calculate base costs for all shipments
3. Apply freight class multipliers using fancy indexing
4. Calculate savings from bulk shipping discounts
5. Find the most cost-effective shipment routes
"""

import numpy as np

# Create shipment data
num_shipments = 8
weights = np.array([500, 1200, 350, 2100, 450, 890, 1500, 600])  # in kg
distances = np.array([100, 250, 150, 400, 120, 300, 350, 200])    # in km
freight_classes = np.array([0, 1, 0, 2, 0, 1, 2, 1])              # 0=Standard, 1=Express, 2=Premium

# Base rate: cost per kg per km
base_rate = 0.05  # dollars per kg per km

print("Shipment Data:")
print(f"Weights (kg): {weights}")
print(f"Distances (km): {distances}")
print(f"Freight Classes: {freight_classes} (0=Standard, 1=Express, 2=Premium)")
print("\n" + "="*60)

# Task 1: Calculate base costs using broadcasting
# TODO: Use broadcasting to multiply weight * distance * base_rate
base_costs = None  # FILL IN
print("\nBase costs (weight × distance × rate):")
print(base_costs)

# Task 2: Apply freight class multipliers using fancy indexing
# Standard=1.0x, Express=1.5x, Premium=2.0x
multipliers = np.array([1.0, 1.5, 2.0])
cost_multipliers = None  # FILL IN: Use multipliers[freight_classes]
print("\nCost multipliers by freight class:")
print(cost_multipliers)

# Task 3: Calculate final shipping costs
# TODO: Apply multipliers to base costs using broadcasting
final_costs = None  # FILL IN
print("\nFinal shipping costs:")
print(final_costs)

# Task 4: Calculate bulk discount savings
# Discount: 10% off for shipments > 1000 kg, additional 5% for > 2000 kg
discounts = None  # FILL IN: Use boolean indexing on weights array
savings = None  # FILL IN
final_costs_with_discount = None  # FILL IN

print("\nDiscount percentages:")
print(discounts * 100 if discounts is not None else None)
print("\nSavings from bulk discounts:")
print(savings)
print("\nFinal costs after discounts:")
print(final_costs_with_discount)

# Task 5: Find most cost-effective shipments
# TODO: Find indices of lowest costs
cheapest_indices = None  # FILL IN: Use np.argsort()
print("\n3 Most cost-effective shipments:")
if cheapest_indices is not None:
    for i, idx in enumerate(cheapest_indices[:3], 1):
        print(f"  {i}. Shipment {idx}: Weight={weights[idx]}kg, " 
              f"Distance={distances[idx]}km, Cost=${final_costs_with_discount[idx]:.2f}" if final_costs_with_discount is not None else "")

# Bonus: Calculate total shipping budget and average cost per km
total_budget = None  # FILL IN: Use np.sum()
cost_per_km = None  # FILL IN
avg_cost_per_km = None  # FILL IN: Use np.mean()

print(f"\nTotal shipping budget: ${total_budget:.2f}" if total_budget is not None else "")
print(f"Average cost per km: ${avg_cost_per_km:.2f}" if avg_cost_per_km is not None else "")
