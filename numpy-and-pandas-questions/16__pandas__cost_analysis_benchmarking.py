"""
Exercise 06: Supply Chain Cost Analysis and Benchmarking

Real-world scenario: Analyze total supply chain costs across multiple cost categories 
and benchmark against industry standards to identify optimization opportunities.

Task:
1. Create comprehensive cost data (procurement, transportation, storage, handling)
2. Categorize and aggregate costs by type
3. Calculate cost per unit for different product lines
4. Perform variance analysis (actual vs budget)
5. Benchmark costs against standards
6. Identify cost reduction opportunities
"""

import pandas as pd
import numpy as np

# Create detailed cost data
cost_data = {
    'Month': pd.period_range('2023-01-01', periods=12, freq='M'),
    'Procurement_Cost': np.random.uniform(50000, 80000, 12),
    'Transportation_Cost': np.random.uniform(30000, 50000, 12),
    'Warehousing_Cost': np.random.uniform(20000, 30000, 12),
    'Handling_Cost': np.random.uniform(15000, 25000, 12),
    'Labor_Cost': np.random.uniform(40000, 60000, 12),
    'Quality_Cost': np.random.uniform(5000, 15000, 12),
    'Units_Processed': np.random.randint(100000, 200000, 12),
    'Orders_Processed': np.random.randint(500, 1000, 12)
}

costs_df = pd.DataFrame(cost_data)

# Create product line cost data
product_costs = pd.DataFrame({
    'Product_Line': ['Electronics', 'Raw Materials', 'Packaging', 'Components', 'Assemblies'],
    'Units_Sold': [50000, 75000, 120000, 40000, 35000],
    'Procurement': [150000, 120000, 80000, 90000, 110000],
    'Transportation': [45000, 35000, 20000, 28000, 32000],
    'Handling': [25000, 20000, 15000, 18000, 22000],
    'Warehousing': [30000, 25000, 18000, 22000, 28000],
    'Labor': [35000, 30000, 22000, 25000, 28000]
})

# Budget/Standard data
budget_data = pd.DataFrame({
    'Cost_Category': ['Procurement', 'Transportation', 'Warehousing', 'Handling', 'Labor', 'Quality'],
    'Budgeted_Annual': [800000, 480000, 300000, 240000, 600000, 120000],
    'Industry_Std_%': [35, 20, 13, 10, 22, 5]  # % of total supply chain cost
})

print("Supply Chain Cost Analysis and Benchmarking")
print("\n" + "="*80)

print("\nMonthly Cost Data Sample:")
print(costs_df.head(10))

print("\n\nProduct Line Cost Breakdown:")
print(product_costs)

print("\n" + "="*80)

# Task 1: Calculate total costs and composition
# TODO: Calculate total monthly costs and cost metrics
print("\nTotal Cost Analysis:")
costs_df['Total_Cost'] = None  # FILL IN
print("TODO: Display monthly cost summary")

# Task 2: Cost composition analysis
# TODO: Analyze cost breakdown by category
print("\n\nAnnual Cost Composition:")
print("TODO: Analyze cost composition")

# Task 3: Variance analysis
# TODO: Compare actual costs vs budget
print("\n\nBudget Variance Analysis:")
print("TODO: Calculate variances")

# Task 4: Benchmarking against industry standards
# TODO: Compare costs against industry standards
print("\n\nIndustry Benchmarking:")
print("TODO: Compare against industry standards")

# Task 5: Product line cost analysis
# TODO: Analyze costs by product line
print("\n\nProduct Line Cost Analysis:")
print("TODO: Analyze by product line")

# Task 6: Cost optimization opportunities
# TODO: Identify cost reduction opportunities
print("\n\nCost Optimization Opportunities:")
print("TODO: Identify opportunities")

total_opportunity = sum([opp[2] for opp in opportunities])
if total_opportunity > 0:
    print(f"\n• Total Cost Reduction Potential: ${total_opportunity:,.0f}")
    print(f"• Percentage Improvement: {(total_opportunity/total_annual_cost)*100:.1f}%")
    
print("\nNext Steps:")
print("1. Prioritize high-impact cost reduction initiatives")
print("2. Implement vendor management program")
print("3. Invest in supply chain technology")
print("4. Regular benchmarking against competitors")
