import os
import cv2
import sys
import numpy as np


def read_image(image_path):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(image, (100, 100))
        # convert the image to numpy array
        image_np = np.array(img_resized)
        return image, image_np
    except Exception as e:
        print("Error:", e)
        return None, None


def prepare_data(path):
    dataset_list = []
    for filename in os.listdir(path):
        if filename.endswith(".BMP"):
            filepath = os.path.join(path, filename)
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img_resized = cv2.resize(img, (100, 100))
            dataset_list.append(img_resized)
    dataset_list = np.array(dataset_list)
    # print("Shape of dataset_list:", dataset_list.shape)
    return dataset_list


def match_image(image1, image2):
    # calculate the similarity score based on the euclidean distance
    similarity_score = np.sqrt(np.sum((image1 - image2) ** 2))
    return similarity_score


def main():
    # prepare the datasets
    real_datalist = prepare_data("../Fingerprint_Authentication/dataset/real")
    # altered_datalist = prepare_data("../Fingerprint_Authentication/dataset/altered")
    # impostor_datalist = prepare_data("../Fingerprint_Authentication/dataset/imposter")

    image_path = input("Enter the path of the image ☺: ")
    image, image_np = read_image(image_path)
    if (image is None):
        print("Error: Image not read successfully !!")
        return

    score_list = []
    # loop the input image with the real dataset and save the similarity score in a list
    for real_data in real_datalist:
        score = match_image(image_np, real_data)
        score_list.append(score)
        print("Score:", score)

    # todo: check the threshold values
    # calculate the mean
    mean_score = np.mean(score_list)
    print("Mean score:", mean_score)

    # calculate the standard deviation
    std_dev = np.std(score_list)
    std_dev = std_dev * 7
    std_dev = std_dev - mean_score
    print("Standard Deviation:", std_dev)

    # scorelist < mean_score => approved
    for score in score_list:
        if score < std_dev:
            print("Approved")
        else:
            print("Rejected")


if __name__ == "__main__":
    #  ../Fingerprint_Authentication/dataset/altered/person6_v1.bmp
    main()
