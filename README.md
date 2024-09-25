# Fingerprint Authentication System

#### Contributers:  <a href="https://github.com/dana-akesh"> Dana Akesh

## Table of Contents:
- [Description](#Description)
- [Dataset](#Dataset)
- [Features](#Features)
- [Technologies](#Technologies)
- [Installation](#Installation)
- [Algorithm and Thresholding](#Algorithm-and-Thresholding)
- [Output](#Output)
- [ROC Curve](#ROC-Curve)


## Description:
This project focuses on fingerprint template matching, leveraging Euclidian Distance as the similarity measure with a dynamic threshold.
The project explores different thresholding techniques such as mean and variance and provides key biometric performance metrics like FMR, FNMR, and EER. 
The ROC curve is also plotted for further analysis.

## Dataset:
- Source: Kaggle <a href="https://www.kaggle.com/datasets/ruizgara/socofing"> SOCOFing dataset </a>.
- Content: 6,000 fingerprint images from 600 African individuals. 
- Labels: Includes gender, hand, and finger designation. 
- Alterations: Three levels: obliteration, central rotation, and z-cut. 
- Usage in Project: Randomly selected altered fingerprints will be used, and the data is split into two types of users: hackers and real users.


## Features:
- Euclidean distance algorithm is used to compare the fingerprints.
- The project uses the ROC curve to evaluate the performance of the model.
- 

## Technologies:
- Python -version 3.12.3
- OpenCV -version 4.9.0.80
- Numpy -version 1.26.4

## Installation:
- Clone the repository
```bash
git clone https://github.com/dana-akesh/Fingerprint_Authentication
cd Fingerprint_Authentication
```
- Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```
- Run the following command to execute the matching algorithm code:
```bash
python system.py
```
- Run the following command to execute the ROC curve code:
```bash
python roc.py
```

## Algorithm and Thresholding:
- The algorithm used in this project is the Euclidean distance algorithm.
- 

## Output:

## ROC Curve:

