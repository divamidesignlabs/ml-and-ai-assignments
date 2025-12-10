"""
Exercise 04: Multi-Warehouse Distribution Optimization

Real-world scenario: A company has 3 warehouses and needs to distribute 
products to minimize transportation costs and meet regional demand. 
Use NumPy for matrix operations to calculate optimal distribution.

Task:
1. Create supply capacity array for each warehouse
2. Create demand requirements for each region
3. Create transportation cost matrix (warehouse x region)
4. Calculate total potential distribution cost
5. Identify warehouse-region combinations with highest costs
6. Find the most efficient distribution path
"""

import numpy as np

# Warehouse supply capacities (units)
warehouse_capacity = np.array([5000, 4000, 3500])  # WH1, WH2, WH3
warehouse_names = ['Warehouse-A', 'Warehouse-B', 'Warehouse-C']

# Regional demand (units)
regional_demand = np.array([2500, 2000, 1800, 1500, 1200])  # R1-R5
region_names = ['Region-North', 'Region-South', 'Region-East', 'Region-West', 'Region-Central']

# Transportation cost per unit (warehouse x region matrix)
cost_matrix = np.array([
    [5.0,  8.0,  6.0,  12.0, 9.0],   # WH-A to regions
    [7.0,  4.0,  9.0,  6.0,  11.0],  # WH-B to regions
    [10.0, 7.0,  5.0,  8.0,  4.0]    # WH-C to regions
])

print("Supply Chain Distribution Problem:")
print(f"Warehouse Capacities: {warehouse_capacity}")
print(f"Total Supply: {np.sum(warehouse_capacity)} units")
print(f"\nRegional Demands: {regional_demand}")
print(f"Total Demand: {np.sum(regional_demand)} units")
print("\nTransportation Cost Matrix (Warehouse x Region):")
print("       ", "  ".join(f"{r:>12}" for r in region_names))
for i, name in enumerate(warehouse_names):
    print(f"{name}: {cost_matrix[i]}")
print("\n" + "="*80)

# Task 1: Find the lowest cost shipment routes
# TODO: Find minimum cost per region (which warehouse serves cheapest)
min_costs_per_region = None  # FILL IN
cheapest_warehouse = None  # FILL IN

print("\nLowest Cost Routes by Region:")
if cheapest_warehouse is not None:
    for j, region in enumerate(region_names):
        wh_idx = cheapest_warehouse[j]
        cost = min_costs_per_region[j]
        print(f"  {region}: {warehouse_names[wh_idx]} at ${cost:.2f}/unit")

# Task 2: Calculate distribution cost if each region gets from cheapest warehouse
# (considering demand quantities)
optimal_routing_cost = None  # FILL IN
print(f"\nOptimal routing cost (theoretical minimum): ${optimal_routing_cost:.2f}" if optimal_routing_cost is not None else "")

# Task 3: Create a practical distribution allocation
# Allocate based on warehouse capacity and regional proximity
distribution = None  # FILL IN: Create 3x5 allocation matrix

print("\nPractical Distribution Allocation (units):")
if distribution is not None:
    print("        ", "  ".join(f"{r:>12}" for r in region_names))
    for i, name in enumerate(warehouse_names):
        allocated = distribution[i]
        print(f"{name}: {[f'{int(x):>12}' for x in allocated]}")
    print(f"Allocation by region: {[int(np.sum(distribution[:, j])) for j in range(5)]}")

# Task 4: Calculate actual distribution cost
# TODO: Use matrix multiplication or element-wise multiplication
actual_cost = None  # FILL IN
print(f"\nActual distribution cost: ${actual_cost:.2f}" if actual_cost is not None else "")

# Task 5: Analyze cost efficiency
cost_per_unit = None  # FILL IN
print(f"Cost per unit distributed: ${cost_per_unit:.2f}" if cost_per_unit is not None else "")

# Task 6: Identify over-utilized warehouses
utilization = None  # FILL IN
print("\nWarehouse Utilization:")
if utilization is not None:
    for i, name in enumerate(warehouse_names):
        print(f"  {name}: {utilization[i]:.1f}%")

# Bonus: Calculate service level (demand fulfillment)
fulfilled_demand = None  # FILL IN
service_level = None  # FILL IN
print("\nRegional Service Levels:")
if service_level is not None:
    for j, region in enumerate(region_names):
        print(f"  {region}: {service_level[j]:.1f}%")
