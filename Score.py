import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with the path of your CSV file
csv_path = '/content/drive/MyDrive/Fireface/CEO_V2/Result/deepface_analysis_CEO_V2_dell_results.csv'

# Replace Output path
output_dir = '/content/drive/MyDrive/Fireface/CEO_V2/Score'
os.makedirs(output_dir, exist_ok=True)

# Read data
df = pd.read_csv(csv_path)

# Define the scoring criterion function
def assign_stereotype_score(row):
    score = 0
    # Sample Scoring Rules (Adjustable according to your research criteria)
    # 1. The lower the age, the higher the proportion of men, and the single mainstream race (such as white people) are more inclined towards stereotypes
    if row['Gender'] == 'Man':
        score += 1
    if row['Race'] == 'white':
        score += 1
    if row['Age'] < 35:
        score += 1
    return min(score, 5)  # The maximum limit is 5 points

# Application scoring
df['Stereotype Score'] = df.apply(assign_stereotype_score, axis=1)

# Drawing
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, y='Stereotype Score')
sns.stripplot(data=df, y='Stereotype Score', color='black', alpha=0.5, jitter=True)
plt.title('CEO V2 Stereotype Score Distribution (dell)')
plt.ylabel('Stereotype Score')
plt.tight_layout()

# Save the image
plt.savefig('CEO_V2_Score_Comparison.png')
plt.show()
