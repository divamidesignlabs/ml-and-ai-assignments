"""
Exercise 05: Supplier Performance Metrics Calculation

Real-world scenario: Evaluate supplier performance based on multiple metrics 
(on-time delivery, quality, cost) using NumPy array operations and 
statistical calculations.

Task:
1. Create arrays for supplier delivery times, defect rates, and unit costs
2. Calculate standardized scores for each metric (0-100 scale)
3. Compute weighted overall performance score
4. Identify top and bottom performing suppliers
5. Detect anomalies in supplier data
6. Rank suppliers for contract renewal decisions
"""

import numpy as np

# Supplier data
num_suppliers = 8
supplier_names = [f'Supplier-{i}' for i in range(1, num_suppliers + 1)]

# On-time delivery rate (%)
on_time_delivery = np.array([95, 87, 92, 78, 88, 91, 85, 89])

# Quality (% defect-free products)
quality_rate = np.array([98, 94, 96, 85, 92, 95, 91, 93])

# Unit cost ($/unit)
unit_cost = np.array([45, 52, 48, 38, 55, 50, 42, 49])

print("Supplier Performance Data:")
print(f"{'Supplier':<15} {'On-Time %':<12} {'Quality %':<12} {'Cost $/unit':<12}")
print("-" * 50)
for i, name in enumerate(supplier_names):
    print(f"{name:<15} {on_time_delivery[i]:<12} {quality_rate[i]:<12} {unit_cost[i]:<12.2f}")
print("\n" + "="*60)

# Task 1: Standardize metrics to 0-100 scale
# TODO: Normalize each metric independently
on_time_score = None  # FILL IN
quality_score = None  # FILL IN
cost_score = None  # FILL IN: Lower cost = higher score

print("\nNormalized Scores (0-100 scale):")
if on_time_score is not None:
    print(f"{'Supplier':<15} {'On-Time':<12} {'Quality':<12} {'Cost':<12}")
    print("-" * 50)
    for i, name in enumerate(supplier_names):
        print(f"{name:<15} {on_time_score[i]:<12.1f} {quality_score[i]:<12.1f} {cost_score[i]:<12.1f}")

# Task 2: Calculate weighted overall performance score
# Weights: On-time delivery (40%), Quality (35%), Cost (25%)
overall_scores = None  # FILL IN: Use weights

print("\nOverall Performance Scores (weighted):")
if overall_scores is not None:
    print(f"{'Supplier':<15} {'Score':<10} {'Percentile':<12}")
    print("-" * 40)
    percentiles = np.argsort(np.argsort(overall_scores)) / len(overall_scores) * 100
    for i, name in enumerate(supplier_names):
        print(f"{name:<15} {overall_scores[i]:<10.2f} {percentiles[i]:<12.1f}%")

# Task 3: Identify top and bottom performers
# TODO: Use np.argsort() and slicing
sorted_indices = None  # FILL IN
top_3_indices = None  # FILL IN
bottom_3_indices = None  # FILL IN

print("\nTop 3 Performing Suppliers:")
if top_3_indices is not None:
    for rank, idx in enumerate(sorted(top_3_indices, reverse=True), 1):
        print(f"  {rank}. {supplier_names[idx]}: {overall_scores[idx]:.2f}" if overall_scores is not None else "")

print("\nBottom 3 Performing Suppliers:")
if bottom_3_indices is not None:
    for rank, idx in enumerate(sorted(bottom_3_indices), 1):
        print(f"  {rank}. {supplier_names[idx]}: {overall_scores[idx]:.2f}" if overall_scores is not None else "")

# Task 4: Detect anomalies (outliers in performance)
# TODO: Use mean and standard deviation to find outliers
z_scores = None  # FILL IN
anomalies = None  # FILL IN

print("\nPerformance Anomalies (Z-score > 2):")
if anomalies is not None and np.any(anomalies):
    for idx in np.where(anomalies)[0]:
        deviation = "Above" if z_scores[idx] > 0 else "Below"
        print(f"  {supplier_names[idx]}: {deviation} average")
else:
    print("  No anomalies found or anomalies not calculated")

# Task 5: Create supplier recommendation matrix
# TODO: Use boolean arrays to create selections
reliable_on_time = None  # FILL IN
high_quality = None  # FILL IN
cost_effective = None  # FILL IN

print("\nSupplier Suitability Matrix:")
if reliable_on_time is not None:
    print(f"{'Supplier':<15} {'Reliable':<12} {'Quality':<12} {'Cost-Eff':<12} {'Recommendation'}")
    print("-" * 65)
    for i, name in enumerate(supplier_names):
        criteria_met = sum([reliable_on_time[i], high_quality[i], cost_effective[i]])
        if criteria_met == 3:
            recommendation = "Preferred"
        elif criteria_met == 2:
            recommendation = "Acceptable"
        elif criteria_met == 1:
            recommendation = "Monitor"
        else:
            recommendation = "Consider alternatives"
        print(f"{name:<15} {str(reliable_on_time[i]):<12} {str(high_quality[i]):<12} "
              f"{str(cost_effective[i]):<12} {recommendation}")

# Task 6: Risk assessment for supplier concentration
# TODO: Calculate concentration using Herfindahl index
performance_weights = None  # FILL IN
herfindahl_index = None  # FILL IN
concentration_ratio = None  # FILL IN

print(f"\nSupply Chain Concentration Analysis:")
if herfindahl_index is not None:
    print(f"  Herfindahl Index: {herfindahl_index:.4f}")
    print(f"  Top 3 supplier concentration: {concentration_ratio*100:.1f}%")
