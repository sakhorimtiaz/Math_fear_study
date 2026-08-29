import pandas as pd
import random

# 1. Setup Demographics (100 Students: 33 Class 6, 34 Class 7, 33 Class 9)
classes = [6]*33 + [7]*34 + [9]*33
versions = random.choices(['Bangla', 'English'], k=100)
sections = random.choices(['A', 'B', 'C', 'D', 'E'], k=100)
student_ids = [f"S{str(i).zfill(3)}" for i in range(1, 101)]

# 2. Extract Exact Variables from the Final OMR Form
part_b_5pt = [f"B{i}" for i in range(1, 10)]
part_b_4pt = [f"C{i}" for i in range(1, 9)]
part_c_rev = ["D1", "D2", "D3", "D4", "D5", "D6", "E2", "E4", "E5", "E6", "E7",
              "F1", "F2", "F3", "F4", "F5", "F6", "G1", "G2", "G4"]
part_d_5pt = ["EN1", "EN3", "FN7", "GN3", "GN5", "GN6", "GN7", "GN8",
              "HN1", "HN2", "HN3", "HN5", "HN6"]

# 3. Generate Randomized Demo Data
data = {
    "StudentID": student_ids,
    "Class": classes,
    "Version": versions,
    "Section": sections
}

for col in part_b_5pt: data[col] = random.choices([1, 2, 3, 4, 5], k=100)
for col in part_b_4pt: data[col] = random.choices([1, 2, 3, 4], k=100)
for col in part_c_rev: data[col] = random.choices([5, 4, 3, 2, 1], k=100)
for col in part_d_5pt: data[col] = random.choices([1, 2, 3, 4, 5], k=100)

# 4. Export directly to an Excel Spreadsheet
df = pd.DataFrame(data)

new_path = r'C:\Users\THINKPAD\Downloads\math_fear_demo_data.csv'
df.to_csv(new_path, index=False, encoding='utf-8')
