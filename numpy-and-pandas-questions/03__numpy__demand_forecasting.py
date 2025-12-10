"""
Exercise 03: Demand Forecasting with Time Series Data

Real-world scenario: A supply chain analyst needs to analyze historical demand 
patterns to forecast future product demand. Use NumPy to calculate moving averages, 
trends, and seasonal variations.

Task:
1. Create a time series array of monthly product demand
2. Calculate 3-month and 6-month moving averages
3. Calculate month-over-month growth rates
4. Identify seasonal patterns (high vs low demand months)
5. Normalize demand data for comparison across products
6. Forecast next month demand using trend analysis
"""

import numpy as np

# Historical monthly demand data for a product (in units)
monthly_demand = np.array([
    1200, 1450, 1100, 950, 1300, 1150,  # Year 1
    1400, 1600, 1250, 1350, 1500, 1450,  # Year 2
    1600, 1800, 1400, 1200, 1550, 1350   # Year 3 (partial)
])

months = np.arange(1, len(monthly_demand) + 1)

print("Monthly Demand Data:")
print(f"Months 1-{len(monthly_demand)}: {monthly_demand}")
print("\n" + "="*60)

# Task 1: Calculate 3-month moving average
# TODO: Use slicing and np.mean()
moving_avg_3 = None  # FILL IN
print("\n3-month moving average (starting from month 3):")
print(moving_avg_3)

# Task 2: Calculate 6-month moving average
# TODO: Use slicing and np.mean()
moving_avg_6 = None  # FILL IN
print("\n6-month moving average (starting from month 6):")
print(moving_avg_6)

# Task 3: Calculate month-over-month growth rates
# TODO: Use array slicing and basic arithmetic
growth_rates = None  # FILL IN
print("\nMonth-over-month growth rates (%):")
print(np.round(growth_rates, 2) if growth_rates is not None else None)

# Task 4: Identify seasonal patterns by quarter
# Q1: months 1,4,7,10,13,16 | Q2: months 2,5,8,11,14,17 | Q3: months 3,6,9,12,15,18
q1_demand = None  # FILL IN: Every 3rd month starting from index 0
q2_demand = None  # FILL IN
q3_demand = None  # FILL IN

print("\nSeasonal Pattern Analysis:")
if q1_demand is not None:
    print(f"Q1 (Winter) average demand: {np.mean(q1_demand):.2f}")
if q2_demand is not None:
    print(f"Q2 (Spring) average demand: {np.mean(q2_demand):.2f}")
if q3_demand is not None:
    print(f"Q3 (Summer) average demand: {np.mean(q3_demand):.2f}")

# Task 5: Normalize demand data (Z-score normalization)
# TODO: Use (value - mean) / std
mean_demand = np.mean(monthly_demand)
std_demand = np.std(monthly_demand)
normalized_demand = None  # FILL IN
print("\nNormalized demand (Z-score):")
print(np.round(normalized_demand, 2) if normalized_demand is not None else None)

# Task 6: Forecast next month using linear trend
# TODO: Use np.polyfit() or simple linear regression
coefficients = None  # FILL IN: Use np.polyfit(months, monthly_demand, 1)
next_month = len(months) + 1
forecasted_demand = None  # FILL IN: Use np.polyval(coefficients, next_month)

print(f"\nTrend analysis:")
if coefficients is not None:
    print(f"Linear trend coefficient: {coefficients[0]:.2f} units/month")
    print(f"Intercept: {coefficients[1]:.2f}")
print(f"Forecasted demand for month {next_month}: {forecasted_demand:.0f}" if forecasted_demand is not None else "")

# Bonus: Calculate demand volatility and safety stock
demand_std = np.std(monthly_demand)
demand_cv = (demand_std / mean_demand) * 100  # Coefficient of variation
safety_stock = 2 * demand_std  # 2-sigma safety stock

print(f"\nDemand Volatility:")
print(f"Standard deviation: {demand_std:.2f} units")
print(f"Coefficient of variation: {demand_cv:.2f}%")
print(f"Recommended safety stock (2-sigma): {safety_stock:.0f} units")
