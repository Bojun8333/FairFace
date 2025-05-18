import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Modify the save path to your Google Drive
output_dir = '/content/drive/MyDrive/Fireface/Score/Score_Distributions1'
os.makedirs(output_dir, exist_ok=True)

# The scoring file paths of the three models
files = {
    'dell': '/content/drive/MyDrive/Fireface/Score/dell_Score/Doctor_dell_Stereotype_Score.csv',
    'dreamlike_v2': '/content/drive/MyDrive/Fireface/Score/DreamlikeV2_Score/Doctor_dreamlike_v2_Stereotype_Score.csv',
    'SD': '/content/drive/MyDrive/Fireface/Score/SD_Score/Doctor_SD_Stereotype_Score.csv'
}

df_list = []

# Read and merge the data
for model_name, path in files.items():
    df = pd.read_csv(path)
    df = df[['Stereotype Score']].copy()
    df = df.rename(columns={'Stereotype Score': 'Score'})
    df['Model'] = model_name
    df_list.append(df)

df_all = pd.concat(df_list, ignore_index=True)

# Generate a box plot and scatter plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Model', y='Score', data=df_all, palette='Set2')
sns.stripplot(x='Model', y='Score', data=df_all, color='black', size=4, jitter=True, alpha=0.6)
plt.title('Doctor Stereotype Score Distribution by Model')
plt.ylabel('Stereotype Score')
plt.savefig(os.path.join(output_dir, 'Doctor_Score_Comparison.png'))
plt.show()
