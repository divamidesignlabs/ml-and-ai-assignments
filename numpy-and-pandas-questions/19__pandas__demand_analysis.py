"""
Exercise 09: Demand Pattern Analysis and Forecasting

Real-world scenario: Analyze historical demand patterns across products and 
seasons to improve forecast accuracy and inventory planning.

Task:
1. Create historical demand data with seasonality
2. Identify demand patterns and trends
3. Calculate seasonality indices
4. Perform decomposition (trend, seasonal, residual)
5. Generate forecasts using simple methods
6. Analyze forecast accuracy and recommendations
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create historical demand data with seasonality
np.random.seed(42)

dates = pd.date_range('2021-01-01', periods=156, freq='W')  # 3 years of weekly data
products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E']

# Create demand data with seasonality
demand_data = []
for product in products:
    base_demand = np.random.uniform(500, 2000)
    trend = np.linspace(0, 300, len(dates))
    
    # Seasonal pattern (quarterly peaks)
    seasonality = np.array([np.sin(2 * np.pi * i / 52) * 300 for i in range(len(dates))])
    
    # Random noise
    noise = np.random.normal(0, base_demand * 0.1, len(dates))
    
    demand = base_demand + trend + seasonality + noise
    demand = np.maximum(demand, 0)  # No negative demand
    
    for i, date in enumerate(dates):
        demand_data.append({
            'Date': date,
            'Product': product,
            'Demand': demand[i]
        })

demand_df = pd.DataFrame(demand_data)

print("Demand Pattern Analysis and Forecasting")
print("\n" + "="*80)

print("\nHistorical Demand Data Summary:")
print(f"Date Range: {demand_df['Date'].min().date()} to {demand_df['Date'].max().date()}")
print(f"Products: {len(demand_df['Product'].unique())}")
print(f"Total Records: {len(demand_df)}")

print("\n\nDemand Data Sample:")
print(demand_df.head(15))

print("\n" + "="*80)

# Task 1: Analyze demand statistics by product
print("\nDemand Statistics by Product:")

product_stats = demand_df.groupby('Product')['Demand'].agg([
    ('Mean', 'mean'),
    ('Std_Dev', 'std'),
    ('Min', 'min'),
    ('Max', 'max'),
    ('CV_%', lambda x: (x.std() / x.mean()) * 100)
]).round(2)

product_stats = product_stats.sort_values('Mean', ascending=False)
print(product_stats)

# Task 2: Identify trends
print("\n\n" + "="*80)
print("\nTrend Analysis by Product:")

for product in demand_df['Product'].unique():
    product_data = demand_df[demand_df['Product'] == product].sort_values('Date')
    
    # Simple trend: compare first and last periods
    first_period = product_data.iloc[:13]['Demand'].mean()  # First quarter
    last_period = product_data.iloc[-13:]['Demand'].mean()  # Last quarter
    trend_pct = ((last_period - first_period) / first_period) * 100
    
    trend_direction = "↑ INCREASING" if trend_pct > 5 else "↓ DECREASING" if trend_pct < -5 else "→ STABLE"
    print(f"\n{product}: {trend_direction}")
    print(f"  First period average: {first_period:.0f}")
    print(f"  Last period average: {last_period:.0f}")
    print(f"  Change: {trend_pct:+.1f}%")

# Task 3: Calculate seasonality indices
print("\n\n" + "="*80)
print("\nSeasonality Analysis:")

# Group by month and calculate indices
demand_df['Month'] = demand_df['Date'].dt.month
demand_df['Quarter'] = demand_df['Date'].dt.quarter

quarterly_avg = demand_df.groupby(['Product', 'Quarter'])['Demand'].mean().unstack(fill_value=0)
print("\nAverage Demand by Quarter:")
print(quarterly_avg.round(0))

# Calculate seasonality indices (quarterly)
print("\n\nSeasonality Indices (Average = 100):")
for product in quarterly_avg.index:
    overall_avg = quarterly_avg.loc[product].mean()
    indices = (quarterly_avg.loc[product] / overall_avg * 100).round(1)
    print(f"\n{product}:")
    for quarter in range(1, 5):
        if quarter in indices.index:
            index = indices[quarter]
            strength = "HIGH" if index > 110 else "LOW" if index < 90 else "NORMAL"
            print(f"  Q{quarter}: {index} ({strength})")

# Task 4: Demand volatility and reliability
print("\n\n" + "="*80)
print("\nDemand Volatility and Reliability:")

for product in demand_df['Product'].unique():
    product_data = demand_df[demand_df['Product'] == product]['Demand']
    
    cv = (product_data.std() / product_data.mean()) * 100
    
    if cv < 15:
        reliability = "HIGHLY STABLE"
    elif cv < 30:
        reliability = "STABLE"
    elif cv < 50:
        reliability = "MODERATE VOLATILITY"
    else:
        reliability = "HIGH VOLATILITY"
    
    print(f"\n{product}:")
    print(f"  Coefficient of Variation: {cv:.1f}%")
    print(f"  Reliability: {reliability}")
    print(f"  Forecast Difficulty: {'Easy' if cv < 25 else 'Moderate' if cv < 40 else 'Difficult'}")

# Task 5: Weekly patterns
print("\n\n" + "="*80)
print("\nWeekly Demand Patterns:")

demand_df['Week_of_Year'] = demand_df['Date'].dt.isocalendar().week
weekly_patterns = demand_df.groupby(['Product', 'Week_of_Year'])['Demand'].mean().unstack(fill_value=0)

for product in demand_df['Product'].unique():
    product_weekly = weekly_patterns.loc[product]
    peak_week = product_weekly.idxmax()
    low_week = product_weekly.idxmin()
    
    print(f"\n{product}:")
    print(f"  Peak week: Week {peak_week} (Demand: {product_weekly.max():.0f})")
    print(f"  Low week: Week {low_week} (Demand: {product_weekly.min():.0f})")

# Task 6: Generate simple forecasts
print("\n\n" + "="*80)
print("\nForecast Generation:")

forecast_results = []

for product in demand_df['Product'].unique():
    product_data = demand_df[demand_df['Product'] == product].sort_values('Date')
    
    # Historical average
    hist_avg = product_data['Demand'].mean()
    
    # Last period average (last 13 weeks)
    recent_avg = product_data.iloc[-13:]['Demand'].mean()
    
    # Moving average (8-week)
    ma_8 = product_data['Demand'].rolling(window=8).mean().iloc[-1]
    
    # Forecast next period (weighted average of methods)
    forecast = (hist_avg * 0.3 + recent_avg * 0.5 + ma_8 * 0.2)
    
    forecast_results.append({
        'Product': product,
        'Historical_Avg': hist_avg,
        'Recent_Avg': recent_avg,
        'MA_8W': ma_8,
        'Forecast_Next_Period': forecast
    })

forecast_df = pd.DataFrame(forecast_results).round(0)
print("\nForecast Summary (Next Week):")
print(forecast_df)

# Task 7: Recommended safety stock
print("\n\n" + "="*80)
print("\nSafety Stock Recommendations:")

for product in demand_df['Product'].unique():
    product_data = demand_df[demand_df['Product'] == product]['Demand']
    
    mean_demand = product_data.mean()
    std_demand = product_data.std()
    
    # Safety stock for 95% service level (Z=1.65)
    safety_stock_95 = 1.65 * std_demand
    
    # Safety stock for 99% service level (Z=2.33)
    safety_stock_99 = 2.33 * std_demand
    
    print(f"\n{product}:")
    print(f"  Mean Demand: {mean_demand:.0f}")
    print(f"  Demand Std Dev: {std_demand:.0f}")
    print(f"  Safety Stock (95% SL): {safety_stock_95:.0f} units")
    print(f"  Safety Stock (99% SL): {safety_stock_99:.0f} units")
    print(f"  Months of Supply (95% SL): {safety_stock_95 / (mean_demand/4.3):.1f} months")

# Task 8: Recommendations
print("\n\n" + "="*80)
print("\nDemand Planning Recommendations:")

print("\n1. PRODUCT CLASSIFICATION:")
for product in product_stats.index:
    cv = product_stats.loc[product, 'CV_%']
    if cv < 20:
        print(f"   {product}: PREDICTABLE - Use simple forecasting methods")
    elif cv < 40:
        print(f"   {product}: MODERATE - Use trend-seasonal decomposition")
    else:
        print(f"   {product}: ERRATIC - Increase safety stock, shorter lead times")

print("\n2. INVENTORY POLICY:")
print("   • High seasonality: Implement seasonal adjustments in forecasts")
print("   • Growing demand: Increase safety stock during growth phases")
print("   • Volatile products: Consider vendor-managed inventory (VMI)")

print("\n3. REPLENISHMENT STRATEGY:")
print("   • Weekly review recommended for all products")
print("   • Dynamic safety stock based on forecast error")
print("   • Adjust reorder points quarterly based on trends")

print("\n4. FORECAST IMPROVEMENT:")
print("   • Implement exponential smoothing for trend products")
print("   • Use seasonal decomposition for Q4 peaks")
print("   • Collaborate with sales for demand signals")
print("   • Review and adjust forecasts monthly")

print("\n\nSummary:")
print(f"• Average Demand Volatility: {demand_df.groupby('Product')['Demand'].std().mean():.0f} units")
print(f"• Highest CV Product: {product_stats['CV_%'].idxmax()} ({product_stats['CV_%'].max():.1f}%)")
print(f"• Lowest CV Product: {product_stats['CV_%'].idxmin()} ({product_stats['CV_%'].min():.1f}%)")
print(f"• Overall Forecast Confidence: {100 - demand_df.groupby('Product')['Demand'].std().mean()/demand_df['Demand'].mean()*100:.1f}%")
