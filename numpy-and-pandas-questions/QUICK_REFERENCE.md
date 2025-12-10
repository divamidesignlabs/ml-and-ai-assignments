# NumPy & Pandas Supply Chain Exercises - Quick Reference

## 📋 Complete Exercise List

### NumPy Exercises (Array Operations & Numerical Computing)

| # | Exercise | Focus Area | Key Skills |
|---|----------|-----------|-----------|
| **01** | Inventory Stock Levels | Warehouse Analytics | Arrays, Aggregation, Boolean Masks |
| **02** | Freight Cost Optimization | Logistics Costs | Broadcasting, Fancy Indexing, Vectors |
| **03** | Demand Forecasting | Time Series | Moving Averages, Trend Analysis, Normalization |
| **04** | Warehouse Distribution | Network Optimization | 2D Arrays, Matrix Operations, Constraints |
| **05** | Supplier Performance | Vendor Management | Normalization, Weighted Scoring, Ranking |
| **06** | ABC Inventory Analysis | Inventory Classification | Sorting, Cumulative Sums, Pareto Analysis |
| **07** | Lead Time & Safety Stock | Inventory Planning | Statistics, Normal Distribution, Service Levels |
| **08** | Route Optimization | Delivery Planning | Distance Matrices, Path Finding, Permutations |
| **09** | Warehouse Capacity | Facility Planning | Volume Calculations, Projections, Constraints |
| **10** | Product Mix Optimization | Profitability | Profit Analysis, Ranking, Multi-Criteria Decisions |

### Pandas Exercises (Tabular Data & Data Analysis)

| # | Exercise | Focus Area | Key Skills |
|---|----------|-----------|-----------|
| **11** | Transaction Analysis | Purchase Ledger | DataFrames, GroupBy, Pivot Tables |
| **12** | Shipment Tracking | Logistics Performance | Datetime, Status Tracking, Performance Metrics |
| **13** | Inventory Cleaning | Data Quality | Missing Values, Data Types, Standardization |
| **14** | Multi-Location Orders | Procurement Network | Merging, Complex Grouping, Budget Analysis |
| **15** | Customer Fulfillment | Order Management | Customer Segmentation, Performance, Recommendations |
| **16** | Cost Analysis & Benchmarking | Financial Analysis | Cost Aggregation, Variance, Efficiency Metrics |
| **17** | Inventory Aging | Obsolescence Management | Age Classification, Risk Scoring, Disposition |
| **18** | Supplier Scorecard | Vendor Performance | Weighted Scoring, Multi-Dimensional Evaluation |
| **19** | Demand Analysis | Demand Planning | Seasonality, Patterns, Forecasting Methods |
| **20** | Risk Assessment | Supply Chain Resilience | Risk Scoring, Concentration Analysis, Mitigation |

---

## 🎯 Exercise by Learning Level

### Beginner (Build Foundations)
- **NumPy:** 01, 02
- **Pandas:** 11, 12, 13

**Focus:** Basic operations, simple filtering, fundamentals

### Intermediate (Apply Concepts)
- **NumPy:** 03, 04, 05, 06
- **Pandas:** 14, 15, 16

**Focus:** Multi-step analysis, merging data, business logic

### Advanced (Complex Analysis)
- **NumPy:** 07, 08, 09, 10
- **Pandas:** 17, 18, 19, 20

**Focus:** Advanced optimization, risk analysis, comprehensive strategies

---

## 📊 Exercise by Supply Chain Function

### Procurement & Sourcing
- 02: Freight Cost Optimization
- 05: Supplier Performance
- 14: Multi-Location Orders
- 18: Supplier Scorecard
- 20: Risk Assessment

### Inventory Management
- 01: Inventory Stock Levels
- 06: ABC Analysis
- 07: Safety Stock Calculation
- 13: Inventory Cleaning
- 17: Inventory Aging

### Demand & Planning
- 03: Demand Forecasting
- 19: Demand Analysis

### Logistics & Operations
- 04: Warehouse Distribution
- 08: Route Optimization
- 09: Warehouse Capacity
- 12: Shipment Tracking

### Finance & Analysis
- 10: Product Mix Optimization
- 11: Transaction Analysis
- 15: Customer Fulfillment
- 16: Cost Analysis

---

## 🔑 Key NumPy Concepts by Exercise

| Concept | Exercises | Description |
|---------|-----------|-------------|
| **Array Creation** | 01-10 | zeros, ones, arange, linspace, random |
| **Indexing** | 01, 04, 05, 06, 08 | Basic, fancy, boolean indexing |
| **Broadcasting** | 02, 04, 05, 07 | Operations on different-shaped arrays |
| **Aggregation** | 01, 03, 05, 06, 07 | sum, mean, min, max, std |
| **Sorting** | 05, 06, 08, 10 | argsort, argmax, argmin |
| **Linear Algebra** | 04, 08 | Matrix operations, path optimization |
| **Statistics** | 03, 05, 07, 09 | Normalization, Z-scores, percentiles |
| **Vectorization** | 02, 05, 10 | Element-wise operations, no loops |

---

## 🔑 Key Pandas Concepts by Exercise

| Concept | Exercises | Description |
|---------|-----------|-------------|
| **DataFrame Creation** | 11-20 | From dict, list, other sources |
| **Indexing/Selection** | 11-20 | .loc, .iloc, direct access, filtering |
| **GroupBy & Agg** | 11, 14, 15, 16, 18, 19 | Splitting, applying, combining |
| **Merging/Joining** | 14, 15, 18, 20 | merge, concat, different join types |
| **Reshaping** | 14, 16 | pivot_table, stack, unstack |
| **Missing Data** | 13 | isnull, fillna, dropna |
| **DateTime** | 12, 19 | Date operations, time periods |
| **Boolean Indexing** | 12, 13, 15, 17, 20 | Filtering with conditions |
| **String Operations** | 13 | Standardization, case conversion |

---

## 💡 Quick Start Guide

### To Run One Exercise
```bash
cd /Users/yeshwanth/Code/Divami/ml-and-ai-assignments/numpy-and-pandas
python 01__numpy__inventory_stock_levels.py
```

### To Run All NumPy Exercises
```bash
python 0[1-9]__numpy*.py && python 10__numpy*.py
```

### To Run All Pandas Exercises
```bash
python [1-2][0-9]__pandas*.py
```

### To Run Specific Category
```bash
# All inventory-related
python *inventory*.py

# All forecasting
python *forecast*.py *demand*.py
```

---

## 📈 Data Complexity by Exercise

```
Exercise Complexity Growth
│
│     ◆ (20-Risk Assessment)
│    ◆ (19-Demand Analysis)  
│   ◆ (18-Supplier Scorecard)
│  ◆ (17-Inventory Aging)
│ ◆ (16-Cost Analysis)
├─────────────────────────── Advanced
│ ◆ (15-Customer Fulfillment)
│ ◆ (14-Multi-Location Orders)
├─────────────────────────── Intermediate
│ ◆ (13-Inventory Cleaning)
│ ◆ (12-Shipment Tracking)
│ ◆ (11-Transactions)
├─────────────────────────── Beginner
│ ◆ (10-Product Mix)
│ ◆ (09-Capacity)
│ ◆ (08-Route Optimization)
│ ◆ (07-Safety Stock)
│ ◆ (06-ABC Analysis)
│ ◆ (05-Supplier Performance)
│ ◆ (04-Distribution)
│ ◆ (03-Demand Forecasting)
│ ◆ (02-Freight Costs)
│ ◆ (01-Inventory Levels)
└─────────────────────────────
  Beginner → Intermediate → Advanced
```

---

## 🎓 Learning Paths

### Path A: Supply Chain Analyst
1. 01 → 03 → 06 → 07 → 19 → 17 → 20

**Skills:** Inventory optimization, demand planning, risk management

### Path B: Procurement Professional
1. 02 → 05 → 11 → 14 → 18 → 20 → 14

**Skills:** Cost optimization, supplier management, strategic sourcing

### Path C: Operations Manager
1. 01 → 04 → 08 → 09 → 12 → 15 → 16

**Skills:** Network optimization, facility management, performance metrics

### Path D: Finance/Cost Management
1. 02 → 10 → 11 → 16 → 19 → 06 → 03

**Skills:** Profitability analysis, cost control, financial planning

---

## 📚 Data Structures Used

### NumPy
- **1D Arrays:** Demand, costs, scores
- **2D Arrays:** Warehouses×Products, Distance matrices, Cost matrices
- **3D Arrays:** Multi-level inventory (Warehouse×Category×Item)

### Pandas
- **Series:** Single product data, time series
- **DataFrame:** Transactions, orders, shipments, customers
- **MultiIndex:** Supplier×Category, Time×Location
- **Categorical:** Status, classification, region

---

## ✅ Expected Outcomes

Each exercise produces:

1. **Data Exploration**
   - Row/column counts
   - Data types and formats
   - Missing value assessment

2. **Statistical Analysis**
   - Descriptive statistics
   - Aggregated metrics
   - Comparisons and ratios

3. **Business Insights**
   - Patterns and trends
   - Performance gaps
   - Optimization opportunities

4. **Actionable Recommendations**
   - Priority actions
   - Timeline for execution
   - Expected benefits/savings

---

## 🚀 Advanced Usage

### Extend Exercise 01
```python
# Add your own data
warehouse_stock = np.array([...])  # Your data

# Add new metrics
holding_cost_per_unit = 2.5
annual_holding = np.sum(total_per_product * holding_cost_per_unit)
```

### Combine Exercises
```python
# Use output from Ex01 (inventory levels) with Ex07 (safety stock)
# Use output from Ex03 (demand) with Ex06 (ABC analysis)
```

### Integrate with Real Data
```python
# Read from CSV
import pandas as pd
df = pd.read_csv('your_data.csv')

# Apply exercise logic to your data
results = df.groupby('Supplier')['Cost'].agg(['sum', 'mean'])
```

---

## 📖 File Organization

```
numpy-and-pandas/
├── 01__numpy__*.py through 10__numpy__*.py    [10 NumPy exercises]
├── 11__pandas__*.py through 20__pandas__*.py  [10 Pandas exercises]
├── README_EXERCISES.md                        [Comprehensive guide]
└── QUICK_REFERENCE.md                         [This file]
```

---

## ⏱️ Estimated Time Investment

| Level | NumPy | Pandas | Total |
|-------|-------|--------|-------|
| **Beginner** | 3-4 hrs | 3-4 hrs | 6-8 hrs |
| **Intermediate** | 4-5 hrs | 4-5 hrs | 8-10 hrs |
| **Advanced** | 6-8 hrs | 6-8 hrs | 12-16 hrs |
| **All Exercises** | 13-17 hrs | 13-17 hrs | **26-34 hrs** |

---

## 🔗 Connections Between Exercises

```
Exercise Dependencies:
- Ex01 (Stock) → Ex06 (ABC) → Ex07 (Safety Stock)
- Ex03 (Demand) → Ex07 (Safety Stock) → Ex19 (Demand Analysis)
- Ex02 (Freight) → Ex04 (Distribution) → Ex08 (Routes)
- Ex05 (Supplier Perf) → Ex18 (Scorecard) → Ex20 (Risk)
- Ex11 (Transactions) → Ex14 (Orders) → Ex16 (Cost)
- Ex12 (Shipments) → Ex15 (Fulfillment) → Ex16 (Cost Analysis)
```

---

## 💻 System Requirements

- Python 3.7+
- NumPy 1.19+
- Pandas 1.1+
- No external dependencies beyond these

All exercises are self-contained and can run independently.

---

## 📝 Exercise Template Structure

Each exercise follows this pattern:

```python
"""Scenario description and learning objectives"""

import pandas as pd  # or numpy as np
import numpy as np

# 1. CREATE DATA
# Your data creation code

print("Analysis Title")
print("\n" + "="*80)

# 2. EXPLORE DATA
# Show raw data, shapes, types

# 3. ANALYSIS
# Task 1, Task 2, etc.

# 4. INSIGHTS
# Summary of findings

# 5. RECOMMENDATIONS
# Action items based on analysis
```

---

## 🎯 Success Criteria

By completing these exercises, you will be able to:

✅ Create and manipulate NumPy arrays for supply chain calculations
✅ Perform aggregations and filtering on large datasets
✅ Create and analyze Pandas DataFrames for business data
✅ Merge and combine data from multiple sources
✅ Calculate performance metrics and KPIs
✅ Identify patterns, trends, and anomalies
✅ Rank and classify items by multiple criteria
✅ Generate business-relevant insights and recommendations
✅ Apply statistics to real-world supply chain problems
✅ Create data-driven decision support analyses

---

## 🔗 Related Resources

- **NumPy Documentation:** https://numpy.org/doc/
- **Pandas Documentation:** https://pandas.pydata.org/docs/
- **Supply Chain Management:** Industry-specific applications
- **Data Science:** Foundation for ML/AI in supply chains
- **Business Analytics:** Turning data into decisions

---

**Total Exercises:** 20 (10 NumPy + 10 Pandas)
**Total Code:** 2000+ lines
**Estimated Learning Time:** 26-34 hours
**Real-World Applicability:** ⭐⭐⭐⭐⭐

Happy learning! 🚀
