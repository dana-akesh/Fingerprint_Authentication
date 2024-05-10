import os
import cv2
import sys
import re
import numpy as np

import roc


class Color:
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'


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
    filenames = sorted(os.listdir(path), key=lambda x: (int(x.split('person')[1].split('.')[0])))
    for i in range(len(filenames)):
        filename = filenames[i]
        img = cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(img, (100, 100))
        dataset_list.append(np.array(img_resized))
    return dataset_list


def match_image(image1, image2):
    # calculate the similarity score based on the Euclidean distance
    similarity_score = np.sqrt(np.sum((image1 - image2) ** 2))
    return similarity_score


def get_user_number(image_path):
    name = image_path.split('/')
    name_part = name[-1]
    user_number = name_part.split('_')
    match = re.search(r'\d{1,2}', user_number[0])
    if match:
        return match.group()
    else:
        return None


def get_user_type(image_path):
    name = image_path.split('/')
    name_part = name[-1]
    if "person" in name_part:
        return "p"
    elif "hacker" in name_part:
        return "h"
    else:
        return None


def main():
    real_datalist = prepare_data("../Fingerprint_Authentication/dataset/real")
    # altered_datalist = prepare_data("../Fingerprint_Authentication/dataset/altered")
    # hacker_datalist = prepare_data("../Fingerprint_Authentication/dataset/hacker")

    while True:
        print_menu()
        choice = input("-> Enter your choice: ")
        if choice == "1":
            user_number = input("-> Enter the user number(1-13): ")
            image_path = input("-> Enter the path of the image ☺: ")
            image, image_np = read_image(image_path)
            get_user_number(image_path)
            if image is None:
                print(Color.RED + "Error: Image not read successfully !!" + Color.END)
                continue

            score_list = []
            i = 1
            # loop the input image with the real dataset and save the similarity score in a list
            for real_data in real_datalist:
                score = match_image(image_np, real_data)
                score_list.append(score)
                print("User number:", i, "|| Score:", score / 1000)
                i += 1

            # calculate the mean (adaptive threshold)
            mean_score = np.mean(score_list)
            print(Color.BLUE + "Mean score:", mean_score, Color.END)

            # calculate the standard deviation
            std_dev = np.std(score_list)
            std_dev = std_dev * 11
            std_dev = std_dev - mean_score
            print(Color.BLUE + "Standard deviation:", std_dev, Color.END)

            # threshold = std_dev
            threshold = mean_score
            print("Threshold", threshold / 1000)

            if score_list[int(user_number) - 1] < threshold:
                if ((get_user_type(image_path))[0] != "p") and (user_number != (get_user_number(image_path))):
                    print(Color.GREEN + "** Approved" + Color.END)
                elif ((get_user_type(image_path))[0] == "p") and (user_number != (get_user_number(image_path))):
                    print(Color.GREEN + "** Approved" + Color.END)
                else:
                    print(Color.GREEN + "** Hello user, Approved" + Color.END)
            else:
                if (get_user_type(image_path)) == "h":
                    print(Color.RED + "** Hacker!! Rejected" + Color.END)
                elif ((get_user_type(image_path)) == "p") and (user_number == (get_user_number(image_path))):
                    print(Color.RED + "** Rejected" + Color.END)
                else:
                    print(Color.RED + "** Rejected, you are not the user!!" + Color.END)

        elif choice == "2":
            roc.plot_pre_roc_curve()
            print("ROC curve plotted successfully!!")
        elif choice == "3":
            print("Exiting the system...")
            sys.exit()
        else:
            print("Invalid. Please enter a valid choice!!")


def print_menu():
    print(Color.PURPLE + "-----------------Fingerprint Authentication System-----------------" + Color.END)
    print(Color.YELLOW + "1. Match the image (Log in the system)" + Color.END)
    print(Color.YELLOW + "2. Print the roc" + Color.END)
    print(Color.YELLOW + "3. Exit" + Color.END)


if __name__ == "__main__":
    #  ../Fingerprint_Authentication/dataset/altered/person6_v1.bmp
    #  ../Fingerprint_Authentication/dataset/real/person1.bmp
    #  ../Fingerprint_Authentication/dataset/hacker/hacker7.bmp
    main()
