# Fingerprint Authentication System

#### Contributers:  <a href="https://github.com/dana-akesh"> Dana Akesh

## Table of Contents:
- [Description](#description)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Algorithm](#algorithm)
- [Feature Extraction](#feature-extraction)
- [Threshold](#threshold)
- [Output](#output)
- [ROC Curve](#roc-curve)


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
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/user-attachments/assets/a2a47f43-2a66-4857-a8ff-5590e39eb462" width="150">
    <img src="https://github.com/user-attachments/assets/11233579-d74c-4205-ba60-78a858209bf7" width="150">
    <img src="https://github.com/user-attachments/assets/d77fd510-249b-467f-b214-c39904a6d44c" width="150">
    <img src="https://github.com/user-attachments/assets/a4bb1eb5-b7a2-44e8-8478-3283d1de7dfa" width="150">
</div>

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

## Algorithm:
- Purpose: Identify similarities between biometric images.
- Euclidean Algorithm:
  - Measures similarity between fingerprint features.
  - Computes geometric differences between minutiae.
  - Matches based on the smallest Euclidean distance for high accuracy.
 
## Feature Extraction:
- Method:
  - Read photo using OpenCV’s imread.
  - Convert to a NumPy array to represent pixel values.
  - Simplifies comparison between images.
 
## Threshold:
- Purpose: Dynamically calculated to determine if the user is accepted into the system.
   - Mean: If the input photo's score is below the mean of all scores, it is approved.
   - <img src="https://github.com/user-attachments/assets/63dd40cc-467d-4249-83f2-a90925e6358b" alt="mean formula" width="300">
   - Standard Deviation: If the input photo's score is below the standard deviation, it is approved.
     - <img src="https://github.com/user-attachments/assets/cfc0d4b8-acd2-42ec-b22a-e51f36ea7313" alt="standard deviation formula" width="300">



## Output:
The image shows a real fingerprint photo matched with its corresponding registered template in the database. The person6.bmp photo achieved a similarity score of zero with the stored template, which is below the adaptive threshold (calculated as the mean of all scores).
<img src="https://github.com/user-attachments/assets/a51a95f6-75d0-47d9-a13c-7e166c834beb" alt="output sample">


## ROC Curve:
At a threshold of 0.1, the system mistakenly rejects legitimate users (low FNMR) and accepts malicious ones (high FMR) due to the small distance values. Increasing the threshold results in more logical distances, improving accuracy by rejecting malicious users and accepting legitimate ones.
![image](https://github.com/user-attachments/assets/57eea7b4-15e4-44ac-a6d1-8c838e6c290f)

