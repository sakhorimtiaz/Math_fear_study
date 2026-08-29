import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the aggregated dataset
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\aggregated_math_fear_scores.csv')

# 2. Select only the columns that contain the grouped scores
score_cols = [col for col in df.columns if 'Score' in col]

# 3. Calculate the Pearson correlation matrix
corr_matrix = df[score_cols].corr()

# 4. Set up the matplotlib figure size
plt.figure(figsize=(10, 8))

# 5. Draw the heatmap with Seaborn
sns.heatmap(
    corr_matrix,
    annot=True,          # Show the correlation numbers inside the squares
    cmap='coolwarm',     # Use a blue-to-red color scale
    vmin=-1,             # Set minimum scale to -1 (strong negative correlation)
    vmax=1,              # Set maximum scale to 1 (strong positive correlation)
    fmt=".2f",           # Format numbers to 2 decimal places
    linewidths=.5        # Add lines between squares for readability
)

# 6. Add title and format labels
plt.title('Correlation Heatmap of Math Anxiety Constructs', fontsize=14)
plt.xticks(rotation=45, ha='right') # Tilt the x-axis labels so they don't overlap
plt.tight_layout()                  # Automatically adjust layout so nothing gets cut off

# 7. Save and display
plt.savefig('correlation_heatmap.png')
plt.show()
