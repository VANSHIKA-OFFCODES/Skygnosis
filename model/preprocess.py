import os
import cv2
from tqdm import tqdm
import matplotlib.pyplot as plt

# Constants
SIZE = (224, 224)  
HEIGHT_CROP = 120 
input_path = 'dataset/smartphone_raw/images'  
output_path = 'dataset/smartphone_processed' 


os.makedirs(output_path, exist_ok=True)


files = os.listdir(input_path)
for file in tqdm(files):
    img_path = os.path.join(input_path, file)
    img = cv2.imread(img_path)  
    if img is not None and img.shape[0] > 0: 
        
        img_resized = cv2.resize(img, SIZE)

        
        img_cropped = img_resized[:HEIGHT_CROP, :]  

        
        output_img_path = os.path.join(output_path, file) 
        cv2.imwrite(output_img_path, img_cropped)
    else:
        print(f"Failed to process: {img_path}")

print(f"Processed images saved to {output_path}")
