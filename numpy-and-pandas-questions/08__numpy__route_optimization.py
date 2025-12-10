"""
Exercise 08: Route Optimization and Distance Matrix Analysis

Real-world scenario: Analyze delivery routes using distance matrices to identify 
the shortest and most fuel-efficient paths for product distribution.

Task:
1. Create a distance matrix between distribution centers and delivery points
2. Calculate total distance for different route sequences
3. Find the shortest route for delivery
4. Estimate fuel costs and delivery time for each route
5. Identify inefficient routes for optimization
6. Recommend optimal routing strategy
"""

import numpy as np

# 5 delivery locations (warehouse + 4 delivery points)
location_names = np.array(['Warehouse', 'Client-A', 'Client-B', 'Client-C', 'Client-D'])

# Distance matrix (in km) - symmetric
distance_matrix = np.array([
    [0,    50,   80,   60,   120],   # Warehouse
    [50,   0,    35,   45,   90],    # Client-A
    [80,   35,   0,    70,   110],   # Client-B
    [60,   45,   70,   0,    85],    # Client-C
    [120,  90,   110,  85,   0]      # Client-D
])

print("Delivery Route Optimization Analysis:")
print("\nDistance Matrix (km):")
print(f"{'Location':<15}", end="")
for name in location_names:
    print(f"{name:<12}", end="")
print()
print("-" * 75)

for i, name in enumerate(location_names):
    print(f"{name:<15}", end="")
    for j in range(len(location_names)):
        print(f"{distance_matrix[i][j]:<12.0f}", end="")
    print()

print("\n" + "="*75)

# Task 1: Calculate distances for different route sequences
# Route 1: Warehouse → A → B → C → D → Warehouse
route1 = [0, 1, 2, 3, 4, 0]  # indices

# Route 2: Warehouse → B → A → D → C → Warehouse
route2 = [0, 2, 1, 4, 3, 0]

# Route 3: Warehouse → D → C → B → A → Warehouse
route3 = [0, 4, 3, 2, 1, 0]

def calculate_route_distance(route_indices, distance_mat):
    """Calculate total distance for a route."""
    total = 0
    for i in range(len(route_indices) - 1):
        total += distance_mat[route_indices[i], route_indices[i+1]]
    return total

# TODO: Calculate distances for routes 1, 2, and 3
route1_distance = None  # FILL IN
route2_distance = None  # FILL IN
route3_distance = None  # FILL IN

print("\nRoute Distance Calculations:")
if route1_distance is not None:
    print(f"\nRoute 1: {' → '.join([location_names[i] for i in route1])}")
    print(f"  Distance: {route1_distance:.0f} km")

    print(f"\nRoute 2: {' → '.join([location_names[i] for i in route2])}")
    print(f"  Distance: {route2_distance:.0f} km")

    print(f"\nRoute 3: {' → '.join([location_names[i] for i in route3])}")
    print(f"  Distance: {route3_distance:.0f} km")

# Task 2: Find shortest route from all possible combinations
# Generate all permutations of clients (excluding warehouse which is fixed start/end)
from itertools import permutations

all_routes = None  # FILL IN: Generate and sort all possible routes

print("\n\nTop 5 Shortest Routes:")
if all_routes is not None:
    print(f"{'Rank':<6} {'Route':<50} {'Distance (km)':<15}")
    print("-" * 75)
    for rank, (route, distance) in enumerate(all_routes[:5], 1):
        route_str = ' → '.join([location_names[i] for i in route])
        print(f"{rank:<6} {route_str:<50} {distance:<15.0f}")

# Task 3: Calculate fuel costs and delivery time
fuel_consumption = 8  # km per liter
fuel_cost = 1.50  # dollars per liter
avg_speed = 60  # km per hour
delivery_time_per_stop = 30  # minutes

print("\n\nFuel Cost and Time Analysis:")
if all_routes is not None:
    print(f"{'Route':<40} {'Distance':<12} {'Fuel Cost':<15} {'Travel Time':<15}")
    print("-" * 82)
    # TODO: Calculate fuel costs and times for top 5 routes

# Task 4: Analyze current routes against optimal
print("\n\nRoute Efficiency Analysis:")
if all_routes is not None:
    optimal_distance = all_routes[0][1]
    # TODO: Compare routes 1, 2, 3 against optimal

# Task 5: Identify inefficiencies using distance matrix analysis
print("\n\nDistance Matrix Analysis:")
# TODO: Find shortest edges between all location pairs

# Task 6: Recommendations for optimization
print("\n\nOptimal Route Recommendation:")
if all_routes is not None:
    # TODO: Provide recommendations based on optimal route analysis
    print("TODO: Complete route recommendations")
