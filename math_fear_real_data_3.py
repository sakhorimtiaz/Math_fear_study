import pandas as pd

# Load the item-level data and the new average-based aggregated data
df_items = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data_no_null.csv')
df_agg = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data_aggregated.csv')

# Merge based on StudentID
df_merged = pd.merge(df_items, df_agg, on='StudentID')

# Calculate correlation between a specific item (e.g., D2) and the new Average column
corr_d2_b = df_merged['G2'].corr(df_merged['Avg_B (Math Anxiety)'])
corr_f3_b = df_merged['F3'].corr(df_merged['Avg_B (Math Anxiety)'])

print(f"Correlation between D2 and Average Math Anxiety: {corr_d2_b:.3f}")
print(f"Correlation between F3 and Average Math Anxiety: {corr_f3_b:.3f}")
