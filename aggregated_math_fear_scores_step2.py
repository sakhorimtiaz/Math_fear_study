import pandas as pd

# 1. Load your generated demo data
old_path = r'C:\Users\THINKPAD\Downloads\math_fear_demo_data.csv'
df = pd.read_csv(old_path, encoding='utf-8')

# 2. Define the exact columns for each psychological construct
# (Combining both standard and 'N' reverse-logic variables)
group_b_cols = [f'B{i}' for i in range(1, 10)]
group_c_cols = [f'C{i}' for i in range(1, 9)]
group_d_cols = [f'D{i}' for i in range(1, 7)]
group_e_cols = ['E2', 'E4', 'E5', 'E6', 'E7', 'EN1', 'EN3']
group_f_cols = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'FN7']
group_g_cols = ['G1', 'G2', 'G4', 'GN3', 'GN5', 'GN6', 'GN7', 'GN8']
group_h_cols = ['HN1', 'HN2', 'HN3', 'HN5', 'HN6']

# 3. Calculate total numerical scores for each group per student
df['Score_B (Math Anxiety)'] = df[group_b_cols].sum(axis=1)
df['Score_C (Test Anxiety)'] = df[group_c_cols].sum(axis=1)
df['Score_D (Math Thinking)'] = df[group_d_cols].sum(axis=1)
df['Score_E (Classroom Safety)'] = df[group_e_cols].sum(axis=1)
df['Score_F (Exam Self-Reg)'] = df[group_f_cols].sum(axis=1)
df['Score_G (Academic Pressure)'] = df[group_g_cols].sum(axis=1)
df['Score_H (Exam Phobia)'] = df[group_h_cols].sum(axis=1)

# 4. Filter the dataframe to show only the Student ID and their new grouped scores
summary_chart = df[[
    'StudentID', 'Class', 'Version',
    'Score_B (Math Anxiety)', 'Score_C (Test Anxiety)',
    'Score_D (Math Thinking)', 'Score_E (Classroom Safety)',
    'Score_F (Exam Self-Reg)', 'Score_G (Academic Pressure)',
    'Score_H (Exam Phobia)'
]]

# 5. Display the first 10 rows in the console to verify
print(summary_chart.head(10))

# 6. Export this cleaned, aggregated chart to a new CSV for correlation testing
new_path = r'C:\Users\THINKPAD\Downloads\aggregated_math_fear_scores.csv'

# Change 'df' to 'summary_chart' here:
summary_chart.to_csv(new_path, index=False, encoding='utf-8')

print("\nAggregated chart successfully saved as 'aggregated_math_fear_scores.csv'.")
