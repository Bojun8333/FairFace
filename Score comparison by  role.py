import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Model selection: 'dell', 'dreamlike_v2' or 'SD'
model = 'dell'
score_folder = f'/content/drive/MyDrive/Fireface/Score/{model}_Score'
roles = ['CEO', 'Doctor', 'Scientist', 'BeautifulPerson']

# Summarize all role data
dfs = []
for role in roles:
    path = os.path.join(score_folder, f'{role}_{model}_Stereotype_Score.csv')
    df = pd.read_csv(path)
    df['Role'] = role
    df['Model'] = model
    dfs.append(df)

# Merge
df_all = pd.concat(dfs, ignore_index=True)

# Draw a picture
plt.figure(figsize=(10, 6))
sns.boxplot(x='Role', y='Stereotype Score', data=df_all, palette='Set3')
sns.stripplot(x='Role', y='Stereotype Score', data=df_all, color='black', size=3, jitter=True, alpha=0.5)
plt.title(f'{model} Model distribution of stereotype scores for each character')
plt.ylabel('Stereotype Score')
plt.xlabel('Role')

# Save
output_path = '/content/drive/MyDrive/Fireface/Score/Score_Distributions1'
os.makedirs(output_path, exist_ok=True)
plt.savefig(os.path.join(output_path, f'{model}_Score_By_Role.png'))
plt.show()
