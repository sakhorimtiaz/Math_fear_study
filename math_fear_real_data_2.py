import pandas as pd

# 1. Load the pre-cleaned dataset (nulls already handled)
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data_no_null.csv', encoding='utf-8')

# 2. Define the exact variables for each psychological construct
b_cols = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
c_cols = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
d_cols = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
e_cols = ['E2', 'E4', 'E5', 'E6', 'E7', 'EN1', 'EN3']
f_cols = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'FN7']
g_cols = ['G1', 'G2', 'G4', 'GN3', 'GN5', 'GN6', 'GN7']
h_cols = ['HN1', 'HN2', 'HN3', 'HN5', 'HN6']

# 3. Create the new aggregated dataframe
df_agg = pd.DataFrame()
df_agg['StudentID'] = df['StudentID']
df_agg['Class'] = df['Class']
df_agg['Version'] = df['Version']
df_agg['Section'] = df['Section']

# 4. Calculate the average (mean) for each construct, rounded to 2 decimal places
df_agg['Avg_B (Math Anxiety)'] = df[b_cols].mean(axis=1).round(2)
df_agg['Avg_C (Test Anxiety)'] = df[c_cols].mean(axis=1).round(2)
df_agg['Avg_D (Math Thinking)'] = df[d_cols].mean(axis=1).round(2)
df_agg['Avg_E (Classroom Safety)'] = df[e_cols].mean(axis=1).round(2)
df_agg['Avg_F (Exam Self-Reg)'] = df[f_cols].mean(axis=1).round(2)
df_agg['Avg_G (Academic Pressure)'] = df[g_cols].mean(axis=1).round(2)
df_agg['Avg_H (Exam Phobia)'] = df[h_cols].mean(axis=1).round(2)


# 5. Export the finalized dataset
new_path = r'C:\Users\THINKPAD\Downloads\math_fear_real_data_aggregated.csv'
df_agg.to_csv(new_path, index=False, encoding='utf-8')
