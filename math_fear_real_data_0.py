import pandas as pd

# 1. Load the raw dataset
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\math_fear_real_data.csv', encoding='utf-8')

# 2. Apply the reverse-scoring correction specifically to the E5 column
df['E5'] = 6 - df['E5']

# 3. Export the corrected dataset
new_path = r'C:\Users\THINKPAD\Downloads\math_fear_real_data_E5_corrected.csv'
df.to_csv(new_path, index=False, encoding='utf-8')
