# Skygnosis

## Overview
Skygnosis is a machine learning-based system designed to estimate Air Quality Index (AQI) levels from sky images. The project leverages computer vision techniques to analyze visual patterns in sky conditions and classify air quality into predefined categories.

## Problem Statement
Traditional AQI monitoring relies on physical sensors, which may not always be accessible or cost-effective. This project explores an alternative approach using image-based analysis to estimate AQI levels.

A key challenge encountered during development is **dataset bias**, as the available smartphone dataset contains a disproportionate number of samples from certain AQI categories. This leads to skewed model predictions, which the project aims to address through improved data strategies and model refinement.

## Features
- Image preprocessing and sky segmentation
- AQI classification using deep learning models
- Bias identification in imbalanced datasets
- Modular pipeline for training and evaluation
- Android application (in progress) for real-time predictions

## Dataset
- Smartphone-based sky image dataset
- Preprocessed to remove non-sky elements such as buildings and trees
- Labeled into AQI categories (e.g., Good, Unhealthy, Very Unhealthy)

## Methodology
1. Data Cleaning and Preprocessing
2. Sky Region Extraction
3. Model Training (CNN-based architecture)
4. Bias Analysis due to class imbalance
5. Model Evaluation and Prediction

## Current Challenges
- Class imbalance leading to biased predictions
- Limited availability of diverse AQI image datasets
- Need for improved generalization across different environments

## Future Work
- Integration of additional datasets to reduce bias
- Data augmentation and rebalancing techniques
- Deployment of a fully functional mobile application
- Real-time AQI estimation using live camera input


## Contributors
- Vanshika – Model development, data preprocessing, system design, Application development, Implimentation (in progress)
- Kirti Saini – 

## Status
 Work in progress 

## License
This project is for academic and research purposes.
