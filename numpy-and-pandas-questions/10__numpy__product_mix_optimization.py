"""
Exercise 10: Product Mix Optimization for Revenue and Profit

Real-world scenario: Analyze product profitability, demand constraints, and 
production capacity to recommend optimal product mix for maximum profit.

Task:
1. Create arrays for product costs, prices, and constraints
2. Calculate profit margin for each product
3. Analyze demand elasticity and supply constraints
4. Calculate contribution margin and break-even points
5. Identify profitable vs unprofitable products
6. Recommend optimal product mix strategy
"""

import numpy as np

# Product data
product_names = np.array([
    'Connector-A', 'Module-B', 'Panel-C', 'Unit-D', 'Cable-E', 'Assembly-F', 'Control-G', 'Sensor-H'
])

# Cost and pricing information
unit_costs = np.array([15.0, 45.0, 85.0, 120.0, 8.0, 200.0, 95.0, 55.0])
selling_prices = np.array([25.0, 78.0, 145.0, 210.0, 12.0, 380.0, 160.0, 95.0])

# Current monthly demand (units)
current_demand = np.array([8000, 2500, 1200, 800, 15000, 500, 1500, 3000])

# Maximum production capacity (units per month)
max_capacity = np.array([10000, 3000, 1500, 1000, 20000, 700, 2000, 4000])

# Market growth rate (% per year)
growth_rate = np.array([5, 12, 8, 3, 15, 20, 10, 7])

# Raw material availability constraint (monthly)
raw_materials_required = np.array([1, 3, 5, 8, 0.5, 12, 6, 3.5])  # units per item
total_raw_materials_available = 100000  # units

print("Product Mix Optimization Analysis:")
print("\nProduct Data:")
print(f"{'Product':<15} {'Cost':<12} {'Price':<12} {'Demand':<12} {'Capacity':<12} {'Growth %':<12}")
print("-" * 75)

for i, name in enumerate(product_names):
    print(f"{name:<15} ${unit_costs[i]:<11.2f} ${selling_prices[i]:<11.2f} "
          f"{current_demand[i]:<12.0f} {max_capacity[i]:<12.0f} {growth_rate[i]:<12.0f}")

print("\n" + "="*75)

# Task 1: Calculate profit metrics
# TODO: Calculate unit profit, profit margin %, and contribution margin
unit_profit = None  # FILL IN
profit_margin_pct = None  # FILL IN
contribution_margin = None  # FILL IN

print("\nProfit Metrics Analysis:")
if unit_profit is not None:
    print(f"{'Product':<15} {'Unit Profit':<14} {'Margin %':<14} {'CM Ratio':<14}")
    print("-" * 60)
    for i, name in enumerate(product_names):
        print(f"{name:<15} ${unit_profit[i]:<13.2f} {profit_margin_pct[i]:<13.1f}% {contribution_margin[i]:<13.1f}%")

# Task 2: Calculate current profitability
# TODO: Calculate current revenue, costs, and profit for each product
current_revenue = None  # FILL IN
current_costs = None  # FILL IN
current_profits = None  # FILL IN

print("\n\nCurrent Profitability Analysis:")
if current_revenue is not None:
    print(f"{'Product':<15} {'Revenue':<18} {'Costs':<18} {'Profit':<18}")
    print("-" * 70)
    for i, name in enumerate(product_names):
        print(f"{name:<15} ${current_revenue[i]:>16,.0f} ${current_costs[i]:>16,.0f} "
              f"${current_profits[i]:>16,.0f}")

# Task 3: Capacity utilization analysis
# TODO: Calculate actual utilization percentage
capacity_utilization = None  # FILL IN

print("\n\nCapacity Utilization Analysis:")
if capacity_utilization is not None:
    print(f"{'Product':<15} {'Demand':<12} {'Capacity':<12} {'Utilization':<15} {'Available Slack':<15}")
    print("-" * 70)
    for i, name in enumerate(product_names):
        utilization = capacity_utilization[i]
        slack = max_capacity[i] - current_demand[i]
        print(f"{name:<15} {current_demand[i]:<12.0f} {max_capacity[i]:<12.0f} "
              f"{utilization:<14.1f}% {slack:<15.0f}")

# TODO: Identify bottleneck products (over 90% utilization)
bottlenecks = None  # FILL IN

# Task 4: Ranking products by profitability metrics
# TODO: Rank by different criteria
profit_per_unit_ranking = None  # FILL IN
margin_ranking = None  # FILL IN
total_profit_ranking = None  # FILL IN

print("\n\nProduct Rankings by Different Criteria:")

if profit_per_unit_ranking is not None:
    print("\n1. By Unit Profit (highest to lowest):")
    for rank, idx in enumerate(profit_per_unit_ranking, 1):
        print(f"   {rank}. {product_names[idx]}: ${unit_profit[idx]:.2f}/unit" if unit_profit is not None else "")

if margin_ranking is not None:
    print("\n2. By Profit Margin % (highest to lowest):")
    for rank, idx in enumerate(margin_ranking, 1):
        print(f"   {rank}. {product_names[idx]}: {profit_margin_pct[idx]:.1f}%" if profit_margin_pct is not None else "")

if total_profit_ranking is not None:
    print("\n3. By Total Monthly Profit (highest to lowest):")
    for rank, idx in enumerate(total_profit_ranking, 1):
        print(f"   {rank}. {product_names[idx]}: ${current_profits[idx]:,.0f}" if current_profits is not None else "")

# Task 5: Growth potential analysis
# TODO: Project 12-month future demand and profitability
months_ahead = 12
growth_multiplier = None  # FILL IN
projected_demand = None  # FILL IN
projected_demand_constrained = None  # FILL IN

print("\n\n12-Month Growth Projection:")
if projected_demand is not None:
    print(f"{'Product':<15} {'Current':<15} {'Projected':<15} {'Max Capacity':<15} {'Constrained':<15} {'Growth %':<12}")
    print("-" * 90)
    for i, name in enumerate(product_names):
        constrained = projected_demand_constrained[i]
        growth = ((constrained - current_demand[i]) / current_demand[i]) * 100 if current_demand[i] > 0 else 0
        print(f"{name:<15} {current_demand[i]:<15.0f} {projected_demand[i]:<15.0f} "
              f"{max_capacity[i]:<15.0f} {constrained:<15.0f} {growth:<12.1f}%")

# Task 6: Product mix recommendations
print("\n\nProduct Mix Optimization Recommendations:")
print("\n1. CORE PRODUCTS (High profit, high growth):")
print("   TODO: Identify and list core products")

print("\n2. CASH COW PRODUCTS (High current profit):")
print("   TODO: Identify and list cash cows")

print("\n3. PROBLEM PRODUCTS (Low margin, high capacity used):")
print("   TODO: Identify and list problem products")

print("\n4. EMERGING PRODUCTS (Low current volume, high growth potential):")
print("   TODO: Identify and list emerging products")

# Optimal production allocation
print("\n\nOptimal Production Allocation (constrained):")
print(f"{'Rank':<6} {'Product':<15} {'Production':<15} {'Profit/Unit':<15} {'Total Profit':<15}")
print("-" * 70)
print("TODO: Complete optimal allocation based on profit rankings")
