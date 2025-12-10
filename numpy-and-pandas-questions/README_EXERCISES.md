## NumPy and Pandas Supply Chain Exercises - Complete Collection

### Overview
This collection contains **20 comprehensive exercises** (10 NumPy + 10 Pandas) focused on **real-world supply chain scenarios**. Each exercise integrates concepts from the NumPy and Pandas tutorial material and applies them to practical supply chain and logistics problems.

---

## NumPy Exercises (01-10)

### 01__numpy__inventory_stock_levels.py
**Scenario:** Warehouse stock level analysis across distribution centers
**Key Concepts:** 2D arrays, aggregation functions, boolean masks, axis operations
**Learning Objectives:**
- Work with multi-dimensional arrays (products × distribution centers)
- Calculate statistics across different axes (by product, by location)
- Use boolean indexing to identify items meeting specific criteria
- Calculate derived metrics (reorder quantities, inventory value)

**Skills Practiced:** Array creation, slicing, aggregation (sum, mean, min, max), boolean masking

---

### 02__numpy__freight_cost_optimization.py
**Scenario:** Shipping cost calculation with freight class multipliers
**Key Concepts:** Broadcasting, fancy indexing, vectorized operations, cost analysis
**Learning Objectives:**
- Apply broadcasting to perform element-wise operations on arrays of different shapes
- Use fancy indexing to apply conditional multipliers
- Calculate costs and optimize routes
- Identify cost-effective shipping options

**Skills Practiced:** Broadcasting, fancy indexing, element-wise multiplication, sorting

---

### 03__numpy__demand_forecasting.py
**Scenario:** Historical demand analysis with moving averages and trend analysis
**Key Concepts:** Time series analysis, moving averages, standardization, forecasting
**Learning Objectives:**
- Calculate moving averages for trend identification
- Compute growth rates and seasonal variations
- Normalize data for comparison across products
- Project future demand using linear regression

**Skills Practiced:** Slicing for windows, aggregation, normalization (Z-score), polyfit, trend analysis

---

### 04__numpy__warehouse_distribution.py
**Scenario:** Multi-warehouse distribution optimization
**Key Concepts:** Matrix operations, broadcasting, constraint satisfaction
**Learning Objectives:**
- Model supply-demand problems using matrices
- Find minimum cost solutions using matrix operations
- Analyze capacity utilization across facilities
- Optimize product allocation across warehouses

**Skills Practiced:** 2D arrays, matrix operations, sum with axis parameter, conditional assignment

---

### 05__numpy__supplier_performance.py
**Scenario:** Supplier evaluation with multi-dimensional scoring
**Key Concepts:** Normalization, weighted scoring, ranking, outlier detection
**Learning Objectives:**
- Normalize different metrics to common scale (0-100)
- Calculate weighted overall scores from multiple dimensions
- Identify outliers using z-scores
- Rank and classify suppliers based on performance

**Skills Practiced:** Normalization (min-max), weighted averaging, argsort, z-score calculation, fancy indexing

---

### 06__numpy__abc_inventory_analysis.py
**Scenario:** ABC inventory analysis (Pareto principle)
**Key Concepts:** Sorting, cumulative sums, classification, conditional filtering
**Learning Objectives:**
- Rank inventory items by value
- Calculate cumulative percentages
- Classify items as A/B/C based on value concentration
- Apply Pareto principle (80-20 rule) to inventory management

**Skills Practiced:** argsort with reverse, cumsum, boolean array filtering, value_counts equivalent

---

### 07__numpy__lead_time_safety_stock.py
**Scenario:** Safety stock calculation based on demand variability
**Key Concepts:** Standard deviation, normal distribution, lead time analysis
**Learning Objectives:**
- Calculate demand statistics and variability metrics
- Compute safety stock for different service levels
- Calculate reorder points considering lead time
- Analyze cost-service tradeoffs

**Skills Practiced:** Statistical functions (mean, std, sqrt), array operations with lead times, scalar multiplication

---

### 08__numpy__route_optimization.py
**Scenario:** Delivery route optimization using distance matrices
**Key Concepts:** Distance matrix operations, path optimization, permutations
**Learning Objectives:**
- Analyze distance matrices for optimal routes
- Calculate total distances for different sequences
- Find shortest paths using sorting
- Estimate fuel costs and delivery times

**Skills Practiced:** Matrix indexing, sum operations, looping with permutations, argmin/argsort

---

### 09__numpy__warehouse_capacity.py
**Scenario:** Warehouse capacity planning and utilization analysis
**Key Concepts:** Volume calculations, utilization rates, growth projections
**Learning Objectives:**
- Calculate warehouse volumes from dimensions
- Analyze current and projected capacity utilization
- Identify capacity constraints and bottlenecks
- Project future needs based on growth rates

**Skills Practiced:** Element-wise multiplication (volume calculation), division for percentages, exponentiation for growth

---

### 10__numpy__product_mix_optimization.py
**Scenario:** Product profitability analysis and optimal product mix
**Key Concepts:** Profit calculations, margin analysis, ranking, constraint analysis
**Learning Objectives:**
- Calculate unit and total profits for products
- Analyze profit margins and contribution metrics
- Rank products by multiple criteria (profitability, growth, margin)
- Recommend optimal product mix for maximum profit

**Skills Practiced:** Subtraction for profit, division for percentages, ranking (argsort), conditional selection

---

## Pandas Exercises (11-20)

### 11__pandas__transaction_analysis.py
**Scenario:** Supply chain transaction ledger analysis
**Key Concepts:** DataFrame creation, groupby, aggregation, pivot tables
**Learning Objectives:**
- Create and manipulate transaction DataFrames
- Group transactions by vendor and product
- Analyze patterns in procurement
- Identify high-value transactions

**Skills Practiced:** DataFrame creation, groupby with multiple aggregations, pivot_table, filtering

---

### 12__pandas__shipment_tracking.py
**Scenario:** Shipment performance and delivery tracking
**Key Concepts:** Date/time operations, status tracking, performance metrics
**Learning Objectives:**
- Track shipment status and performance
- Calculate on-time delivery rates
- Analyze delays and exceptions
- Create carrier performance reports

**Skills Practiced:** datetime operations, boolean filtering, groupby with custom calculations, sorting

---

### 13__pandas__inventory_cleaning.py
**Scenario:** Data cleaning and standardization from multiple sources
**Key Concepts:** Missing value handling, data type conversion, standardization
**Learning Objectives:**
- Identify and handle missing values appropriately
- Standardize text formatting and data types
- Remove duplicates
- Create data quality metrics

**Skills Practiced:** isnull/notnull, fillna, pd.to_numeric, pd.to_datetime, drop_duplicates, data type conversion

---

### 14__pandas__multi_location_orders.py
**Scenario:** Purchase order analysis across multiple locations
**Key Concepts:** Merging DataFrames, multi-level grouping, cross-location analysis
**Learning Objectives:**
- Merge supplier data with order information
- Analyze order patterns by location and supplier
- Identify consolidation opportunities
- Calculate budget utilization by location

**Skills Practiced:** merge (different join types), groupby with multiple columns, pivot_table, budget analysis

---

### 15__pandas__customer_order_fulfillment.py
**Scenario:** Customer order fulfillment and satisfaction analysis
**Key Concepts:** Customer segmentation, performance metrics, trend analysis
**Learning Objectives:**
- Analyze order fulfillment rates by customer segment
- Calculate on-time delivery performance
- Identify high-value and at-risk customers
- Generate recommendations for customer retention

**Skills Practiced:** merge, groupby with lambda functions, nlargest, filtering, segment analysis

---

### 16__pandas__cost_analysis_benchmarking.py
**Scenario:** Comprehensive supply chain cost analysis with benchmarking
**Key Concepts:** Cost aggregation, variance analysis, efficiency metrics
**Learning Objectives:**
- Categorize and aggregate supply chain costs
- Perform variance analysis (actual vs budget)
- Benchmark costs against industry standards
- Identify cost reduction opportunities

**Skills Practiced:** groupby with multiple aggregations, DataFrame operations, custom calculations, variance analysis

---

### 17__pandas__inventory_aging.py
**Scenario:** Inventory aging and obsolescence analysis
**Key Concepts:** Age classification, risk scoring, disposition strategies
**Learning Objectives:**
- Classify inventory by age and movement
- Calculate obsolescence risk scores
- Recommend disposition strategies
- Estimate financial impact of obsolete inventory

**Skills Practiced:** apply with custom functions, classification logic, calculated risk scores, conditional recommendations

---

### 18__pandas__supplier_scorecard.py
**Scenario:** Comprehensive supplier performance scorecard
**Key Concepts:** Weighted scoring, multi-dimensional evaluation, supplier ranking
**Learning Objectives:**
- Create multi-dimensional performance scores
- Calculate weighted overall supplier ratings
- Classify suppliers by performance tier
- Generate actionable recommendations

**Skills Practiced:** apply with complex calculations, groupby aggregation, weighted scoring, custom classifications

---

### 19__pandas__demand_analysis.py
**Scenario:** Demand pattern analysis with seasonality and forecasting
**Key Concepts:** Demand patterns, seasonality indices, forecast generation, volatility analysis
**Learning Objectives:**
- Analyze historical demand patterns
- Calculate seasonality indices
- Generate demand forecasts
- Recommend safety stock levels

**Skills Practiced:** groupby by date periods, rolling calculations, seasonal decomposition, forecast methods

---

### 20__pandas__risk_assessment.py
**Scenario:** Supply chain risk assessment and mitigation
**Key Concepts:** Risk scoring, supplier concentration, geopolitical analysis
**Learning Objectives:**
- Calculate multi-factor risk scores
- Assess supplier concentration risk
- Evaluate geopolitical exposures
- Create risk mitigation strategies

**Skills Practiced:** merge with complex logic, risk score calculations, groupby for concentration analysis, critical dependency identification

---

## Naming Convention

All files follow the pattern: `XX__[numpy|pandas]__exercise_name.py`

Where:
- `XX` = Exercise number (01-20)
- `[numpy|pandas]` = Framework used
- `exercise_name` = Descriptive kebab-case name

---

## Learning Progression

### Beginner (Exercises 1-5 NumPy, 11-13 Pandas)
Focus on basic array operations, DataFrame creation, and simple filtering
- Array creation and manipulation
- Basic aggregations
- Simple filtering and selection
- Data type basics

### Intermediate (Exercises 6-8 NumPy, 14-16 Pandas)
Advanced array operations, complex grouping, and business logic
- Multi-level operations
- Complex filtering conditions
- Merging and joining
- Cost and financial analysis

### Advanced (Exercises 9-10 NumPy, 17-20 Pandas)
Comprehensive business analysis and recommendations
- Risk assessment and scoring
- Predictive analysis and forecasting
- Multi-dimensional decision making
- Strategic recommendations

---

## Real-World Applications

Each exercise addresses actual supply chain challenges:

1. **Inventory Management** - Stock levels, aging, ABC analysis
2. **Procurement** - Purchase orders, supplier evaluation, consolidation
3. **Logistics** - Shipping costs, route optimization, delivery tracking
4. **Demand Planning** - Forecasting, seasonality, safety stock
5. **Cost Management** - Budget analysis, variance, benchmarking
6. **Risk Management** - Supplier concentration, geopolitical exposure
7. **Quality Control** - Supplier scorecards, performance metrics
8. **Operations** - Warehouse capacity, product mix, distribution

---

## How to Use These Exercises

### For Learning:
1. Start with exercises 01-05 (NumPy) to master array operations
2. Progress to exercises 11-13 (Pandas) for DataFrame fundamentals
3. Move to intermediate exercises (06-08, 14-16) for business applications
4. Complete advanced exercises (09-10, 17-20) for comprehensive analysis

### For Practice:
- Each exercise includes detailed comments and TODO sections
- Run the code and modify values to understand relationships
- Create variants of exercises with different data
- Combine concepts from multiple exercises

### For Reference:
- Use as templates for similar supply chain problems
- Copy the analysis patterns for your own datasets
- Reference the calculations and logic for your projects

---

## Key Concepts Summary

### NumPy Concepts Covered
- Array creation and manipulation (zeros, ones, arange, linspace, random)
- Indexing and slicing (basic, fancy, boolean)
- Broadcasting and vectorization
- Aggregation functions (sum, mean, min, max, std)
- Reshaping and transposing
- Linear algebra operations (polyfit, dot products implied)
- Statistical operations

### Pandas Concepts Covered
- Series and DataFrame creation
- Indexing and selection (.loc, .iloc, direct access)
- Groupby and aggregation (agg, transform)
- Merging and joining (merge, concat)
- Reshaping (pivot_table, melt, stack, unstack)
- Missing value handling (isnull, fillna, dropna)
- Boolean indexing and filtering
- Date/time operations
- Data cleaning and standardization

---

## Running the Exercises

```bash
# Run a specific exercise
python 01__numpy__inventory_stock_levels.py

# Run all NumPy exercises
for f in 0[1-9]__numpy*.py 10__numpy*.py; do python $f; done

# Run all Pandas exercises
for f in [1-2][0-9]__pandas*.py; do python $f; done

# Run all exercises
for f in *__*.py; do python $f; done
```

---

## Expected Output

Each exercise produces:
1. **Data Sample** - Shows the input/raw data
2. **Analysis Results** - Statistical summaries and findings
3. **Visualizations** (text-based) - Tables and formatted output
4. **Recommendations** - Actionable insights for decision making

---

## Difficulty Levels by Exercise

| Exercise | Topic | Difficulty | Primary Concept |
|----------|-------|-----------|-----------------|
| 01 | Inventory Levels | ⭐ Beginner | Aggregation |
| 02 | Freight Costs | ⭐ Beginner | Broadcasting |
| 03 | Demand Forecasting | ⭐⭐ Intermediate | Moving Averages |
| 04 | Warehouse Distribution | ⭐⭐ Intermediate | Matrix Operations |
| 05 | Supplier Performance | ⭐⭐ Intermediate | Normalization/Ranking |
| 06 | ABC Analysis | ⭐⭐ Intermediate | Sorting/Cumulative |
| 07 | Safety Stock | ⭐⭐⭐ Advanced | Statistics |
| 08 | Route Optimization | ⭐⭐⭐ Advanced | Path Finding |
| 09 | Capacity Planning | ⭐⭐⭐ Advanced | Projections |
| 10 | Product Mix | ⭐⭐⭐ Advanced | Multi-Criteria Optimization |
| 11 | Transactions | ⭐ Beginner | DataFrame Creation |
| 12 | Shipment Tracking | ⭐ Beginner | Datetime/Status |
| 13 | Data Cleaning | ⭐⭐ Intermediate | Data Quality |
| 14 | Multi-Location Orders | ⭐⭐ Intermediate | Merging/Grouping |
| 15 | Customer Fulfillment | ⭐⭐⭐ Advanced | Segmentation |
| 16 | Cost Analysis | ⭐⭐⭐ Advanced | Variance Analysis |
| 17 | Inventory Aging | ⭐⭐⭐ Advanced | Risk Scoring |
| 18 | Supplier Scorecard | ⭐⭐⭐ Advanced | Weighted Scoring |
| 19 | Demand Analysis | ⭐⭐⭐ Advanced | Seasonality |
| 20 | Risk Assessment | ⭐⭐⭐ Advanced | Multi-Factor Risk |

---

## Common Patterns Across Exercises

### Data Preparation
```python
# NumPy: Create arrays with random data
data = np.random.uniform(min, max, size)

# Pandas: Create DataFrames from dictionaries
df = pd.DataFrame({...})
```

### Aggregation
```python
# NumPy: Along axes
np.sum(array, axis=0)  # Sum columns
np.sum(array, axis=1)  # Sum rows

# Pandas: Group and aggregate
df.groupby('column').agg({'value': ['sum', 'mean']})
```

### Filtering
```python
# NumPy: Boolean masks
mask = array > threshold
result = array[mask]

# Pandas: Boolean indexing
filtered_df = df[df['column'] > threshold]
```

### Calculations
```python
# NumPy: Vectorized operations
result = (array1 * array2) + array3

# Pandas: Element-wise operations
df['new_col'] = df['col1'] * df['col2']
```

---

## Tips for Success

1. **Understand the data first** - Always examine the structure and values
2. **Start simple** - Get basic calculations working before complex operations
3. **Use intermediate variables** - Store results of calculations for clarity
4. **Print intermediate results** - Verify calculations at each step
5. **Test edge cases** - Try with different data values
6. **Read the comments** - Each section explains the business logic
7. **Modify and experiment** - Change parameters to understand relationships
8. **Create variants** - Apply the same logic to different datasets

---

## Next Steps After These Exercises

1. **Combine concepts** - Create larger analyses using multiple techniques
2. **Real data** - Apply these exercises to your actual supply chain data
3. **Visualization** - Add matplotlib or seaborn to create charts
4. **Automation** - Build ETL pipelines using these techniques
5. **Optimization** - Use SciPy to solve optimization problems
6. **Machine Learning** - Use scikit-learn for predictive models
7. **Database Integration** - Read/write data from SQL databases
8. **Reporting** - Generate automated reports from these analyses

---

**Created:** 2024
**Total Exercises:** 20 (10 NumPy + 10 Pandas)
**Total Code Lines:** ~2000+ lines of well-commented, production-quality code
**Estimated Learning Time:** 20-30 hours of hands-on practice

All exercises are designed to be self-contained, educational, and applicable to real supply chain scenarios.
