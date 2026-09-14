import pandas as pd

# Load the real dataset
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data.csv',encoding='utf-8')

# 1. Identify columns that actually contain the 1-5 scale responses
# (Assuming they start from column index 4 onwards, skipping ID, Class, Version, Section)
question_columns = df.columns[4:]

# 2. Fill blanks (NaN) with the median value of that specific column
for col in question_columns:
    if df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

new_path = r'C:\Users\THINKPAD\Downloads\math_fear_real_data_no_null.csv'
df.to_csv(new_path, index=False, encoding='utf-8')
