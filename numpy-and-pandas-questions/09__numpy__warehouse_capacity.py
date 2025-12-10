"""
Exercise 09: Warehouse Capacity Planning and Utilization

Real-world scenario: Analyze warehouse capacity utilization across multiple 
facilities to identify bottlenecks and opportunities for optimization.

Task:
1. Create arrays for warehouse dimensions and current inventory
2. Calculate available and used capacity
3. Analyze utilization rates across warehouses
4. Identify capacity constraints and bottlenecks
5. Project future needs based on growth trends
6. Recommend capacity adjustments
"""

import numpy as np

# Warehouse data
warehouse_names = np.array(['NYC Hub', 'LA Hub', 'Chicago Hub', 'Dallas Hub', 'Atlanta Hub'])

# Warehouse dimensions (Length x Width x Height in meters)
warehouse_dims = np.array([
    [100, 50, 12],   # NYC Hub
    [150, 60, 10],   # LA Hub
    [80, 40, 15],    # Chicago Hub
    [120, 70, 12],   # Dallas Hub
    [90, 45, 14]     # Atlanta Hub
])

# Current inventory volume (cubic meters)
current_volume = np.array([45000, 68000, 32000, 55000, 38000])

# Monthly growth rate (%)
growth_rate = np.array([2.5, 1.8, 3.2, 2.1, 2.8])

print("Warehouse Capacity Planning Analysis:")
print("\nWarehouse Information:")
print(f"{'Warehouse':<20} {'L x W x H (m)':<20} {'Max Capacity (m³)':<20}")
print("-" * 60)

# Task 1: Calculate total capacity for each warehouse
# TODO: Use np.prod() to calculate volume
total_capacity = None  # FILL IN

if total_capacity is not None:
    for i, name in enumerate(warehouse_names):
        l, w, h = warehouse_dims[i]
        cap = total_capacity[i]
        print(f"{name:<20} {l:.0f} x {w:.0f} x {h:.0f}{'':<10} {cap:>18,.0f}")

print("\n" + "="*70)

# Task 2: Calculate utilization rates
# TODO: Use element-wise division
utilization_rate = None  # FILL IN

print("\nCurrent Utilization Analysis:")
if utilization_rate is not None:
    print(f"{'Warehouse':<20} {'Current (m³)':<18} {'Max Capacity (m³)':<20} {'Utilization %':<15}")
    print("-" * 75)
    for i, name in enumerate(warehouse_names):
        print(f"{name:<20} {current_volume[i]:>16,.0f} {total_capacity[i]:>18,.0f} {utilization_rate[i]:>13.1f}%")

# Task 3: Identify capacity constraints
# TODO: Flag warehouses at >80% and >85% capacity
critical_warehouses = None  # FILL IN
warning_warehouses = None  # FILL IN

print("\nCapacity Status:")
if critical_warehouses is not None:
    for i, name in enumerate(warehouse_names):
        if critical_warehouses[i]:
            print(f"  ⚠ CRITICAL: {name}")
        elif warning_warehouses[i]:
            print(f"  ⚠ WARNING: {name}")
        else:
            print(f"  ✓ OK: {name}")

# Task 4: Project future capacity needs
# TODO: Calculate projected volume using growth rates and months ahead
months_ahead = 12
growth_multiplier = None  # FILL IN: (1 + growth_rate/100) ** months_ahead
projected_volume = None  # FILL IN
projected_utilization = None  # FILL IN

print(f"\n\nProjected Capacity in {months_ahead} Months:")
if projected_volume is not None:
    print(f"{'Warehouse':<20} {'Current (m³)':<18} {'Projected (m³)':<18} {'Util. %':<12}")
    print("-" * 70)
    for i, name in enumerate(warehouse_names):
        print(f"{name:<20} {current_volume[i]:>16,.0f} {projected_volume[i]:>16,.0f} "
              f"{projected_utilization[i]:>10.1f}%")

# Task 5: Calculate capacity shortfall
# TODO: Use np.maximum() to find shortfall
shortfall = None  # FILL IN
shortfall_pct = None  # FILL IN

print("\n\nCapacity Gap Analysis:")
if shortfall is not None:
    print(f"{'Warehouse':<20} {'Shortfall (m³)':<18} {'% Over Capacity':<18}")
    print("-" * 60)
    for i, name in enumerate(warehouse_names):
        print(f"{name:<20} {shortfall[i]:>16,.0f} {shortfall_pct[i]:>16.1f}%")

# Task 6: Analyze utilization trends
print("\n\nUtilization Trend Analysis:")
if utilization_rate is not None:
    avg_utilization = np.mean(utilization_rate)
    std_utilization = np.std(utilization_rate)
    print(f"Network Average Utilization: {avg_utilization:.1f}%")
    print(f"Std Dev (variance in utilization): {std_utilization:.1f}%")

# Identify under-utilized warehouses
under_utilized = utilization_rate < 60 if utilization_rate is not None else None
if under_utilized is not None and np.any(under_utilized):
    print(f"\nUnder-utilized facilities (< 60%):")
    for i in np.where(under_utilized)[0]:
        print(f"  • {warehouse_names[i]}")

# Task 7: Capacity expansion recommendations
print("\n\nCapacity Expansion Recommendations:")
if shortfall is not None:
    expansion_needed = np.where(shortfall > 0)[0]
    if len(expansion_needed) == 0:
        print("✓ No expansion needed in next 12 months")
    else:
        print("TODO: Recommend expansions for facilities with shortfall")

print("\nOptimization Opportunities:")
print("1. Load Balancing - TODO: Calculate potential transfers")
print("2. Inventory Optimization - TODO: Calculate potential reductions")
print("3. Network Consolidation - TODO: Identify consolidation opportunities")
