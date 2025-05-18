import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Path setting: CSV and chart save paths
csv_path = '/content/drive/MyDrive/Fireface/Scientist_dreamlike_v2_result/deepface_analysis_Scientist_dreamlike_v2_results.csv'
output_dir = '/content/drive/MyDrive/Fireface/Scientist_dreamlike_v2_result'

# Read the analysis results
df = pd.read_csv(csv_path)

# Age Distribution Map
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Age Distribution (Scientist)')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'scientist_age_distribution.png'))
plt.show()

# Gender Pie Chart
plt.figure(figsize=(6, 6))
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'pink'])
plt.title('Gender Distribution (Scientist)')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'scientist_gender_distribution.png'))
plt.show()

# Race Bar Chart
plt.figure(figsize=(10, 6))
sns.countplot(y='Race', data=df, order=df['Race'].value_counts().index, palette='viridis')
plt.title('Race Distribution (Scientist)')
plt.xlabel('Count')
plt.ylabel('Race')
plt.savefig(os.path.join(output_dir, 'scientist_race_distribution.png'))
plt.show()
