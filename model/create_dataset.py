import os
import shutil
import pandas as pd

#  Correct paths for YOUR project
excel_path = "dataset/smartphone_raw/dataset.xlsx"
image_dir = "dataset/smartphone_processed"
final_dir = "Final"

#  Create output class folders
classes = ["Good", "Moderate", "Unhealthy", "Severe"]
for c in classes:
    os.makedirs(os.path.join(final_dir, c), exist_ok=True)

#  Read Excel file (IMPORTANT — not CSV)
df = pd.read_excel(excel_path)

#  Category mapping (VisionAir → 4 classes)
def map_category(cat):
    cat = str(cat).lower()

    if "good" in cat:
        return "Good"

    elif "moderate" in cat:
        return "Moderate"

    elif "sensitive" in cat or cat.strip() == "unhealthy":
        return "Unhealthy"

    elif "very" in cat or "hazardous" in cat:
        return "Severe"

    else:
        return None


# Copy images into class folders
for _, row in df.iterrows():

    img_num = row["Image no."]
    category = map_category(row["AQI Category"])

    if category is None:
        continue

    src = os.path.join(image_dir, f"{int(img_num)}.jpg")
    dst = os.path.join(final_dir, category, f"{int(img_num)}.jpg")

    if os.path.exists(src):
        shutil.copy(src, dst)
    else:
        print(f"Missing image: {src}")

print("Dataset creation completed")