Overview

Skygnosis is a machine learning-based system designed to estimate Air Quality Index (AQI) levels from sky images. The idea is to use computer vision to capture visual patterns in the sky and map them to different air quality categories.

Problem Statement

Traditional AQI monitoring depends on physical sensors, which are not always easily accessible or affordable. This project explores whether image-based analysis can act as an alternative way to estimate AQI.

While working on this, one major issue that came up was dataset bias. The smartphone dataset used here is not evenly distributed across AQI categories, which leads to skewed predictions. A significant part of this project focuses on identifying and dealing with that imbalance.

Features
-Image preprocessing and basic sky segmentation
-AQI classification using deep learning
-Identification and analysis of dataset bias
-Multiple experimental setups for comparison
-Modular pipeline for training and evaluation
-Android application (in progress) for real-time prediction

Dataset

-Smartphone-based sky image dataset
-Preprocessed to remove non-sky elements like buildings and trees
-Categorized into AQI levels (Good, Moderate, Severe, Unhealthy)

Methodology

The workflow evolved over time rather than being fixed from the start:

-Data cleaning and preprocessing

-Sky region extraction

-Baseline model training (CNN / ResNet50-based)

-Experiments with:

                  Data augmentation
                  Class weighting
                  Oversampling
                  Focal loss
                  
-Bias and performance analysis

-Robustness testing (adversarial + sensitivity analysis)

What I Observed
Baseline model struggled due to imbalance, Class weighting alone didn’t help much, Data augmentation improved performance noticeably, Oversampling helped stabilize training, Focal loss handled difficult samples better than expected

One interesting observation:
During adversarial testing, predictions often stayed the same, but confidence kept decreasing as perturbations increased.

Current Challenges

-Class imbalance affecting prediction quality
-Limited diversity in available AQI image datasets
-Generalization across different lighting and environments

Future Work

-Add more diverse datasets
-Improve balancing techniques
-Strengthen robustness against adversarial noise
-Complete and deploy the mobile application
-Explore real-time AQI prediction using live camera input

License

This project is intended for academic and research purposes.
