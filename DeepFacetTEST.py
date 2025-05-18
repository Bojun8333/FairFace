import os
import pandas as pd
from deepface import DeepFace
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path of your picture folder
image_folder = '/content/drive/MyDrive/Fireface/Scientist_dreamlike_v2'

# Supported image formats
image_formats = (".jpg", ".jpeg", ".png", ".PNG")

# Save the list of results
results = []

# Traverse the pictures and analyze them
for img_file in tqdm(os.listdir(image_folder)):
    if img_file.lower().endswith(image_formats):
        img_path = os.path.join(image_folder, img_file)
        try:
            analysis = DeepFace.analyze(img_path=img_path,
                                        actions=['age', 'gender', 'race'],
                                        enforce_detection=False)
            results.append({
                'Image': img_file,
                'Age': analysis[0]['age'],
                'Gender': analysis[0]['dominant_gender'],
                'Race': analysis[0]['dominant_race']
            })
        except Exception as e:
            print(f"❌ Error processing {img_file}: {e}")

# Convert to a DataFrame
df_results = pd.DataFrame(results)

# Display the result table
display(df_results)

# Save the CSV to your Google Drive
output_csv_path = '/content/drive/MyDrive/Fireface/Scientist_dreamlike_v2_result/deepface_analysis_Scientist_dreamlike_v2_results.csv'
#change to your path
df_results.to_csv(output_csv_path, index=False)
print(f"✅ 检测结果已保存至: {output_csv_path}")