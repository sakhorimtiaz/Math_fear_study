import pandas as pd

# 1. Load the item-level data and the new average-based aggregated data
df_items = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data_no_null.csv', encoding='utf-8')
df_agg = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data_aggregated.csv', encoding='utf-8')

# 2. Merge both datasets based on StudentID
df_merged = pd.merge(df_items, df_agg, on='StudentID')

# 3. Identify all individual question columns (skipping ID, Class, Version, Section)
item_columns = df_items.columns[4:]

# 4. Create an empty list to store the correlation results
correlation_data = []

# 5. Loop through each question to calculate correlations
for item in item_columns:
    # Calculate Pearson correlation, rounding to 3 decimal places for readability
    corr_math_anxiety = df_merged[item].corr(df_merged['Avg_B (Math Anxiety)']).round(3)
    corr_exam_phobia = df_merged[item].corr(df_merged['Avg_H (Exam Phobia)']).round(3)

    # Append the results to our list
    correlation_data.append({
        'Question_ID': item,
        'Corr_with_Math_Anxiety': corr_math_anxiety,
        'Corr_with_Exam_Phobia': corr_exam_phobia
    })

# 6. Convert the list into a Pandas DataFrame
df_correlations = pd.DataFrame(correlation_data)

# 7. Export the results to a single summary CSV
output_path = r'C:\Users\THINKPAD\Downloads\item_correlations_summary.csv'
df_correlations.to_csv(output_path, index=False, encoding='utf-8')

