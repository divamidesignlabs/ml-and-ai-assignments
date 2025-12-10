"""
Exercise 07: Lead Time Analysis and Safety Stock Calculation

Real-world scenario: Calculate safety stock levels based on demand variability 
and lead time to prevent stockouts while minimizing excess inventory.

Task:
1. Create daily demand and lead time data
2. Calculate mean demand and standard deviation
3. Compute safety stock using different service levels
4. Calculate reorder points for different lead times
5. Analyze the trade-off between service level and inventory cost
6. Determine optimal ordering parameters
"""

import numpy as np

# Daily demand data (in units) for 90 days
np.random.seed(42)
mean_daily_demand = 50
demand_std = 8
daily_demand = np.random.normal(mean_daily_demand, demand_std, 90)
daily_demand = np.maximum(daily_demand, 0)  # Ensure non-negative

# Lead times from different suppliers (in days)
lead_times = np.array([5, 7, 10, 14])
supplier_names = ['Fast Supplier', 'Standard Supplier', 'Economical Supplier', 'Overseas Supplier']

# Service level factors (Z-scores) corresponding to service levels
service_levels = np.array([0.84, 1.04, 1.28, 1.65, 2.33])  # 80%, 85%, 90%, 95%, 99%
service_level_pcts = np.array([80, 85, 90, 95, 99])

print("Lead Time and Safety Stock Analysis:")
print(f"Mean Daily Demand: {mean_daily_demand:.2f} units")
print(f"Demand Standard Deviation: {demand_std:.2f} units")
print(f"Coefficient of Variation: {(demand_std/mean_daily_demand)*100:.1f}%")
print("\n" + "="*70)

# Task 1: Calculate statistics from demand data
# TODO: Use np.mean(), np.std(), np.min(), np.max()
actual_mean = None  # FILL IN
actual_std = None  # FILL IN
min_demand = None  # FILL IN
max_demand = None  # FILL IN

print(f"\nActual Demand Statistics (from {len(daily_demand)} days):")
if actual_mean is not None:
    print(f"  Mean: {actual_mean:.2f} units")
    print(f"  Std Dev: {actual_std:.2f} units")
    print(f"  Min: {min_demand:.2f} units")
    print(f"  Max: {max_demand:.2f} units")
    print(f"  Range: {max_demand - min_demand:.2f} units")

# Task 2: Calculate safety stock for each lead time and service level
# Safety Stock = Z-score × Std Dev of Lead Time Demand
# Std Dev of Lead Time Demand = Demand Std × sqrt(Lead Time)

print("\nSafety Stock Requirements by Lead Time and Service Level:")
print(f"{'Lead Time (days)':<20} {'Supplier':<25}", end="")
for pct in service_level_pcts:
    print(f"{pct}%{'':<5}", end="")
print()
print("-" * 100)

# TODO: Calculate safety stock for each combination
safety_stock_matrix = None  # FILL IN

if safety_stock_matrix is not None:
    for i, lt in enumerate(lead_times):
        print(f"{lt:<20} {supplier_names[i]:<25}", end="")
        for ss in safety_stock_matrix[i]:
            print(f"{ss:>8.0f}  ", end="")
        print()

# Task 3: Calculate reorder points
# Reorder Point = (Average Daily Demand × Lead Time) + Safety Stock

print("\n\nReorder Points by Lead Time and Service Level:")
print(f"{'Lead Time (days)':<20} {'Supplier':<25}", end="")
for pct in service_level_pcts:
    print(f"{pct}%{'':<5}", end="")
print()
print("-" * 100)

# TODO: Calculate reorder points
reorder_point_matrix = None  # FILL IN

if reorder_point_matrix is not None:
    for i, lt in enumerate(lead_times):
        print(f"{lt:<20} {supplier_names[i]:<25}", end="")
        for rp in reorder_point_matrix[i]:
            print(f"{rp:>8.0f}  ", end="")
        print()

# Task 4: Analyze cost trade-offs
print("\n\nInventory Cost Analysis:")
carrying_cost_per_unit_day = 2
stockout_cost_per_unit = 100

service_level_90_idx = 2  # Index for 90% service level
print(f"\nAnalysis at 90% Service Level:")
if safety_stock_matrix is not None:
    print(f"{'Lead Time':<20} {'Supplier':<25} {'Safety Stock':<15} {'Carrying Cost/Day':<20}")
    print("-" * 80)

# Task 5: Compare different service levels
print(f"\n\nService Level Comparison ({supplier_names[1]}, {lead_times[1]}-day lead time):")
print(f"{'Service Level':<20} {'Safety Stock':<15} {'Reorder Point':<15} {'Annual Carrying Cost':<25}")
print("-" * 75)

# Task 6: Recommendations
print("\n\nRecommendations:")
print("\n1. Optimal Order Quantity (using Economic Order Quantity - EOQ concept):")
print("   TODO: Calculate EOQ")

print("\n2. Supplier Selection Recommendation:")
print("   TODO: Provide recommendation based on analysis")
print(f"   - If cost-conscious: Choose {supplier_names[2]} (10-day lead time)")
print(f"     Higher safety stock but lower supplier costs")
print(f"   - If reliability critical: Choose {supplier_names[0]} (5-day lead time)")
print(f"     Lower safety stock, faster replenishment")

print("\n3. Service Level Recommendation:")
print("   - 90% for Class C inventory (low value, easy to replace)")
print("   - 95% for Class B inventory (medium value)")
print("   - 99% for Class A inventory (high value, critical items)")

print("\n* Annual cost assumes daily carrying cost remains constant")
