"""
Exercise 08: Supplier Quality and Reliability Scorecard

Real-world scenario: Create comprehensive supplier performance scorecards 
combining quality metrics, reliability, cost, and responsiveness.

Task:
1. Create supplier performance data across multiple dimensions
2. Calculate individual performance scores
3. Create weighted overall scorecard
4. Identify top and underperforming suppliers
5. Trend analysis of supplier performance
6. Generate supplier recommendations and rankings
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create supplier performance data
suppliers = pd.DataFrame({
    'Supplier_ID': [f'SUPP-{i:03d}' for i in range(1, 21)],
    'Supplier_Name': [f'Supplier {chr(65+i%26)}{i//26}' for i in range(20)],
    'Category': np.random.choice(['Electronics', 'Raw Materials', 'Packaging'], 20),
    'Active': [True] * 20,
    'Contract_Start': [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1095)) for _ in range(20)]
})

# Create performance metrics
performance = pd.DataFrame({
    'Supplier_ID': suppliers['Supplier_ID'],
    
    # Quality metrics (0-100)
    'Quality_Score': np.random.uniform(75, 100, 20),
    'Defect_Rate_%': np.random.uniform(0.1, 5, 20),
    'Reject_Rate_%': np.random.uniform(0, 3, 20),
    
    # Delivery metrics (0-100)
    'On_Time_Rate_%': np.random.uniform(70, 99, 20),
    'Lead_Time_Days': np.random.randint(3, 30, 20),
    'Lead_Time_Compliance': np.random.uniform(70, 100, 20),
    
    # Cost metrics (0-100, higher = better cost)
    'Price_Competitiveness': np.random.uniform(60, 100, 20),
    'Cost_Trend': np.random.uniform(-5, 5, 20),  # % change
    
    # Service metrics (0-100)
    'Responsiveness_Score': np.random.uniform(70, 100, 20),
    'Communication_Score': np.random.uniform(70, 100, 20),
    
    # Volume metrics
    'Annual_Orders': np.random.randint(10, 500, 20),
    'Annual_Spend': np.random.uniform(50000, 500000, 20)
})

# Merge supplier and performance data
supplier_scorecard = suppliers.merge(performance, on='Supplier_ID')

print("Supplier Quality and Reliability Scorecard")
print("\n" + "="*80)

print("\nSupplier Base Overview:")
print(f"Total Active Suppliers: {len(supplier_scorecard)}")
print(f"Categories: {', '.join(supplier_scorecard['Category'].unique())}")
print(f"Total Annual Spend: ${supplier_scorecard['Annual_Spend'].sum():,.0f}")

print("\n\nSupplier Data Sample:")
print(supplier_scorecard[['Supplier_ID', 'Supplier_Name', 'Category', 'Quality_Score', 
                          'On_Time_Rate_%', 'Price_Competitiveness']].head(10))

print("\n" + "="*80)

# Task 1: Calculate individual performance dimensions
print("\n\nPerformance Dimensions Summary:")

quality_metrics = supplier_scorecard[['Supplier_ID', 'Quality_Score', 'Defect_Rate_%', 'Reject_Rate_%']]
delivery_metrics = supplier_scorecard[['Supplier_ID', 'On_Time_Rate_%', 'Lead_Time_Compliance']]
cost_metrics = supplier_scorecard[['Supplier_ID', 'Price_Competitiveness', 'Cost_Trend']]
service_metrics = supplier_scorecard[['Supplier_ID', 'Responsiveness_Score', 'Communication_Score']]

print("\n1. Quality Dimension Average:")
print(f"   Overall Quality Score: {supplier_scorecard['Quality_Score'].mean():.1f}/100")
print(f"   Average Defect Rate: {supplier_scorecard['Defect_Rate_%'].mean():.2f}%")
print(f"   Average Reject Rate: {supplier_scorecard['Reject_Rate_%'].mean():.2f}%")

print("\n2. Delivery Dimension Average:")
print(f"   Overall On-Time Rate: {supplier_scorecard['On_Time_Rate_%'].mean():.1f}%")
print(f"   Average Lead Time: {supplier_scorecard['Lead_Time_Days'].mean():.0f} days")
print(f"   Average Lead Time Compliance: {supplier_scorecard['Lead_Time_Compliance'].mean():.1f}%")

print("\n3. Cost Dimension Average:")
print(f"   Overall Price Competitiveness: {supplier_scorecard['Price_Competitiveness'].mean():.1f}/100")
print(f"   Average Cost Trend: {supplier_scorecard['Cost_Trend'].mean():.2f}%")

print("\n4. Service Dimension Average:")
print(f"   Overall Responsiveness: {supplier_scorecard['Responsiveness_Score'].mean():.1f}/100")
print(f"   Overall Communication: {supplier_scorecard['Communication_Score'].mean():.1f}/100")

# Task 2: Create weighted overall scorecard
print("\n\n" + "="*80)
print("\nWeighted Overall Performance Scorecard:")

# TODO: Calculate weighted dimension scores (Quality, Delivery, Cost, Service)
supplier_scorecard['Quality_Dimension'] = None  # FILL IN
supplier_scorecard['Delivery_Dimension'] = None  # FILL IN
supplier_scorecard['Cost_Dimension'] = None  # FILL IN
supplier_scorecard['Service_Dimension'] = None  # FILL IN
supplier_scorecard['Overall_Score'] = None  # FILL IN

print("\nSupplier Performance Scorecard (sorted by Overall Score):")
print("TODO: Display weighted scorecard")

# Task 3: Classify suppliers by performance
print("\n\n" + "="*80)
print("\nSupplier Classification:")

def classify_supplier(score):
    if score >= 85:
        return 'Preferred'
    elif score >= 75:
        return 'Approved'
    elif score >= 65:
        return 'Conditional'
    else:
        return 'At Risk'

supplier_scorecard['Classification'] = supplier_scorecard['Overall_Score'].apply(classify_supplier)

classification_summary = supplier_scorecard['Classification'].value_counts()
print("\nSuppliers by Classification:")
for classification in ['Preferred', 'Approved', 'Conditional', 'At Risk']:
    count = classification_summary.get(classification, 0)
    items = supplier_scorecard[supplier_scorecard['Classification'] == classification]
    total_spend = items['Annual_Spend'].sum()
    avg_score = items['Overall_Score'].mean()
    
    print(f"\n{classification}: {count} suppliers")
    print(f"  Total Spend: ${total_spend:,.0f}")
    print(f"  Average Score: {avg_score:.1f}/100")
    if count > 0:
        print(f"  Examples: {', '.join(items['Supplier_Name'].head(3).values)}")

# Task 4: Identify top and underperforming
print("\n\n" + "="*80)
print("\nTop Performing Suppliers:")

top_5 = supplier_scorecard.nlargest(5, 'Overall_Score')[
    ['Supplier_Name', 'Category', 'Overall_Score', 'Quality_Dimension', 'Delivery_Dimension', 
     'Cost_Dimension', 'Service_Dimension', 'Annual_Spend']
]
print(top_5.round(1).to_string(index=False))

print("\n\nAt-Risk Suppliers Requiring Attention:")

at_risk = supplier_scorecard[supplier_scorecard['Classification'].isin(['Conditional', 'At Risk'])].nlargest(5, 'Annual_Spend')[
    ['Supplier_Name', 'Category', 'Overall_Score', 'Quality_Dimension', 'Delivery_Dimension', 
     'Cost_Dimension', 'Service_Dimension', 'Annual_Spend']
]

if len(at_risk) > 0:
    print(at_risk.round(1).to_string(index=False))
else:
    print("No at-risk suppliers with significant spend")

# Task 5: Category performance analysis
print("\n\n" + "="*80)
print("\nPerformance by Category:")

category_performance = supplier_scorecard.groupby('Category').agg({
    'Supplier_Name': 'count',
    'Overall_Score': ['mean', 'min', 'max'],
    'Quality_Dimension': 'mean',
    'Delivery_Dimension': 'mean',
    'Annual_Spend': 'sum'
}).round(2)

category_performance.columns = ['Supplier_Count', 'Avg_Overall', 'Min_Score', 'Max_Score', 
                               'Avg_Quality', 'Avg_Delivery', 'Total_Spend']
print(category_performance)

# Task 6: Recommendations and action plan
print("\n\n" + "="*80)
print("\nRecommendations and Action Plan:")

print("\n1. PREFERRED SUPPLIERS (Score ≥85):")
preferred = supplier_scorecard[supplier_scorecard['Classification'] == 'Preferred']
if len(preferred) > 0:
    print(f"   • {len(preferred)} preferred suppliers identified")
    print(f"   • Combined spend: ${preferred['Annual_Spend'].sum():,.0f}")
    print("   • Recommended actions:")
    print("     - Increase order volume to take advantage of better terms")
    print("     - Consider long-term strategic partnerships")
    print("     - Negotiate volume discounts")

print("\n2. APPROVED SUPPLIERS (Score 75-84):")
approved = supplier_scorecard[supplier_scorecard['Classification'] == 'Approved']
if len(approved) > 0:
    print(f"   • {len(approved)} approved suppliers")
    print(f"   • Combined spend: ${approved['Annual_Spend'].sum():,.0f}")
    print("   • Recommended actions:")
    print("     - Maintain current relationship")
    print("     - Monitor performance quarterly")
    print("     - Identify improvement areas")

print("\n3. CONDITIONAL SUPPLIERS (Score 65-74):")
conditional = supplier_scorecard[supplier_scorecard['Classification'] == 'Conditional']
if len(conditional) > 0:
    print(f"   • {len(conditional)} conditional suppliers")
    print(f"   • Combined spend: ${conditional['Annual_Spend'].sum():,.0f}")
    print("   • Recommended actions:")
    print("     - Develop improvement plan with supplier")
    print("     - Increase order monitoring")
    print("     - Set performance targets")

print("\n4. AT-RISK SUPPLIERS (Score <65):")
risk = supplier_scorecard[supplier_scorecard['Classification'] == 'At Risk']
if len(risk) > 0:
    print(f"   • {len(risk)} at-risk suppliers")
    print(f"   • Combined spend: ${risk['Annual_Spend'].sum():,.0f}")
    print("   • Recommended actions:")
    print("     - Immediate performance review meeting")
    print("     - Create 90-day corrective action plan")
    print("     - Consider alternate suppliers")
    print("     - Plan transition if no improvement")

print("\n5. COST OPTIMIZATION:")
high_cost = supplier_scorecard[supplier_scorecard['Cost_Dimension'] < 70]
if len(high_cost) > 0:
    print(f"   • {len(high_cost)} suppliers have cost concerns")
    print(f"   • Potential savings target: 5-10% of spend")
    print("   • Actions:")
    print("     - Negotiate volume discounts")
    print("     - Benchmark against competitors")
    print("     - Consider consolidation opportunities")

print("\n6. QUALITY FOCUS:")
quality_concerns = supplier_scorecard[supplier_scorecard['Quality_Dimension'] < 80]
if len(quality_concerns) > 0:
    print(f"   • {len(quality_concerns)} suppliers need quality improvement")
    print("   • Actions:")
    print("     - Implement quality audits")
    print("     - Establish quality metrics")
    print("     - Provide training if needed")

print("\n\nSummary Metrics:")
print(f"• Supplier Health Score (Network Average): {supplier_scorecard['Overall_Score'].mean():.1f}/100")
print(f"• Suppliers Performing Above Target (≥75): {len(supplier_scorecard[supplier_scorecard['Overall_Score'] >= 75])}")
print(f"• High-Risk Suppliers: {len(supplier_scorecard[supplier_scorecard['Overall_Score'] < 65])}")
print(f"• Recommended action items: {len(at_risk) + len(quality_concerns) + len(high_cost)}")
