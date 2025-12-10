"""
Exercise 10: Supply Chain Risk Assessment and Mitigation

Real-world scenario: Identify and evaluate supply chain risks including 
supplier concentration, geopolitical factors, and operational vulnerabilities.

Task:
1. Create supplier and geographic risk data
2. Assess supplier concentration risk
3. Evaluate geopolitical and operational risks
4. Calculate overall supply chain risk score
5. Identify critical dependencies
6. Generate risk mitigation recommendations
"""

import pandas as pd
import numpy as np

# Create supplier risk data
suppliers = pd.DataFrame({
    'Supplier_ID': [f'SUPP-{i:03d}' for i in range(1, 26)],
    'Supplier_Name': [f'Supplier {chr(65+i%26)}{i//26}' for i in range(25)],
    'Country': np.random.choice(['USA', 'China', 'India', 'Vietnam', 'Germany', 'Japan'], 25),
    'Product_Category': np.random.choice(['Electronics', 'Raw Materials', 'Packaging', 'Components'], 25),
    'Annual_Spend': np.random.uniform(50000, 500000, 25),
    'Years_in_Partnership': np.random.randint(1, 15, 25),
    'Financial_Health_Score': np.random.uniform(60, 100, 25),
    'On_Time_Delivery_%': np.random.uniform(70, 99, 25),
    'Quality_Score': np.random.uniform(70, 100, 25),
    'Backup_Supplier_Available': np.random.choice([True, False], 25, p=[0.4, 0.6])
})

# Create geopolitical risk data by country
geo_risk = pd.DataFrame({
    'Country': ['USA', 'China', 'India', 'Vietnam', 'Germany', 'Japan'],
    'Political_Stability': [85, 60, 65, 70, 90, 85],
    'Trade_Risk': [40, 75, 50, 55, 35, 40],
    'Currency_Risk': [30, 65, 60, 55, 25, 30],
    'Supply_Chain_Risk_Exposure': [35, 80, 60, 65, 25, 30]
})

# Create product category critical importance
product_importance = pd.DataFrame({
    'Product_Category': ['Electronics', 'Raw Materials', 'Packaging', 'Components'],
    'Criticality_Score': [95, 90, 60, 85],
    'Lead_Time_Days': [21, 14, 7, 14],
    'Substitutability': [40, 35, 80, 50]  # How easy to substitute
})

print("Supply Chain Risk Assessment and Mitigation")
print("\n" + "="*80)

print("\nSupplier Risk Data:")
print(suppliers.head(10))

print("\n\nGeopolitical Risk by Country:")
print(geo_risk)

print("\n" + "="*80)

# Task 1: Assess supplier concentration risk
print("\nSupplier Concentration Risk Analysis:")

# Supplier concentration (Herfindahl index)
total_spend = suppliers['Annual_Spend'].sum()
supplier_weights = (suppliers['Annual_Spend'] / total_spend).values
herfindahl = (supplier_weights ** 2).sum()

print(f"\nTotal Annual Spend: ${total_spend:,.0f}")
print(f"Herfindahl Index: {herfindahl:.4f}")

if herfindahl > 0.25:
    risk_level = "HIGH - Excessive concentration with few suppliers"
elif herfindahl > 0.15:
    risk_level = "MODERATE - Some concentration risk"
else:
    risk_level = "LOW - Well-diversified supplier base"

print(f"Risk Assessment: {risk_level}")

# Top suppliers concentration
top_5_spend = suppliers.nlargest(5, 'Annual_Spend')['Annual_Spend'].sum()
top_5_pct = (top_5_spend / total_spend) * 100

print(f"\nTop 5 Suppliers: {top_5_pct:.1f}% of total spend")
print("Top 5 Suppliers:")
for idx, (i, row) in enumerate(suppliers.nlargest(5, 'Annual_Spend').iterrows(), 1):
    pct = (row['Annual_Spend'] / total_spend) * 100
    print(f"  {idx}. {row['Supplier_Name']}: ${row['Annual_Spend']:,.0f} ({pct:.1f}%)")

# Task 2: Evaluate geopolitical risks
print("\n\n" + "="*80)
print("\nGeopolitical Risk Evaluation:")

# Merge supplier and geo risk data
suppliers_with_geo = suppliers.merge(geo_risk, on='Country', how='left')

print("\nCountry Risk Profile:")
print(geo_risk.sort_values('Supply_Chain_Risk_Exposure', ascending=False))

# Identify high-risk country exposures
print("\n\nSuppliers in High-Risk Countries:")
high_risk_countries = geo_risk[geo_risk['Supply_Chain_Risk_Exposure'] >= 60]['Country'].values
high_risk_suppliers = suppliers_with_geo[suppliers_with_geo['Country'].isin(high_risk_countries)]

if len(high_risk_suppliers) > 0:
    high_risk_spend = high_risk_suppliers['Annual_Spend'].sum()
    high_risk_pct = (high_risk_spend / total_spend) * 100
    
    print(f"Suppliers in high-risk countries: {len(high_risk_suppliers)}")
    print(f"Annual spend exposure: ${high_risk_spend:,.0f} ({high_risk_pct:.1f}%)")
    print("\nBreakdown by country:")
    for country in high_risk_countries:
        country_suppliers = high_risk_suppliers[high_risk_suppliers['Country'] == country]
        country_spend = country_suppliers['Annual_Spend'].sum()
        country_risk = geo_risk[geo_risk['Country'] == country]['Supply_Chain_Risk_Exposure'].values[0]
        print(f"  {country}: {len(country_suppliers)} suppliers, ${country_spend:,.0f} (Risk: {country_risk})")
else:
    print("No critical high-risk country exposures identified")

# Task 3: Calculate supplier-specific risk scores
print("\n\n" + "="*80)
print("\nSupplier Risk Score Calculation:")

# Risk factors
suppliers_with_geo['Financial_Risk'] = 100 - suppliers_with_geo['Financial_Health_Score']
suppliers_with_geo['Operational_Risk'] = 100 - (
    (suppliers_with_geo['On_Time_Delivery_%'] + suppliers_with_geo['Quality_Score']) / 2
)
suppliers_with_geo['Geo_Risk'] = suppliers_with_geo['Supply_Chain_Risk_Exposure']
suppliers_with_geo['Concentration_Risk'] = (suppliers_with_geo['Annual_Spend'] / total_spend) * 100 * 5

# Backup availability risk
suppliers_with_geo['Backup_Risk'] = suppliers_with_geo['Backup_Supplier_Available'].apply(
    lambda x: 0 if x else 40
)

# Overall supplier risk score (0-100, higher = more risky)
suppliers_with_geo['Overall_Risk_Score'] = (
    suppliers_with_geo['Financial_Risk'] * 0.25 +
    suppliers_with_geo['Operational_Risk'] * 0.25 +
    suppliers_with_geo['Geo_Risk'] * 0.25 +
    suppliers_with_geo['Backup_Risk'] * 0.15 +
    suppliers_with_geo['Concentration_Risk'].clip(0, 100) * 0.10
).round(1)

# Classify risk
def classify_risk(score):
    if score >= 70:
        return 'CRITICAL'
    elif score >= 50:
        return 'HIGH'
    elif score >= 30:
        return 'MODERATE'
    else:
        return 'LOW'

suppliers_with_geo['Risk_Category'] = suppliers_with_geo['Overall_Risk_Score'].apply(classify_risk)

print("\nSupplier Risk Scorecard (Top 10 by Risk):")
risk_scorecard = suppliers_with_geo[[
    'Supplier_Name', 'Country', 'Annual_Spend', 'Overall_Risk_Score', 'Risk_Category'
]].sort_values('Overall_Risk_Score', ascending=False).head(10)

for col in ['Annual_Spend']:
    risk_scorecard[col] = risk_scorecard[col].apply(lambda x: f"${x:,.0f}")
    
print(risk_scorecard.to_string(index=False))

# Risk distribution
print("\n\nRisk Distribution:")
risk_dist = suppliers_with_geo['Risk_Category'].value_counts()
for risk_level in ['CRITICAL', 'HIGH', 'MODERATE', 'LOW']:
    count = risk_dist.get(risk_level, 0)
    items = suppliers_with_geo[suppliers_with_geo['Risk_Category'] == risk_level]
    spend = items['Annual_Spend'].sum()
    pct = (spend / total_spend) * 100 if total_spend > 0 else 0
    
    print(f"\n{risk_level}: {count} suppliers")
    print(f"  Spend: ${spend:,.0f} ({pct:.1f}%)")

# Task 4: Identify critical dependencies
print("\n\n" + "="*80)
print("\nCritical Dependency Analysis:")

# Merge with product importance
suppliers_with_risk = suppliers_with_geo.merge(product_importance, 
                                               left_on='Product_Category', 
                                               right_on='Product_Category', 
                                               how='left')

# Calculate criticality
suppliers_with_risk['Criticality_Score'] = (
    suppliers_with_risk['Overall_Risk_Score'] * suppliers_with_risk['Criticality_Score'] / 100
)

print("\nCritical Risk Items (High Risk + High Importance):")
critical = suppliers_with_risk[
    (suppliers_with_risk['Overall_Risk_Score'] >= 50) & 
    (suppliers_with_risk['Criticality_Score'] >= 50)
].nlargest(10, 'Criticality_Score')[
    ['Supplier_Name', 'Product_Category', 'Country', 'Overall_Risk_Score', 'Criticality_Score']
]

if len(critical) > 0:
    print(f"Identified {len(critical)} critical risk items:")
    for idx, (i, row) in enumerate(critical.iterrows(), 1):
        print(f"\n{idx}. {row['Supplier_Name']}")
        print(f"   Category: {row['Product_Category']}")
        print(f"   Country: {row['Country']}")
        print(f"   Risk Score: {row['Overall_Risk_Score']:.1f}")
else:
    print("No critical dependencies identified")

# Task 5: Single points of failure
print("\n\n" + "="*80)
print("\nSingle Point of Failure Analysis:")

for category in product_importance['Product_Category'].unique():
    category_suppliers = suppliers_with_risk[suppliers_with_risk['Product_Category'] == category]
    
    if len(category_suppliers) == 1:
        print(f"\n⚠ {category}: SINGLE SUPPLIER")
        supplier = category_suppliers.iloc[0]
        print(f"   Supplier: {supplier['Supplier_Name']}")
        print(f"   Risk Score: {supplier['Overall_Risk_Score']:.1f}")
        print(f"   Action: CRITICAL - Immediately develop alternative sourcing")
    
    elif len(category_suppliers) < 3:
        print(f"\n⚠ {category}: LIMITED SUPPLIERS ({len(category_suppliers)})")
        print(f"   Action: URGENT - Develop additional supplier relationships")

# Task 6: Risk mitigation strategies
print("\n\n" + "="*80)
print("\nRisk Mitigation Strategies and Recommendations:")

# Critical risk items requiring action
critical_items = suppliers_with_risk[suppliers_with_risk['Overall_Risk_Score'] >= 70]
high_risk_items = suppliers_with_risk[suppliers_with_risk['Overall_Risk_Score'] >= 50]

print(f"\n1. IMMEDIATE ACTIONS (Critical Risk - {len(critical_items)} items):")
if len(critical_items) > 0:
    for idx, (i, row) in enumerate(critical_items.iterrows(), 1):
        print(f"\n   a) {row['Supplier_Name']}:")
        
        if not row['Backup_Supplier_Available']:
            print(f"      • Develop backup supplier for {row['Product_Category']}")
        
        if row['Overall_Risk_Score'] >= 70 and row['Supply_Chain_Risk_Exposure'] >= 70:
            print(f"      • Consider alternative countries for sourcing")
        
        if row['Financial_Risk'] >= 40:
            print(f"      • Evaluate financial stability of supplier")
        
        print(f"      • Timeline: 30-60 days")

print(f"\n2. SHORT-TERM ACTIONS (High Risk - {len(high_risk_items)} items):")
print("   • Establish backup suppliers")
print("   • Increase safety stock for critical items")
print("   • Implement closer monitoring and audits")
print("   • Timeline: 60-90 days")

print(f"\n3. MEDIUM-TERM ACTIONS (0-6 months):")
print("   • Diversify supplier base geographically")
print("   • Implement supplier development programs")
print("   • Establish vendor-managed inventory for critical items")
print("   • Create disaster recovery plans")

print(f"\n4. LONG-TERM STRATEGY (6+ months):")
print("   • Develop nearshoring/reshoring strategy")
print("   • Implement supply chain visibility tools")
print("   • Create supplier resilience index")
print("   • Build strategic partnerships")

# Summary metrics
print("\n\n" + "="*80)
print("\nSupply Chain Risk Summary:")
print(f"\n• Overall Risk Level: {'CRITICAL' if len(critical) > 5 else 'HIGH' if len(high_risk_items) > 10 else 'MODERATE'}")
print(f"• Suppliers at Critical Risk: {len(critical_items)}")
print(f"• Suppliers at High Risk: {len(high_risk_items)}")
print(f"• Geographic Concentration: {len(suppliers_with_geo['Country'].unique())} countries")
print(f"• Critical Single-Source Items: {len(suppliers_with_risk[suppliers_with_risk.groupby('Product_Category').Product_Category.transform('size') == 1])}")
print(f"• High-Risk Geopolitical Exposure: {(high_risk_spend / total_spend * 100):.1f}% of spend")
print(f"\n• Recommended Priority Actions: {len(critical_items) + len(suppliers_with_risk[suppliers_with_risk.groupby('Product_Category').Product_Category.transform('size') == 1])}")
