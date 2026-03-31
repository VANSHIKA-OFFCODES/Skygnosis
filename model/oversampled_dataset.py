import os
import shutil
import random

# Paths
original_dataset = r"D:\AQI_ESTIMATION\model\Final"
new_dataset = r"D:\AQI_ESTIMATION\model\oversampled_dataset"

# Target count (you can adjust)
TARGET_COUNT = 300

# Create new dataset folder
if not os.path.exists(new_dataset):
    os.makedirs(new_dataset)

for class_name in os.listdir(original_dataset):
    class_path = os.path.join(original_dataset, class_name)
    new_class_path = os.path.join(new_dataset, class_name)

    os.makedirs(new_class_path, exist_ok=True)

    images = os.listdir(class_path)

    # Copy existing images
    for img in images:
        shutil.copy(os.path.join(class_path, img), new_class_path)

    # Oversample (duplicate)
    while len(os.listdir(new_class_path)) < TARGET_COUNT:
        img = random.choice(images)
        src = os.path.join(class_path, img)

        new_name = f"copy_{random.randint(0,100000)}_{img}"
        dst = os.path.join(new_class_path, new_name)

        shutil.copy(src, dst)

print("Oversampled dataset created successfully!")