"""
Exercise 02: Shipment Performance and Delivery Tracking

Real-world scenario: Track and analyze shipment performance metrics including 
on-time delivery rates, cost efficiency, and delivery exceptions.

Task:
1. Create DataFrame with shipment records (date, origin, destination, status)
2. Calculate on-time delivery performance
3. Analyze delivery delays and identify patterns
4. Calculate cost per unit delivered
5. Create performance dashboards by route
6. Identify problem routes and carriers
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create shipment data
np.random.seed(42)
num_shipments = 150

# Generate dates across 3 months
start_date = datetime(2023, 9, 1)
shipment_dates = [start_date + timedelta(days=np.random.randint(0, 90)) for _ in range(num_shipments)]

# Create DataFrame
shipments = pd.DataFrame({
    'Shipment_ID': [f'SHP-{i:05d}' for i in range(1, num_shipments + 1)],
    'Ship_Date': shipment_dates,
    'Origin': np.random.choice(['NYC', 'LA', 'Chicago', 'Dallas'], num_shipments),
    'Destination': np.random.choice(['Miami', 'Denver', 'Seattle', 'Boston'], num_shipments),
    'Carrier': np.random.choice(['FedEx', 'UPS', 'DHL', 'XPO'], num_shipments),
    'Shipped_Units': np.random.randint(100, 2000, num_shipments),
    'Shipping_Cost': np.random.uniform(500, 5000, num_shipments),
    'Expected_Delivery': [d + timedelta(days=np.random.randint(3, 8)) for d in shipment_dates],
    'Actual_Delivery': None,
    'Status': np.random.choice(['Delivered', 'In Transit', 'Delayed', 'Lost'], num_shipments)
})

# Fill actual delivery dates based on status
for idx, row in shipments.iterrows():
    if row['Status'] == 'Delivered':
        days_offset = np.random.randint(-2, 5)
        shipments.at[idx, 'Actual_Delivery'] = row['Expected_Delivery'] + timedelta(days=days_offset)
    elif row['Status'] == 'In Transit':
        shipments.at[idx, 'Actual_Delivery'] = None
    elif row['Status'] == 'Delayed':
        days_offset = np.random.randint(3, 15)
        shipments.at[idx, 'Actual_Delivery'] = row['Expected_Delivery'] + timedelta(days=days_offset)
    else:  # Lost
        shipments.at[idx, 'Actual_Delivery'] = None

print("Shipment Performance Analysis")
print("\n" + "="*80)
print("\nFirst 10 Shipments:")
print(shipments.head(10))

print(f"\nTotal Shipments: {len(shipments)}")
print(f"Date Range: {shipments['Ship_Date'].min().date()} to {shipments['Ship_Date'].max().date()}")

# Task 1: Calculate on-time delivery performance
# TODO: Filter delivered shipments and compare actual vs expected delivery dates
delivered = None  # FILL IN
on_time = None  # FILL IN
on_time_rate = None  # FILL IN

print("\n" + "="*80)
print("\nOn-Time Delivery Performance:")
if delivered is not None:
    print(f"  Total Delivered: {len(delivered)}")
    print(f"  On-Time: {len(on_time) if on_time is not None else 0}")
    print(f"  On-Time Rate: {on_time_rate:.1f}%" if on_time_rate is not None else "")

# Task 2: Analyze delivery delays
# TODO: Group by status and calculate summary statistics
print("\n\nDelivery Performance by Status:")
status_summary = None  # FILL IN
print(status_summary)

# Calculate average delay for late shipments
late_shipments = None  # FILL IN
if late_shipments is not None and len(late_shipments) > 0:
    print(f"\nDelay Analysis (Late Shipments):")
    print("  TODO: Calculate average and max delays")

# Task 3: Calculate cost efficiency
# TODO: Create Cost_Per_Unit column and analyze by carrier
shipments['Cost_Per_Unit'] = None  # FILL IN

print("\n\nCost Efficiency Analysis:")
cost_stats = None  # FILL IN
print(cost_stats)

# Task 4: Performance by route
# TODO: Create Route column and analyze by route
print("\n\nPerformance by Route (Origin → Destination):")
shipments['Route'] = None  # FILL IN
route_performance = None  # FILL IN
print(route_performance)

# Task 5: Carrier performance
# TODO: Calculate on-time rate and other metrics by carrier
print("\n\nCarrier Performance Scorecard:")
carrier_performance = None  # FILL IN
print(carrier_performance)

# Task 6: Identify problem shipments
# TODO: Filter delayed and lost shipments
print("\n\nProblem Shipments Requiring Attention:")
problem_shipments = None  # FILL IN
if problem_shipments is not None:
    print(f"\nTotal Problem Shipments: {len(problem_shipments)}")
    print("\nMost Recent Issues:")
    print(problem_shipments[['Shipment_ID', 'Ship_Date', 'Origin', 'Destination', 'Carrier', 'Status']].head(10))

print("\n\nKey Recommendations:")
print("TODO: Provide recommendations based on analysis")
print("1. Improve on-time delivery through carrier performance management")
print("2. Consolidate shipments with best-performing carriers")
print("3. Review pricing with underperforming carriers")
print("4. Implement expedited shipping for critical routes")
print("5. Establish recovery procedures for delayed shipments")
